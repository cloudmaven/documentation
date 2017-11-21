---
title: AWS Email Notification System
keywords: aws, lambda, sns
last_updated: September 5, 2017
tags: [AWS, Lambda, SNS, cost]
summary: "AWS Email Notification System"
sidebar: mydoc_sidebar
permalink: aws_cost_notification_system.html
folder: aws
---


### Objective and Approach

This page is a walkthrough for building an email notifier into your AWS/DLT account. The main idea is to follow the recipe
and note the connectivity of AWS components as you go. What you get is an email every day in your Inbox where the lead line
tells you at a glance what you spent on the AWS cloud in the past 24 hours, as in: 



![pic0000](/documentation/images/aws/aws_email_summary.png)


We begin with a short glossary.


### Glossary


- **Lambda**: A function (piece of code) that runs automatically on AWS. You configure it but you do 
not 'set up a VM' on which it runs
- **SNS**: The AWS Simple Notification Service(SNS) which permits you to format and send emails 
automatically. In our case this action will be triggered by a Lambda function
- **S3**: Object storage on AWS, i.e. the place where *objects* are placed and accessed. An object 
in the S3 object store is for our purposes analogous to a file in a file system
- **spend**: The amount of money you owe at the end of a period of time (here: one day / 
one week) due to the resources you have used on AWS
- **tag**: A key-value pair associated with a resource. The number of tags you associate with 
a resource is unlimited; but the keys must be unique
- **Owner**: A reserved tag key where the value is an IAM User username 
- **IAM**: Identity and Access Management, the sphere of actions in AWS that control user accounts, roles, 
policies, and groups
- **IAM User**: A user identity assigned to a person that includes a username and authentication (password; 
possibly multi-factor authentication; public/private keys etcetera)
- **Access Keys**: Two fairly short strings associated with *IAM Users* for authentication; not to be conflated with AWS 
Key Pairs associated with EC2 instances. 
- **Group**: A set-like construct: IAM Users can be assigned to a Group
- **Role**: An entity that defines an assumable set of permissions to take actions. Roles are molecular.
- **Policy**: A text document that uses a particular (JSON) syntax to permit or restrict actions. Policies are atomic.


### What is the story line here?


Now that we have some reference terminology let's go ahead and describe what we are going to assemble.


#### The situation


You or one of your minions is the *Account Manager* for an **AWS** public cloud account provided via an 
intermediary company called **DLT**.  Your objectives are two-fold: You want to carry out your research 
computing tasks on the public cloud using this account; and you want to manage your costs and spending 
rates to minimize how much money you spend. 


#### The desired end result 


In your Inbox every day you and your selected account minders will receive an email summary of yesterday's 
spend on AWS.  The first piece of data is a bulk cost and this is followed by a cost breakdown by users. 
You will see at a glance how much you are burning and whether you've had an unauthorized access breach.  
This is measure of security against accidental cost overruns.


#### The *how* of this end result 


Again if terms are unfamiliar you are referred to the glossary above. 


In relation to your account: DLT has allocated an S3 bucket with a standardized name in which they record -- as text lines -- 
the hourly cost of virtually all of the account resources. An EC2 instance that has run for one hour at a cost of $0.17 will 
appear as a time-tagged entry in this cost ledger.  We refer to this ledger in S3 as the DLT billing record. 


The DLT billing record is updated only twice daily.  This update will be configured by you or your minions to trigger a Lambda 
function.  The Lambda function has permission to scan through the DLT billing record (comma separated text) to sum the costs of 
resources based split out on the basis of tags. The costs of untagged resources are also calculated. The summary of this costing 
exercise is then produced and distributed to an email distribution list using SNS.    


From a constructivist point of view we want to take the following steps: 

- Create a role assigned a single policy
- Create a lambda function that assumes this role and therefore has the policy's permissions
- Configure the lambda function for the account
- Configure a trigger that will invoke the lambda function 
  - This trigger is the creation of a new object in the S3 bucket where spending is recorded 
- Create an SNS topic and attach email subscribers to that topic


The figure illustrates the chain of events.


![pic0001](/documentation/images/aws/aws_cost_notification_system_001.png)


DLT appends billing events as records to a compressed CSV object in S3. The bucket has a standardized name:
**123456789012-dlt-utilization**.  This bucket is in US-East-1 (N.Virginia) so we do everything 
in that region.  The bucket is updated on a daily basis. 


For our purposes let us assume an account identifier **kilroy**.  Our task is burn notification so 
the lead string for the things we create will be **kilroy_burn**.  The lambda will be named kilroy_burn_lambda.
The SNS topic will be kilroy_burn_sns. The role will be kilroy_burn_role.  Again these are all in the 
US-East-1 (N.Virginia) region.


The kilroy_burn_lambda service is a Python script with an event handler method. This service is passed
an event that is parsed in code, eventually leading to parsing and analysis of the contents of the S3 bucket.


The Python script will aggregate cost information based on tags and resource type (e.g. EC2). 
For untagged billing the script summarizes cost by resource ID if the resource ID appears in the file. 


### 1 Role

- Log in to the AWS console as an admin with IAM privileges. 
- Verify that your region (upper right corner) is set to N.Virginia
- Have at hand your IAM User Access Keys (Access Key ID and Secret Access Key; two strings)
  - Here they will be called ACCESSKEYIDSTRING and SECRETACCESSKEYSTRINGXXXXXXXXXXXXXXX
- Go to the **IAM** services page and select **Roles**
- Create role of type Lambda and proceed to the permissions page
- Search for the managed policy **AWSLambdaExecute** and associate that with this role
- Name the role **kilroy_burn_role**
- Create the role


### 2 Lambda

- Go to the Lambda services page and Create function
- Author from scratch
- Name the lambda **kilroy_burn_lambda**
- Choose an existing role: **kilroy_burn_role**
- Create function
- Edit code inline (see below), select Python 3.6, keep event handler as lambda_function.lambda_handler




```
# last update: Nov 11, 2017
# author: Jin Qu
# this implementation: rob fatland (kilroy)
# contact: rob5@uw.edu
# programming environment: python3.6
#
# To modify this file for use with your own account search for the string 'kilroy mod'
# kilroy: This example file is made safe for publication using XXXX args

import json
import os
import boto3
import zipfile
import csv
import datetime
import urllib

# kilroy mod: Customize the start notification message if desired
print('kilroy says: starting kilroy_burn_lambda')


# check if today is Sunday (day 6 indexing from 0)
#   If so return True. Intent: A weekly cost summary will be added to the report
def IncludeWeeklySummary(): return datetime.datetime.utcnow().weekday() == 6


### choose which file(s) to parse
'''
    Pick up the most recently updated file;
    Since the cost info of the first day of a month might appear in the cost file of prior month:
    for weekly summary two files will be included.
'''
def FilePicker(contents_list):
    file_list, update_dt = [], []
    for con in contents_list:
        file_name = con['Key'].split('.')
        file_time = con['LastModified']
        if file_name[-1] == 'zip':
            file_list.append(con['Key'])
            update_dt.append(con['LastModified'].timestamp())
    update_dt = sorted(update_dt)
    # check if the current date is within the first 7 days of a month
    # If so output the two most recent files to handle month-end discontinuity
    # If not, output the most recent files
    current_d = datetime.datetime.utcnow().today().day
    if current_d <= 6:
        idx1, idx2 = update_dt.index(update_dt[-1]), update_dt.index(update_dt[-2])
        file_picked = [file_list[idx1], file_list[idx2]]
    else:
        idx = update_dt.index(update_dt[-1])
        file_picked = [file_list[idx]]
    return file_picked


# check if the line belongs to today or yesterday's usage
def dayChecker(line_elements, idx_dt):
    '''
    when parsing through the cost info file, this function checks if a 
    certain line contains info from the most recent 24 hrs
    ---
    arg:    
        array line_elements : a line of a csv file
        int idx_dt : the index of datetime
    return:
        bool  
    '''
    dt_on_line = line_elements[idx_dt]
    cur_dt = datetime.datetime.utcnow()
    time_elapsed = cur_dt - datetime.datetime.strptime(dt_on_line, '%Y-%m-%d %H:%M:%S')
    updated_last24 = False
    if time_elapsed.days == 0:
        updated_last24 = True
    return updated_last24

    # marker

# check if the line belongs to the current week
def weekChecker(line_elements, idx_dt):
    '''
    when parsing through the cost info file, this function checks if a certain line 
    contains info from the most recent 7 days
    ---
    arg:    
        array line_elements : a line of a csv file
        int idx_dt : the index of datetime
    return:
        bool  
    '''
    dt_on_line = line_elements[idx_dt]
    # get current datetime
    cur_dt = datetime.datetime.utcnow()
    # caculate days passed
    time_elapsed = cur_dt - datetime.datetime.strptime(dt_on_line, '%Y-%m-%d %H:%M:%S')
    pick_this_line = False
    if time_elapsed.days <= 6:
        pick_this_line = True
    return pick_this_line


### check if the resource is untagged, if true, return a tag, if not, return False
def untaggedChecker(line_elements, idx_tag1, idx_tag2, idx_tag3, idx_tag4):
    '''
    grab tags
    ---
    arg:    
        array line_elements : a line of a csv file
        int idx_tag1-idx_tag4 : the index of tag
    return:
        if there is a tag, return a string of the tag
        if not return bool False
    '''
    if line_elements[idx_tag1]: return line_elements[idx_tag1]
    if line_elements[idx_tag2]: return line_elements[idx_tag2]
    if line_elements[idx_tag3]: return line_elements[idx_tag3]
    if line_elements[idx_tag4]: return line_elements[idx_tag4]
    return False


### aggregate cost by tag and product name
def Agg(line_elements, aggs, tag, idx_pname, idx_dollar_blend, idx_dollar_unblend):
    '''
    aggregate blended and unblended cost by product name
    ---
    arg:    
        array line_elements : a line of a csv file
        dict aggs : a dictionary like this: {{tag1: {}}, {tag2: {}}, {tag3: {}}}
        int idx_pname, idx_dollar_blend, idx_dollar_unblend : the index of product name, quantity of blended and unblended cost
    return:
        updated aggs with aggregated cost
    '''
    # product name
    pname = line_elements[idx_pname]
    # cost
    cost_blend = float(line_elements[idx_dollar_blend])
    cost_unblend = float(line_elements[idx_dollar_unblend])
    if tag in aggs:
        aggs[tag]['total_blended_cost'] += cost_blend
        aggs[tag]['total_unblended_cost'] += cost_unblend
        if pname in aggs[tag]:
            aggs[tag][pname]['blended_cost'] += cost_blend
            aggs[tag][pname]['unblended_cost'] += cost_unblend
        else:
            aggs[tag][pname] = {'blended_cost': cost_blend, 'unblended_cost': cost_unblend}
            
    else:
        aggs[tag] = {'total_blended_cost': cost_blend, 'total_unblended_cost': cost_unblend, \
            pname: {'blended_cost': cost_blend, 'unblended_cost': cost_unblend}}



### cost aggregation parser (for daily)
def dailyAgg(file_path):
    '''
    parse through the csv file and generate daily cost summary
    ---
    arg:    
        str file_path : path to the cost file
    return:
        an array contains daily cost summary
        1, dict untagged : \{\{'resource id 1': $$$\}, 'resource id 2': $$$\};
        2, dict aggs : \{\{tag1: \{\}\}, \{tag2: \{\}\}, \{tag3: \{\}\}\};
# marker 3
        3, float total_blend;
        4, float total_unblend;
        5, float total_tagged_blend;
        6, float total_tagged_unblend;
        7, float total_untagged_blend;
        8, float total_untagged_unblend
    '''
    untagged, aggs = {}, {}
    total_blend, total_unblend, total_tagged_blend, total_tagged_unblend, \
    total_untagged_blend, total_untagged_unblend = 0, 0, 0, 0, 0, 0
    with open('/tmp/' + file_path, 'r', newline = '\n') as csvfile:
        lines = csv.reader(csvfile, delimiter=',', quotechar='"')
        for idx, line in enumerate(lines):
            if idx == 0:
                col_dict = {}
                for i, n in enumerate(line):
                    col_dict.update({n.strip(): i})
                # get index for tags (user:Name, user:Project)
                idx_tag1, idx_tag2, idx_tag3, idx_tag4 = col_dict['user:Owner'], \
                    col_dict['user:Project'], col_dict['user:ProjectName'], col_dict['user:Name']
                # get index for datetime
                idx_dt = col_dict['UsageEndDate']
                # get index for ProductName
                idx_pname = col_dict['ProductName']
                # use quantity has two, blended and unblended
                idx_dollar_blend = col_dict['BlendedCost']
                idx_dollar_unblend = col_dict['UnBlendedCost']
                # for untagged resources
                idx_resource = col_dict['ResourceId']
            else:
                # avoid parse the last few lines
                if line[idx_pname]:
                    if dayChecker(line, idx_dt):
                        tag = untaggedChecker(line, idx_tag1, idx_tag2, idx_tag3, idx_tag4)
                        total_blend += float(line[idx_dollar_blend])
                        total_unblend += float(line[idx_dollar_unblend])
                        if tag:
                            Agg(line, aggs, tag, idx_pname, idx_dollar_blend, idx_dollar_unblend)
                            total_tagged_blend += float(line[idx_dollar_blend])
                            total_tagged_unblend += float(line[idx_dollar_unblend])
                        else:
                            total_untagged_blend += float(line[idx_dollar_blend])
                            total_untagged_unblend += float(line[idx_dollar_unblend])

                            if line[idx_resource] in untagged:
                                untagged[line[idx_resource]]['total_blended_cost'] += float(line[idx_dollar_blend])
                                untagged[line[idx_resource]]['total_unblended_cost'] += float(line[idx_dollar_unblend])
                            else:
                                untagged[line[idx_resource]] = {}
                                untagged[line[idx_resource]]['total_blended_cost'] = float(line[idx_dollar_blend])
                                untagged[line[idx_resource]]['total_unblended_cost'] = float(line[idx_dollar_unblend])
    return [untagged, aggs, total_blend, total_unblend, \
            total_tagged_blend, total_tagged_unblend,total_untagged_blend, total_untagged_unblend]


# cost aggregation parser (for weekly)
def weeklyAgg(file_paths):
    '''
    parse through the csv file and generate weekly cost summary
    ---
    arg:    
        str file_path : path to the cost file
    return:
        an array contains daily cost summary
        1, dict untagged : \{\{'resource id 1': $$$\}, 'resource id 2': $$$\};
        2, dict aggs : \{\{tag1: \{\}\}, \{tag2: \{\}\}, \{tag3: \{\}\}\};
        3, float total_blend;
        4, float total_unblend;
        5, float total_tagged_blend;
        6, float total_tagged_unblend;
        7, float total_untagged_blend;
        8, float total_untagged_unblend
    '''
    untagged, aggs = {}, {}
    total_blend, total_unblend, total_tagged_blend, total_tagged_unblend, \
    total_untagged_blend, total_untagged_unblend = 0, 0, 0, 0, 0, 0

    for f in file_paths:
        with open('/tmp/' + f.split('.')[0]+'.csv', 'r', newline = '\n') as csvfile:
            lines = csv.reader(csvfile, delimiter=',', quotechar='"')
            for idx, line in enumerate(lines):
                if idx == 0:
                    col_dict = {}
                    for i, n in enumerate(line):
                        col_dict.update({n.strip(): i})
                    # get index for tags (user:Name, user:Project)
                    idx_tag1, idx_tag2, idx_tag3, idx_tag4 = col_dict['user:Owner'], \
                        col_dict['user:Project'], col_dict['user:ProjectName'], col_dict['user:Name']
                    # get index for datetime
                    idx_dt = col_dict['UsageEndDate']
                    # get index for ProductName
                    idx_pname = col_dict['ProductName']
                    # use quantity has two, blended and unblended
                    idx_dollar_blend = col_dict['BlendedCost']
                    idx_dollar_unblend = col_dict['UnBlendedCost']
                    # for untagged resources
                    idx_resource = col_dict['ResourceId']
                else:
                    # avoid parse the last few lines
                    if line[idx_pname]:
                        if weekChecker(line, idx_dt):
                            tag = untaggedChecker(line, idx_tag1, idx_tag2, idx_tag3, idx_tag4)
                            total_blend += float(line[idx_dollar_blend])
                            total_unblend += float(line[idx_dollar_unblend])
                            if tag:
                                Agg(line, aggs, tag, idx_pname, idx_dollar_blend, idx_dollar_unblend)
                                total_tagged_blend += float(line[idx_dollar_blend])
                                total_tagged_unblend += float(line[idx_dollar_unblend])
                            else:
                                total_untagged_blend += float(line[idx_dollar_blend])
                                total_untagged_unblend += float(line[idx_dollar_unblend])

                                if line[idx_resource] in untagged:
                                    untagged[line[idx_resource]]['total_blended_cost'] += float(line[idx_dollar_blend])
                                    untagged[line[idx_resource]]['total_unblended_cost'] += float(line[idx_dollar_unblend])
                                else:
                                    untagged[line[idx_resource]] = {}
                                    untagged[line[idx_resource]]['total_blended_cost'] = float(line[idx_dollar_blend])
                                    untagged[line[idx_resource]]['total_unblended_cost'] = float(line[idx_dollar_unblend])
        return untagged, aggs, total_blend, total_unblend, \
                total_tagged_blend, total_tagged_unblend,total_untagged_blend, total_untagged_unblend


### friendly print out aggregated cost
def BeautifulPrint(aggs, untagged, is_weekly_summary, *all_costs):
    '''
    give the cost summary generated by func dailyAgg or weeklyAgg, 
    output a reader-friendly string 
    ---
    arg:    


```






## Earlier version follows
### 1, Billing information in the S3 bucket

The billing record is located in the "509248752274-dlt-utilization" S3 bucket of the US East(N.Virginia) 
region. The following screenshot shows the files in this bucket. The billing information of a certain 
day can be found in the compressed csv file with the corresponding date in the file name. For example, 
the billing information of Aug, 9th 2017 will appear in the file named as 
"509248752274-aws-billing-detailed-line-items-with-resources-and-tags-2017-08.csv.zip". 
However, the billing information of the first day of every month might appear in the zipped csv file 
of the previous month.


![pic0002](/documentation/images/aws/aws_cost_notification_system_002.png)


### 2, Lambda service

The current version of lambda service was written in Python 3.6. The Lambda will get triggered once 
the "509248752274-dlt-utilization" S3 bucket gets updated. The Python code will download and unzip the most 
recently modified file from the bucket to local machine in the /tmp/ directory. Then the code will parse 
and summarize the billing information by aggregating costs based on user tags. If there is no any 
tag associated with the cost, the code will add up costs based on its resource ID. All costs without 
either user tags nor resource ID will be summed up together. There are two types of costs, blended 
costs and unblended cost. A good explanation of blended and unblended rate can be found from this 
article: 
[https://www.cloudyn.com/blog/blended-rates-vs-unblended-rates-real-life-use-case/](https://www.cloudyn.com/blog/blended-rates-vs-unblended-rates-real-life-use-case/)

The following screenshots show the configurations of the Lambda service.
![pic0003](/documentation/images/aws/aws_cost_notification_system_003.png)
![pic0004](/documentation/images/aws/aws_cost_notification_system_004.png)


### 3, Simple Notification Service (SNS)

After parsing and summarizing the file, the Lambda service will send a long string to the SNS containing all the 
cost information and its associated tags or resource ID. The screenshot below shows details of the SNS setup.


![pic0005](/documentation/images/aws/aws_cost_notification_system_005.png)


## Links


## Heads-up


- The S3 bucket for billing information does not always get updated daily. The update might take a 
vacation during the holidays!!! So should we consider to send 2 day or 3 day summary information 
to users in order to avoid missing anything?

- All time related information is based on UTC time zone!

## Next steps
- aggregate total

## Contact



{% include links.html %}
