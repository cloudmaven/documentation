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


This is	a walk-through for installing a daily cost notify email from your AWS + DLT account to you. 


What does this mean? 
Magda's Second Law states "Tracking cloud computing spending should require **zero effort**;
otherwise a lapse in vigilence is inevitable." 


Background: DLT is the AWS re-seller at the University of Washington. You want to set up your AWS account 
*through DLT* by first emailing *help@uw.edu* and telling them this. You'll go through a process that will
take a few days; and you will need to pre-designate some funds using BPO or Blanket Purchase Order. This
generally involves coordinating with your business office.  Why? Because it means your F&A overhead is 
waived on your cloud spending. And other reasons.


Once you are up and running on AWS via DLT you can do cost accounting: All of your spending events (say
hourly fees) will appear as rows in a file kept in an S3 bucket. This 


From there you will want an automated script (we write
ours in Python) to run once per day -- a cron job -- to tot up how much you have spent and send this to you 
in an email. The amount spent should be the email Subject so that as you glance through your Inbox every day 
you will exert close to zero effort to notice (hopefully) that your spend yesterday was as expected. If your
spend ever rises in an alarming fashion: You may be able to catch this through careful deployment of AWS alarms.
However in cases where alarms fall short this email notification is a good thing to have in place.


##### Qualifiers 


- This walkthrough uses AWS components (and therefore jargon): Lambda functions, SNS, S3, CloudWatch, IAM Role, IAM Policy. 

- These terms are described briefly below and elsewhere at this website in more detail. 

- On successfully following these steps: You will receive an email each day telling you at a glance what your spend was **two days ago**.  

- We can not provide the spend for *one* day ago because this information is not delivered to the accounting bucket in real time. 
  - This is a how AWS + DLT work at this time.  The past 24 hours spend would be much better but not available at this time.

- For more on best practices please refer to the (UW CSE Database group's helpful page](http://db.cs.washington.edu/etc/aws.html).


![pic0000](/documentation/images/aws/aws_email_summary.png)


Skip down to **Installation** to get started; or read on for more context.


This introductory segment is a brief glossary and a description of what you want to build.
The subsequent section is the step-by-step of building it. 


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
- **Access Keys**: Two strings associated with *IAM Users* for authentication; not to be conflated with AWS 
Key Pairs associated with EC2 instances. 
- **Group**: A set-like construct: IAM Users can be assigned to a Group
- **Role**: An entity that defines an assumable set of permissions to take actions. Roles are molecular.
- **Policy**: A text document that uses a particular (JSON) syntax to permit or restrict actions. Policies are atomic.


### Caveat emptor: How accurate is this method?


In other words: Is the quoted cost equal to the actual cost I will pay at the end of the month?


Short answer: Yes, this is pretty accurate; but the solution is still under development. In the table below we 
compare some results that show we are in the ballpark. As noted until DLT can fix their reporting rate
some pathologies may come in; and we report the cost from two days ago, not yesterday. 


In this table the 'Account' column is the daily spend our software generates for an AWS account provided through DLT. 
The **Cost Explorer** tool is available through the AWS browser console. That is our reference for
what the system thinks we spent for the day.  Values are in US dollars.

<br>


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


<br>


For the first account *our* approach gave $1132.58 for the period whereas the cost explorer gave 1130.36.
And so forth.



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
You will see at a glance how much you are spending to use the cloud. You will also notice any strange spikes
in spending, for example due to unauthorized access.  This is measure of security against accidental cost overruns.


### The *how* of this end result 


Taking the glossary above as read: ... 


In relation to your account: DLT has allocated an S3 bucket with a standardized name in which they record -- as text lines -- 
the hourly cost of virtually all of your account resources. An EC2 instance that has run for one hour at a cost of $0.17 will 
appear as a time-tagged entry in this cost ledger.  This ledger in S3 is the DLT billing record. Here in this document we
take your account number to be 123456789012 and the corresponding S3 bucket will be named 123456789012-dlt-utilization. 
Turning the service on will require sending an email to OpsCenter@dlt.com so plan on this taking a day or so to resolve.
We have further notes on this below. 


The DLT billing record is updated sporadically; and it may take more than 24 hours to post everything.  
The update can be used as a trigger event but we prefer to look at the spend of 2 days ago and to trigger 
that calculation every day at noon using AWS CloudWatch (which behaves like an alarm clock). The alarm
triggers a Lambda function to run; which tallies up and emails your daily spend.  The Lambda function has permission 
to scan through the DLT billing record (comma-separated text).  The cost breakdown is based on resource tagging
using tag keys 'Owner', 'Name' and 'Project'.  These should appear as column headers in all billing files 
in the S3 bucket. 


#### What is resource tagging and why do I care? 


The costs of untagged resources are tallied and reported in the body of your dailycostnotify (spend) email.  
This is based on the **Owner** tag, a key which should have a value equal to one of your IAM User IDs. By summing 
by Owner you can determine spend over any time period for a user or set of users.  Perhaps you are running two 
different research projects using one AWS/DLT account. The tagged sums help you split your total bill; and 
the *untagged* cost will give you a sense of how much you are spending that is untraceable.



#### What is auto-tagging?


This section needs an update per...

- Replace this section with a short description of auto-tagging 
- Re-name the AWS 'Cost Tracking' page to 'Auto-tagging resources'
- Rewrite that page to harmonize with this one
- Combine that page with this one and blow that page away


## Installation 


### Introduction


Steps: 


- Create the S3 bucket in your account and turn on the billing process with DLT
- Create an IAM Role with a couple of Policies: General Lambda permissions and SNS permission
- Create a Lambda function that will assume this Role 
- Configure the Lambda function
- Configure a CloudWatch trigger that will invoke the Lambda function
- Create an SNS topic and attach email subscribers to that topic
- Test your notifier



### 0 Enable DLT Logging


In either US-East-1 or US-WEst-2 (AWS regions) create an S3 bucket based upon your account ID '123456789012'. 
Name it **123456789012-dlt-utilization**. The bucket should not be public.  Once you have established this 
bucket: Attach a policy that you create by pasting in the following text:


```
{
"Version": "2012-10-17",
"Id": "Policy1335892530063",
"Statement": [
{
"Sid": "Stmt1335892526596",
"Effect": "Allow",
"Principal": {
"AWS": "arn:aws:iam::371652583900:user/utilization"
},
"Action": "s3:PutObject",
"Resource":"arn:aws:s3:::123456789012-dlt-utilization/*"   
}
]
}
```

Again be sure to substitute your 12-digit account number for '123456789012'.  What does this policy do? It allows 
DLT to write content to a file in this bucket; which the lambda function will subsequently read.


** Notice you must substitute your 12-digit account number in both the name of the S3 bucket
*and* in the policy text above where it reads '123456789012'.**


Once this bucket is set up send an email from your root email account to OpsCenter@dlt.com. In this email 
request DLT to turn on the utilization logging into your bucket. Give your account number and the S3 bucket name; 
and paste in the text of the Policy you used so they can double check it. Once they get back to you with 
'everything is working' or words to that effect: Go to the S3 part of the console and verify that the bucket 
is still there and that it contains objects, specifically zipped csv log files. These will accumulate daily 
so it may take a day or two for the content to start showing up. If it is not showing up: Contact DLT 
for help.


From here we will configure a role (which will have two policies) and a lambda function (which will assume this role).
The lambda function will refer to the above bucket; so keep the bucket name handy.


### 1 Create a Role for your Lambda function in advance


- Log in to the AWS console with admin privileges
- Go to IAM (Identity and Access Management) and choose (left sidebar) **Roles**
  - Notice these are Global; there is no *region* to consider
- Create a new role of type **Lambda**, proceed to Permissions
- Search for the managed policy **AWSLambdaExecute** and check the box
- Search for the managed policy **SNSFullAccess** and check the box 
  - As you do this the previous **AWSLambdaExecute** policy will not be visible; this is ok, it will remember
- Search for the managed policy **AmazonS3ReadOnlyAccess** and check the box
  - As above the other two policies you have selected will not be visible
- At lower right click the button **Next: Review**. You should (must!) see all three of these policies listed here.
- Name the role and give a description of it
  - An example name: 'dailycostnotify' 
- Create the role


##### Qualifier


An earlier version made use of IAM User Access Keys. We now avoid using them: More secure.


### 2 Lambda


- Go to the Lambda services page and select the **N. Virginia** region at the upper right
- Create a new Lambda function: Choose to author it from scratch
- Give it a name like **dailycostnotify**
- Choose the Python 3.6 runtime
- Choose the role from step 1 above: **dailycostnotify**
- Click the button **Create function** at lower right. This should take you to a 'congrats' message at the top of your new Lambda page
  - Notice there are two tabs available: Configuration and Monitoring
  - Both tabs are important and for now we will stay on the Configuration tab
- Scroll past **Designer** panel and **Function code** panel: You will enter four Environment variable key pairs now
  - Enter a Key string: accountnumber
    - Enter the correct Value string for your account: Your 12-digit AWS account number
    - This will be referenced in the Lambda Python code so that you do not need to hardcode your account number
  - Enter a Key string 'dayintervalStart'
    - Enter a Value string '2'
  - Enter a Key string 'dayintervalEnd'
    - Enter a Value string '2'
    - Start and End = 2 is the most recent day range (24 hours) that tends to work properly *most* of the time
      - You can try other values (remember these are days in the past, relative to today) to see how that works
      - If you run this on the second day of the month with values like 32 and 2 you should see something close to your monthly spend as the total
  - Enter a Key string 'emailsubject'
    - Enter a simple recognizable string as the Value, for example 'AWS daily spend'
- Scroll down further to the Basic settings panel
  - Set the Memory (MB) slider to 256 MB
  - Set the Timeout values to reflect 2 min 10 sec 
- The remaining lower panels can be left as-is
  - Notice that the Execution role panel should list the role you created in step 1
- Scroll back up to the **Function code** panel
  - Delete the lines of code if there is some stuff already in the code window 
  - Paste in the code block given here: 


```
# last update: September 11, 2018
# authors: Jin Qu, Amanda Tan, Rob Fatland
# programming environment: python3.6
#
# Modify this file for use with your own account by searching for the tag 'kilroy mod'
#
# Background
#   DLT is a distributor for AWS accounts. Assuming you have a DLT version of an AWS. DLT can be notified that you want your 
#   hourly costs written to an S3 bucket. This is done by appending lines/items to a billing file that spans one calendar month. 
#   This file is in zipped CSV format (CSV means comma-separated-values) and must be unzipped before reading its contents. Each 
#   line typically covers one hour.
#  
#   This code...
#     identifies files with relevant timestamped billing lines
#     opens those files and reads through every line looking for timestamps in a desired range (24-hour-period 2 days ago)
#         Each line includes a resource type (e.g. EC2 instance) and a cost
#         If the cost line includes an identified Owner of the resource: 
#             Add the cost to that owner's total
#         If not: 
#             Add the cost to a cumulative 'untagged' sum
#     creates an email message body with a readable summary of all of this
#         the first line is total = tagged + untagged costs
#     sense email via AWS Simple Notification Service (SNS)
# 
#   This code has been cleaned up: It does not make use of secret access keys; hence it can be shared as-is publicly. 
#     It does make use of an environment variable to recover the 12-digit account number.
#   
#   Do not set the time interval to the past 24 hours without verifying. In our experience there is some cost reporting latency
#     that will produce inaccurate results. Furthermore after you have allowed this Lambda to run for a few days you should check 
#     the output against the AWS Cost Explorer tool to make sure they are in close agreement (to within a few cents).
#

import json
import os
import boto3
import zipfile
import csv
import datetime
import urllib

print('my AWS cost notify lambda function is starting')

accountnumber = os.environ['accountnumber']
dayintervalStart = os.environ['dayintervalStart']
dayintervalEnd = os.environ['dayintervalEnd']
emailsubject = os.environ['emailsubject']

### choose which file(s) to parse
'''
    Pick up the most recently updated file
    cassandra says there is some broken logic here: Which files based on day of month and time-ago range
    should be fixed to reflect an arbitrary time range
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
    current_d = datetime.datetime.utcnow().today().day
    if current_d <= 6:
        idx1, idx2 = update_dt.index(update_dt[-1]), update_dt.index(update_dt[-2])
        file_picked = [file_list[idx1], file_list[idx2]]
    else:
        idx = update_dt.index(update_dt[-1])
        file_picked = [file_list[idx]]
    return file_picked


# check if the line belongs to <time range>
def dayChecker(line_elements, idx_dt, lo_day_bdry, hi_day_bdry):
    '''
    when parsing through the cost info file, this function checks if a certain line contains info of the most recent 24 hrs
    ---
    arg:    
        array line_elements : a line of a csv file
        int idx_dt : the index of datetime
        int lo_day_bdry: days-ago of time range to consider
        int hi_day_bdry: days-ago of time range to consider, other extreme
    return:
        bool  
    '''
    line_dt = line_elements[idx_dt]
    now_dt = datetime.datetime.utcnow()
    time_elapsed = now_dt - datetime.datetime.strptime(line_dt, '%Y-%m-%d %H:%M:%S')
    if lo_day_bdry <= time_elapsed.days <= hi_day_bdry : return True
    return False

### check if the resource is untagged, if true, print a tag, if not, print False
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
    # cassandra does not like this code returning mixed types
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
        dict aggs : a dictionary like this: op op tag1: op cp cp , op tag2: op cp cp , op tag3: op cp cp cp 
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
        aggs[tag] = { 'total_blended_cost': cost_blend, 'total_unblended_cost': cost_unblend, pname: { 'blended_cost': cost_blend, 'unblended_cost': cost_unblend } }

### cost aggregation parser for days-ago-based time range
def dailyAgg(file_path, lo_day_bdry, hi_day_bdry):
    '''
    parse through the csv file and generate daily cost summary
    ---
    arg:    
        str file_path : path to the cost file
        lo_day_bdry: days-ago time range to consider
        hi_day_bdry: days-ago time range to consider, other limit
    return:
        an array contains daily cost summary
        1, dict untagged : op op 'resource id 1': $$$ cp , 'resource id 2': $$$ cp;
        2, dict aggs : op op tag1: op cp cp , op tag2: op cp cp , op tag3: op cp cp cp ;
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
    #start_date = 0

    with open('/tmp/' + file_path, 'r', newline = '\n') as csvfile:
        lines = csv.reader(csvfile, delimiter=',', quotechar='"')
        for idx, line in enumerate(lines):
            if idx == 0:
                col_dict = {}
                for i, n in enumerate(line):
                    col_dict.update({n.strip(): i})
                # get index for tags (user:Name, user:Project)
                idx_tag1, idx_tag2, idx_tag3, idx_tag4 = col_dict['user:Owner'], col_dict['user:Project'], col_dict['user:ProjectName'], col_dict['user:Name']
                # get index for datetime
                idx_dt = col_dict['UsageEndDate']
                # get index for ProductName
                idx_pname = col_dict['ProductName']
                # 'use quantity' has two types: blended and unblended
                idx_dollar_blend = col_dict['BlendedCost']
                idx_dollar_unblend = col_dict['UnBlendedCost']
                # for untagged resources
                idx_resource = col_dict['ResourceId']
            else:
                # avoid parse the last few lines
                if line[idx_pname]:
                    # day boundaries refer to some interval in the past, as in days-ago
                    # lo_day_bdry and hi_day_bdry were traditionally 0 and 0 to give one day of recent results
                    # make them 3 and 4 to look at a two-day range 3 days ago for example
                    if dayChecker(line, idx_dt, lo_day_bdry, hi_day_bdry):
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

### method composes an email message body 'msg' to be sent to the cost monitoring team
def ComposeMessage(aggs, untagged, *all_costs):
    '''
    give the cost summary generated by func dailyAgg or weeklyAgg, 
    output a reader-friendly string 
    ---
    arg:    
        1, dict aggs : ...
        2, dict untagged : ...
        3, *all_costs : float total_blend, float total_unblend, float total_tagged_blend, 
                        float total_tagged_unblend, float total_untagged_blend, float total_untagged_unblend
    return:
        str cost_summary
    '''
    total_blend, total_unblend, total_tagged_blend, total_tagged_unblend, \
    total_untagged_blend, total_untagged_unblend = [*all_costs]
    cur_time = datetime.datetime.utcnow()
    
    # dictionary for substituting full name with shorter name
    resource_name_map = {'Amazon Elastic Compute Cloud': 'EC2', 'Amazon Simple Storage Service': 'S3'}
    
    msg = ' '
    msg += 'TOTAL: ${} / ${} / ${} (All/Tagged/Untagged)\n'.format(str(round(total_blend, 2)),\
      str(round(total_tagged_blend, 2)), str(round(total_untagged_blend, 2)))
    
    ### Get usage summary Owner tag:Total
    msg += '\nSUMMARY: \n'
    for k1, v1 in aggs.items():
        msg += '{ID}{spend}\n'.format(ID=k1 + ',', spend='\t$' + str(round(v1['total_blended_cost'], 2)))
    msg += '~ ' * 20 + '\n'
    
    ### Get usage details
    msg += '\n DETAILS: \n'
    for k1, v1 in aggs.items():
        msg += '{tag}{blend}\n'.format(tag=k1 + ',', blend='\t $' + str(round(v1['total_blended_cost'], 2)))
        for k2, v2 in v1.items():
            if k2 not in ['total_blended_cost', 'total_unblended_cost']:
                msg += '{resource} '.format(resource = resource_name_map[k2] if resource_name_map.get(k2) else k2)
                kv3 = list(v2.items())
                msg += '{cost1}\n'.format(cost1 = ': $'+str(round(kv3[0][1], 2)))
    msg += '\nCost with untagged resources: \n' + '~ ' * 10 + '\n'
    for k, v in untagged.items():
        msg += '{id:}'.format(id = k + ',')
        msg += '{blend}\n'.format(blend=' $' + str(round(v['total_blended_cost'], 2)))
    return msg

# this method is called by the outside world. The original 'event' was used to fuel the logic but it is better
#   to have no dependency so it is autonomous and easy to test
def lambda_handler(event, context):
    '''
    parse cost info and send cost summary to SNS > email notifications
    ---
    arg:    
        1, list event
        2, list context
    return:
        None
    '''
    
    s3 = boto3.client('s3')
    bucketName = accountnumber + '-dlt-utilization'

    try:
        csv_file_list = s3.list_objects(Bucket = bucketName)
        s3_resource = boto3.resource('s3')
        key = csv_file_list['Contents'][1]['Key']
        
        # files_to_parse will be a list of relevant files to scan through
        files_to_parse = FilePicker(csv_file_list['Contents'])
        
        # Take a look at the logs to see if we chose the right files to parse from!
        print(files_to_parse)

        # unzip all the files we need
        for f in files_to_parse:
            s3_resource.Object(bucketName, f).download_file('/tmp/' + f)
            zip_ref = zipfile.ZipFile('/tmp/'+ f, 'r')
            zip_ref.extractall('/tmp/')

        # read and process the most recently updated file
        file_for_daily_agg = files_to_parse[0]

        # set day boundaries form a time range. These are environment variables dayintervalStart and dayintervalEnd.
        #   If they are equal they define a 24-hour period: days-ago, i.e. in the past. As of July 2018 the DLT updates
        #   to the cost-log files in the S3 bucket have some latency; so going closer than 2 days in the past can produce
        #   very inaccurate (low) estimates of daily spend.
        
        # dailyAgg() returns a big tuple of 2 dictionaries and 6 floats (in that order)
        daily_untagged, daily_aggs, daily_total_blend, daily_total_unblend, daily_total_tagged_blend, \
          daily_total_tagged_unblend, daily_total_untagged_blend, daily_total_untagged_unblend = \
          dailyAgg(file_for_daily_agg.split('.')[0]+'.csv', int(dayintervalStart), int(dayintervalEnd))
        
        # Use ComposeMessage() to assemble the body of the email message
        email_body = ComposeMessage(daily_aggs, daily_untagged, daily_total_blend, daily_total_unblend, daily_total_tagged_blend, 
               daily_total_tagged_unblend, daily_total_untagged_blend, daily_total_untagged_unblend)

        sns = boto3.client('sns')

        #   SNS topic should match what is set up in SNS
        #   Import your account number as the external variable accountnumber
        #   Customize your email Subject using the external variable emailsubject
        #   Customize your return value (string)
        arnString = 'arn:aws:sns:us-east-1:' + accountnumber + ':dailycostnotify'
        response = sns.publish(
            TopicArn=arnString,
            Message=email_body,
            Subject=emailsubject)
        return 'eSci AWS spend notify lambda fn completed'
    
    # Last piece of the event handler: something went wrong  
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucketName))
        raise e
```

- Edit this file to customize it to your own account
  - Search for 'kilroy mod' to find the section at the end that is amenable to customizing
- Note down the arnString value for use in the SNS setup (below)
  - In this case it would be 'arn:aws:sns:us-east-1:123456789012:dailycostnotify'
    - Where again 123456789012 should actually be your 12-digit account number
  - This will be the SNS topic as described below
- SAVE your settings so far: Click the Save button at the top of the web page


### 3 Setting the Lambda triggers: CloudWatch and Lambda Test button


- At the top of the lambda function page are tabs for Configuration and Monitoring as noted
- Staying on the Configuration tab locate the Designer region at the top of the page which includes a block diagram of the lambda function
- Add a CloudWatch Events trigger. CloudWatch is a management tool that allows you to create an Event linked to your Lambda.
  - This Event begins with creating a rule in Step 1
    - Choose **schedule** and use the following string to stipulate 'once per day at noon GMT'...
      - cron(0 12 * * ? *)
      - For more on this see [this link](http://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-experessions.html)
    - Set the target as the Lambda function name: **dailycostnotify** 
    - Move forward to Configure details in Step 2
    - Give this rule a Name 'dailycostnotify'. Add a Description and click the button 'Create rule'
    - The new rule should appear with a timer icon
      - It will trigger your lambda function every 24 hours
      - Missing piece: Setting the actual time of day for this trigger...
  - Note: A lambda function can be set to trigger from S3 access (Get or Put Object)
    - We do not do that here because the DLT logging process has latency built in
  - As a separate task: Configure the Lambda function to execute from the Test button 
    - Go through the default configuration process; you don't have to modify anything
    - Save and click the Test button. It will fail until everything below is also in place 


### 4 SNS


- In the AWS console go to the SNS services page
- Select Create topic
- Enter the topic name per the Python code above: dailycostnotify
- Enter a topic abbreviation, 10 characters
  - Example: dailycost
- Continue to topic details and click Create subscription
  - Choose type = email and add your email address plus any others you think should receive notifications
- Click on Create subscription to send a confirmation email to yourself; and then confirm that 


You should now start receiving a daily spend summary in your Inbox. 
Verify that this works using the Test button on the lambda function page.


### 5 Validation and Debugging


You should be able to Test your lambda function now. If it fails you'll have to debug it. 


#### Cost Explorer


Cost Explorer is a feature of the AWS browser console. You can access this using the top right dropdown menu 
and selecting My Billing Dashboard; then start the Cost Explorer.  In more detail:


- When you receive a billing statement you should compare it with the Cost Explorer estimate of yor daily spend
  - At the upper right of the console use your Account Name dropdown to select My Billing Dashboard
  - Link to the Cost Explorer and launch it
  - Use the Reports dropdown to select **Daily Costs**
  - A calendar drop-down allows you to select a time range (I use MTD); and you must click the **Apply** button
  - You should now see daily expense as a bar chart
    - You can hover over a particular day to get the exact value
    - One DLT accounts the current day cost will look low and tend to be inaccurate
  - This daily cost record should be -- we intend -- commensurate with the email notification you will now receive from lambda


#### The Lambda function monitoring tab


- This tab is very useful is something is not working properly with your lambda function
- The monitoring tab is selected near the top of your lambda service page in the AWS console
- Dashboard charts indicate the lambda has been triggered
- The link to View logs in Cloudwatch is also helpful; diagnostics printed by the lambda show up here
  - Set print statements in the lambda; save the lambda; trigger it using the Test button; diagnose 



{% include links.html %}
