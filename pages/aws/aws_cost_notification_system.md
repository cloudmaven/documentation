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


## Objective and Approach


This page is a walkthrough for building an email notifier into your AWS/DLT account. The main idea is to follow the recipe
and note the connectivity of AWS components as you go. What you get is an email every day in your Inbox where the lead line
tells you at a glance what you spent on the AWS cloud in the past 24 hours, as in: 



![pic0000](/documentation/images/aws/aws_email_summary.png)


This introductory segment is a brief glossary and a description of what you want to build.
The subsequent section is the step-by-step of building it. 


Editor: Please search for 'hobie' for places that need improvement on this pass (and delete this line).


### Glossary


- **AWS**: Amazon Web Services, the cloud vendor
- **DLT**: A cloud re-seller that provides AWS accounts to the University of Washington 
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


### Caveat emptor: How accurate is this method?


Short answer: Pretty accurate; but we're not completely satisfied with our results yet. Here is an 
example from December 2017 for two accounts showing pretty good agreement and only one peculiar discrepancy.
The 'Account' column is the daily spend our software generates for an AWS account provided through DLT. 
The **Cost Explorer** tool is available through the AWS browser console; so that is our reference for
what the system thinks we spent for the day.  Values are in US dollars.


| Date | Account 1 | Cost Explorer | Account 2 | Cost Explorer |
| ------- |: ------------ :|: ------------ :|: ------------ :| ------------ :|
| 16-Dec|130.19|127.01|19.87|18.6|
| 17-Dec|101.39|101.45|22.25|20.8|
| 18-Dec|101.47|101.41|19.2|17.75|
| 19-Dec|102.53|102.41|1.45|21.25|
| 20-Dec|99.13|102.41|20.4|20.06|
| 21-Dec|101.48|99.3|18.42|17.16|
| 22-Dec|99.3|99.29|18.39|17.02|
| 23-Dec|99.26|99.25|18.53|17.07|
| 24-Dec|99.21|99.2|18.43|17|
| 25-Dec|99.33|99.34|18.46|17.04|
| 26-Dec|99.29|99.29|18.72|17.28|



For the first account *our* approach gave $1132.58 for the period whereas the cost explorer gave 1130.36.
In the second case it was 194.12 compared to 201.03. 



### Cost-accounting scenario


You or one of your minions is the *Account Manager* for an **AWS** public cloud account provided via an 
intermediary company called **DLT**.  Your objectives are two-fold: You want to carry out your research 
computing tasks on the public cloud using this account; and you want to manage your costs and spending 
rates to minimize how much money you spend.  You also want to be sure -- every day -- that your cloud
spending has not become a runaway monster for some strange reason... like a nefarious third party got 
hold of your cloud access keys for example.


### Desired end result 


In your Inbox every day you and your selected account minders will receive an email summary of yesterday's 
spend on AWS.  The first piece of data is a bulk cost and this is followed by a cost breakdown by users. 
You will see at a glance how much you are burning to use the cloud. You will also notice any strange spikes
in spending, for example due to unauthorized access.  This is measure of security against accidental cost overruns.


## Tutorial


This segment walks the builder through the process. 


### The *how* of this end result 


Taking the glossary above as read: ... 


In relation to your account: DLT has allocated an S3 bucket with a standardized name in which they record -- as text lines -- 
the hourly cost of virtually all of your account resources. An EC2 instance that has run for one hour at a cost of $0.17 will 
appear as a time-tagged entry in this cost ledger.  This ledger in S3 is the DLT billing record. 


The DLT billing record is updated only twice daily.  One approach is to use this update as a trigger event which 
generates your bill. However we have deprecated this approach in favor of simply using AWS CloudWatch. This is an 
alarm that goes off every day and triggers a Lambda function that tallies up and emails your daily spend. 
Said Lambda function has permission to scan through the DLT billing record (which is comma separated text) to do 
its sums.  It is also doing account breakdown sums based on resource tagging.  The costs of untagged resources are 
also tallied. Notice therefore that you receive your total burn broken into a sum of tagged and un-tagged resources.
If resource tagging is an important part of your cost management (perhaps you are conducting two different 
research projects under one AWS/DLT account) then the *untagged* cost will give you an idea of what costs you
are currently not tracking.  


From a builder's point of view we take the following steps: 


- Create a role that has assigned to it a single policy (policies grant permissions to take action)
- Create a lambda function that assumes this role and therefore has the policy's permissions
- Configure the lambda function for the account
- Configure a trigger that will invoke the lambda function (the CloudWatch alarm)
- Create an SNS topic and attach email subscribers to that topic


The DLT billing record S3 bucket has a standardized name based on your account ID '123456789012':
**123456789012-dlt-utilization**.  This bucket is in US-East-1 (N.Virginia) so we do all of the 
cost notification building in that region.  


For our purposes let us assume an identifier strong '**kilroy**'.  As we are building a cost 'burn'
notification email let's use the string '**kilroy_burn**'.  The lambda will be named kilroy_burn_lambda.
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
  - Here they will be called XXXXXXXXXXXXXXXXX and XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
- Also have on hand your 12-digit account number; here we use 123456789012
- Go to the **IAM** services page and select **Roles**
- Create role of type Lambda and proceed to the permissions page
- Search for the managed policy **AWSLambdaExecute** and associate that with this role
- Name the role **kilroy_burn_role** (or your equivalent identifier)
  - Remember 'kilroy_burn' is an identifier for what we are doing: Reporting your daily burn
  - The _role is the name given to the role which is part of the overall machinery
- Create the role


### 2 Lambda


- Go to the Lambda services page and Create function
- Author from scratch
- Name the lambda **kilroy_burn_lambda**
  - As above 'kilroy_burn' identifiers this as a cost (burn) reporting tool
  - and _lambda labels the Lambda as a lambda. It's a bit redundant but we like it.
- Choose an existing role: **kilroy_burn_role**
- Create function
- Edit code inline (see below), select Python 3.6, keep event handler as lambda_function.lambda_handler
  - The code is included below these five steps for cut-and-paste
  - Modify the pasted code by searching for the string 'kilroy mod' and making modifications as directed 
- Environment variables and Tags may be left blank
  - It is good practice to tag everything; so we recommend entering the tag Key = Owner and Value = your User name
- Verify Execution role = kilroy_burn_role set in step 1
- Set Memory to 256MB and Timeout to 2 min 10 sec
- SAVE your settings so far


### 3 Lambda trigger


- Above the code box are tabs for Configuration and for Monitoring 
- In the Configuration tab find the Designer region which describes your lambda function Triggers
- Add a CloudWatch Events trigger


- hobie notes that this is where the Maven would include some details including a sub-section on setting up the CloudWatch...
- hobie notes that kilroy_burn_lambda is still configured to trigger off an S3 access (Get or Put Object) which seems like it should be deleted
  - bucket name is 123456789012-dlt-utilization
- hobie suggests there ought to be a method or button to push that triggers for testing...  but the S3 upload method is not it


### 4 SNS


- In the AWS console go to the SNS services page
- Select Create topic
- Enter the topic name (per the Python code in the lambda function): kilroy_burn_sns
- Enter the topic abbreviation, 10 characters; which will be in the From field of the email notifications
  - I used kilroyburn
- Continue to topic details and click Create subscription
  - Choose type = email and add your email address plus any others you think should receive notifications
- Click on Create subscription to send a confirmation email to yourself; and then confirm that 


You should now start receiving daily cost/burn summaries in your Inbox. Verify that this is working properly. 


### 5 Validation and Debugging


- hobie says the following five lines need to be deleted or modified
  - Upload a file to your S3 billing bucket 123456789012-dlt-utilization
    - One simple way is to install and configure an app like **S3 Browser**
    - You will need to use your personal access keys handy for the configure step
  - This upload creates a new object (the file you uploaded) in the bucket which triggers the lambda function
    - You should therefore receive in short order an email with your cost summary
  

#### Cost Explorer


Cost Explorer is a feature of the AWS browser console. You can access this using the top right dropdown menu 
and selecting My Billing Dashboard; then start the Cost Explorer.  In more detail:


- When you receive a billing statement you should compare it with the Cost Explorer estimate of yor daily burn
  - At the upper right of the console use your Account Name dropdown to select My Billing Dashboard
  - Link to the Cost Explorer and launch it
  - Use the Reports dropdown to select **Daily Costs**
  - A calendar drop-down allows you to select a time range (I use MTD); and you must click the **Apply** button
  - You should now see daily expense as a bar chart
    - You can hover over a particular day to get the exact value
    - One DLT accounts the current day cost will look low and tend to be inaccurate
  - This daily cost record should be -- we intend -- commensurate with the email notification you will now receive from lambda


#### Lambda monitoring tab


- If something is going wrong
  - click on the Monitoring tab at the top of your lambda service page (under the name of the lambda function)
  - You should see some dashboard charts indicating that the lambda function has been triggered
  - There is a useful link here to View logs in Cloudwatch
    - The logs on Cloudwatch are themselves links to log entries; her you can see diagnostics printed by the lambda function
    - This means you can set print statements in the lambda, save it, trigger it, and diagnose issue by looking at the output


hobie again points out the necessity for a non-upload-to-S3 trigger of the lambda...


#### Lambda Python code


Here is the lambda code circa Dec 27 2017.



```
# last update: Nov 11, 2017
# author: Jin Qu
# this implementation: Rob Fatland (kilroy), Amanda Lehr
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
    if 0 < time_elapsed.days <= 1: # AMANDA: If date falls between last 24 - 48 hours of trigger
        updated_last24 = True
    return updated_last24



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
        dict aggs : a dictionary like this: \{\{tag1: \{\}\}, \{tag2: \{\}\}, \{tag3: \{\}\}\}
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
        1, dict aggs : \{\{tag1: \{\}\}, \{tag2: \{\}\}, \{tag3: \{\}\}\};
        2, dict untagged : \{\{'resource id 1': $$$\}, 'resource id 2': $$$\};
        3, bool is_weekly_summary : True/False;
        4, *all_costs : float total_blend, float total_unblend, float total_tagged_blend, 
                        float total_tagged_unblend, float total_untagged_blend, float total_untagged_unblend
    return:
        str cost_summary
    '''
    total_blend, total_unblend, total_tagged_blend, total_tagged_unblend, \
    total_untagged_blend, total_untagged_unblend = [*all_costs]
    cur_time = datetime.datetime.utcnow()
    
    # dictionary for substituting full name with shorter name
    resource_name_map = {'Amazon Elastic Compute Cloud': 'EC2', 'Amazon Simple Storage Service': 'S3'}
    
    cost_agg = ' '
    
    cost_agg += 'TOTAL SPEND: ${} / ${} / ${} (Total/Tagged/Untagged)\n\n'.format(str(round(total_blend, 2)), \
        str(round(total_tagged_blend, 2)), str(round(total_untagged_blend, 2)))
    
    cost_agg += '~ ' * 20
    cost_agg += '\n'
    
    ## AMANDA: Fixed the printed dates 
    
    if is_weekly_summary:
        cost_agg += 'Cloud Czar WEEKLY spend = ${}(${}) from {} to {} \n'.format(str(round(total_tagged_blend, 2)), \
            str(round(total_untagged_blend, 2)), \
            datetime.datetime.fromtimestamp(int(datetime.datetime.utcnow().timestamp() - 86400.0 * 7)).strftime('%Y-%m-%d %H:%M:%S') + \
            ' UTC to ', cur_time.strftime('%Y-%m-%d %H:%M:%S') + ' UTC ')
    else:
        cost_agg += 'Cloud Czar DAILY spend from {} to {} \n'.format(datetime.datetime.fromtimestamp(int(datetime.datetime.utcnow().timestamp() - 86400.0 * 2)).strftime('%Y-%m-%d %H:%M:%S') + \
                                                                     ' UTC to ', datetime.datetime.fromtimestamp(int(datetime.datetime.utcnow().timestamp() - 86400.0)).strftime('%Y-%m-%d %H:%M:%S') + ' UTC ')
    cost_agg += '~ ' * 20 
    cost_agg += '\n'
    
    
    ### Get usage summary OWNER:Total
    cost_agg += '\nSUMMARY: \n\n'
    
    for k1, v1 in aggs.items():
        cost_agg += '{tag}{blend}\n'.format(tag='Tag: '+k1, 
                                            blend='\t Total: $' + str(round(v1['total_blended_cost'], 2)) + '\n')
    
    cost_agg += '~ ' * 20
    
    
    ### Get usage details
    cost_agg += '\n DETAILS: \n'
                                                                                                     
    for k1, v1 in aggs.items():
        cost_agg += '{tag}{blend}\n'.format(tag='Tag: '+k1, 
                                            blend='\t Total: $' + str(round(v1['total_blended_cost'], 2)) + ', ')
        for k2, v2 in v1.items():
            if k2 not in ['total_blended_cost', 'total_unblended_cost']:
                cost_agg += '{resource} '.format(resource = resource_name_map[k2] if resource_name_map.get(k2) else k2)
                kv3 = list(v2.items())
                cost_agg += '{cost1}\n'.format(cost1 = ': $'+str(round(kv3[0][1], 2)))
                    
        cost_agg += ('-'*10 + '\n')
        
    cost_agg += 'Cost with untagged resources: \n' + '~ ' * 10 + '\n'
    for k, v in untagged.items():
        cost_agg += '{id:}'.format(id = 'ResourceID(if any): ' + k + '\n')
        cost_agg += '{blend}\n'.format(blend='Total: $' + str(round(v['total_blended_cost'], 2)) + ', ')
        cost_agg += '----------\n'
    
    return cost_agg
    

### this is the primary method; it catches S3 update event and fires off the aggregation parser   
def lambda_handler(event, context):
    '''
    catches S3 update event, parse cost info and send cost summary to SSN, 
    which will send email notifications
    ---
    arg:    
        1, list event
        2, list context
    return:
        None
    '''
    print('Debug attempt: Delete this and next line')
    print(event)
    # print("Received event: " + json.dumps(event, indent=2))
    # kilroy mod: change the two keys in the following line
    s3 = boto3.client('s3', aws_access_key_id='AKIAJWY2HDSR47EFNU2Q', aws_secret_access_key='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')
    # Get the object from the event and show its content type
    bucket = '879605964811-dlt-utilization'
    
    #key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:
        # list objects
        obj_list = s3.list_objects(Bucket = bucket)
        
        # response2 = s3.get_object(Bucket=bucket, Key = obj_list['Contents'][1]['Key'])
        s3_resource = boto3.resource('s3')
        # s3_resource.Object(bucket, obj_list['Contents'][1]['Key']).download_file('/tmp/'+obj_list['Contents'][1]['Key'])
        files_for_parse = FilePicker(obj_list['Contents'])
        
        print(files_for_parse)

        for f in files_for_parse:
            # print(f)
            # print('\n')
            # print(type(f))
            s3_resource.Object(bucket, f).download_file('/tmp/' + f)
            zip_ref = zipfile.ZipFile('/tmp/'+ f, 'r')
            zip_ref.extractall('/tmp/')
        
        # print(os.listdir('/tmp/'))

        # read and process the most recently updated file
        file_for_daily_agg = files_for_parse[0]

        daily_untagged, daily_aggs, daily_total_blend, daily_total_unblend, daily_total_tagged_blend, \
        daily_total_tagged_unblend, daily_total_untagged_blend, daily_total_untagged_unblend = dailyAgg(file_for_daily_agg.split('.')[0]+'.csv')
        
        # print(aggs)
        # print('---------\n')
        # print(untagged)
        
        cost_agg_str = BeautifulPrint(daily_aggs, daily_untagged, False, daily_total_blend, daily_total_unblend, daily_total_tagged_blend, 
               daily_total_tagged_unblend, daily_total_untagged_blend, daily_total_untagged_unblend)

        if IncludeWeeklySummary():
            weekly_untagged, weekly_aggs, weekly_total_blend, weekly_total_unblend, \
            weekly_total_tagged_blend, weekly_total_tagged_unblend, weekly_total_untagged_blend, \
            weekly_total_untagged_unblend = weeklyAgg(files_for_parse)

            weekly_cost_agg_str = BeautifulPrint(weekly_aggs, weekly_untagged, True, weekly_total_blend, weekly_total_unblend, 
                weekly_total_tagged_blend, weekly_total_tagged_unblend, weekly_total_untagged_blend, weekly_total_untagged_unblend)

            cost_agg_str += ('\n' + '-'*10)
            cost_agg_str += ('\n ~~~ weekly cost summary: ~~~ \n' + weekly_cost_agg_str)

        # kilroy mod: change the access keys in the following line:
        sns = boto3.client('sns', aws_access_key_id='AKIAJWY2HDSR47EFNU2Q', aws_secret_access_key='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')

        # kilroy mod: In the response = sns.publish( there are four things to do:
        #   kilroy mod: TopicArn: Change the account number (notice it is 123456789012)
        #   kilroy mod: TopicArn: Verify the region is correct 
        #   kilroy mod: TopicArn: Provide the correct SNS topic name
        #   kilroy mod: Subject: Choose a subject that fits your account
        response = sns.publish(
            TopicArn='arn:aws:sns:us-east-1:879605964811:kilroy_burn_sns',
            Message=cost_agg_str,
            Subject='Kilroy Burn')

        # kilroy mod: Customize the completion message if you like
        return 'kilroy_burn_lambda completed!'

    except Exception as e:
        print(e)
        print('Err in object {} from bucket {}. Ensure bucket exists in same region as this lambda fn.'.format(key, bucket))
        raise e
```




{% include links.html %}
