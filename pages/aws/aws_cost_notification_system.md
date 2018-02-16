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


To cut to the chase: Skip down to the Installation Recipe section below. 


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


Short answer: Pretty accurate; but this solution is still under development. In the table below we 
compare some results that show we are in the ballpark. However until DLT fixes up their reporting rate
we notice some pathologies and report the burn from two days ago to avoid them. 


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


### The *how* of this end result 


Taking the glossary above as read: ... 


In relation to your account: DLT has allocated an S3 bucket with a standardized name in which they record -- as text lines -- 
the hourly cost of virtually all of your account resources. An EC2 instance that has run for one hour at a cost of $0.17 will 
appear as a time-tagged entry in this cost ledger.  This ledger in S3 is the DLT billing record. 


The DLT billing record is updated only twice daily.  One approach is to use this update as a trigger event which 
generates your bill. However we have deprecated this approach in favor of simply using AWS CloudWatch. This is an 
alarm that goes off every day and triggers a Lambda function that tallies up and emails your daily spend. 
Said Lambda function has permission to scan through the DLT billing record (which is comma separated text) to do 
its sums.  It is also doing account breakdown sums based on resource tagging.  Let's digress on this for a moment.


hobie would like to point out, ma'am, that he's not sure we made it clear that the account owner needs to 
turn on the S3 bucket access... but he's not sure how that goes now. perhaps it is quite simple?


#### What is resource tagging and why do I care? 


The costs of untagged resources are tallied and reported in the body of your burn email.  This is based on
the **Owner** tag, a key which should have a value equal to one of your IAM User IDs. By summing by Owner
you can determine cost/burn over any time period for a user or set of users.  Perhaps you are running two 
different research projects using one AWS/DLT account. The tagged sums help you split your total bill; and 
the *untagged* cost will give you a sense of how much you are spending that is untraceable.


#### What is auto-tagging?


hobie would like to suggest a sequence of events for integrating auto-tagging


- Replace this section with a short description of auto-tagging 
- Re-name the AWS 'Cost Tracking' page to 'Auto-tagging resources'
- Rewrite that page to harmonize with this one
- Combine that page with this one and blow that page away



## Installation Recipe: A procedural to set up cost (burn) notification email


### Intro


Steps: 


- Create a role that has assigned to it a single policy (policies grant permissions to take action)
- Create a lambda function that assumes this role and therefore has the policy's permissions
- Configure the lambda function for the account
- Configure a trigger that will invoke the lambda function (the CloudWatch alarm)
- Create an SNS topic and attach email subscribers to that topic


#### Pro Tip
The DLT billing record S3 bucket has a standardized name based on your account ID '123456789012':
**123456789012-dlt-utilization**.  This bucket is in US-East-1 (N.Virginia) so we do all of the 
cost notification building in that region.  Make sure this is the region shown in the AWS console
at the upper right.


We will use an identifier string for this task: '**kilroy_burn**'.  
For example the lambda function will be named kilroy_burn_lambda.
The SNS topic will be kilroy_burn_sns. The role will be kilroy_burn_role.  


The kilroy_burn_lambda service is a Python script with an event handler method. This service is passed
an event that is parsed in code, eventually leading to parsing and analysis of the contents of the S3 bucket
where the billing data is compiled by DLT.



### 0 Enable DLT Logging


Send an email to the AWS account provider 'DLT': Use the email address OpsCenter@dlt.com. 
You should send this from your account manager email alias; so for example if the root user
is kilroy_administrator@kilroy.org you should send it from there. In this email 
simply request that DLT enable cost logging to an S3 bucket and provide your account number. 


Once they confirm you should find an S3 bucket called 123456789012-dlt-utilization in your S3
console. It should have access = Public and it will be located in US East (N. Virginia). 
This bucket will accumulate a time sequence of csv.zip files where each row of each file is a 
billing item. 


If this procedure fails you may need to check the DLT website to locate more 
technical support. 


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
- Add a CloudWatch Events trigger. Cloud watch is a management tool that allows you to create an Event linked to your Lambda.
  - This Event begins with creating a rule in Step 1
    - I chose **schedule**
    - I chose a Fixed rate of 24 Hours
    - I chose to add a target: Specifically a Lambda function: Specifically kilroy_burn_lambda 
    - Then I move forward to Configure details in Step 2
    - I give my rule a Name 'kilroytrigger' and a Description and click the button 'Create rule'
    - The new rule should appear with a little timer icon and it should fire off your lambda every 24 hours
      - kilroy has no idea how to set the actual time of day that this trigger goes off


- A Lambda can also be set to trigger off an S3 access (Get or Put Object)
- You can configure your Lambda to execute off of the default Test; obviously this is useful


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


Needed here: 
A remark on creating a test. (Don't need some other sort of trigger.)


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


#### Lambda Python code


Here is the lambda code circa Jan 2018. Looks for the string 'kilroy mod' to find the six-or-so places where
you will make changes.



```
# last update: Jan 10, 2018
# author: Jin Qu, Amanda Tan Lehr, Rob Fatland
# programming environment: python3.6
#
# Modify this file for use with your own account by searching for the tag 'kilroy mod' (about 7 lines of code)
#
# Background
#   DLT is a company that acts as a distributor for AWS accounts. Assuming you have a DLT version of an AWS
#   account: DLT can be notified that you want your hourly costs written to an S3 bucket. Their process is 
#   to append on a ~daily basis lines of billing data for the past day. These lines are appended to a billing 
#   file that spans one calendar month. This file is in zipped CSV format (CSV means comma-separated-values) 
#   so it must be unzipped before we can read it. Each line of the file is a separate billing item typically
#   covering one hour. So the basic algorithm for this code is something like this: 
#  
#   Identify which files are going to have relevant timestamped billing lines
#   Open those files and read through every line looking for timestamps in a desired range (say 2 days ago)
#     Each cost line in this file will include a resource type (e.g. EC2 instance) and a cost
#     If the cost line includes an identified Owner of the resource: 
#       Add the cost to that owner's total
#     If not: Add the cost to a cumulative 'untagged' sum
#   Once the lines are all scanned and relevant costs are aggregated...
#     Create an email message body with a readable summary of all of this
#     The very first line includes total + tagged + untagged costs
#     Use the Simple Notification Service at AWS to send this email to interested persons
# 
#   Now this all sounds simple enough although as you'll see it requires three hundred plus lines of code.
#   However there are some 'wild west of the public cloud' warnings that go with it, circa 2018... so we 
#   strongly suggest reading the next two paragraphs carefully.
#
#   First and foremost: If you use this code and insert your own access keys and then publish the code
#     to a public location like GitHub you are at risk of losing tens of thousands of dollars. This
#     is because your access keys can be used to spin up other AWS resources en masse; and there are
#     bots out there that scan GitHub for just this mistake. So keep the working code here in this 
#     Lambda function and here only. This has happened many many times. If you accidentally publish 
#     your keys just go disable them and generate new keys; it's quite easy.
#
#   Second and less critical: We have found that DLT has a very irregular cost-reporting schedule; so if
#     you use this code to look at recent billing -- say today or yesterday -- you are very likely to get
#     an incorrect aggregate spend estimate. In fact you should check your results from this code against 
#     the AWS Cost Explorer tool. That will take some effort to sort out; but it will give you an idea of 
#     whether this Lambda is working properly. If it is then you will see your 'recent past' daily burn 
#     in your Inbox every day; which is intended as a quick glance check that your account is not burning 
#     huge amounts of your money. 
#

import json
import os
import boto3
import zipfile
import csv
import datetime
import urllib

# search tag 'kilroy mod': The following diagnostic should reflect your idea of a label for this lambda function
# Look in the Monitoring tab to find the log where this and other print messages appear
print('kilroy cost burn lambda starting')

### choose which file(s) to parse
'''
    Pick up the most recently updated file
    kilroy there is some broken logic here: Which files based on day of month and time-ago range
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
    # kilroy does not like this code returning mixed types
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
            aggs[tag][pname] = {'blended_cost': cost_blend,
                            'unblended_cost': cost_unblend}
            
    else:
        aggs[tag] = {'total_blended_cost': cost_blend,
                     'total_unblended_cost': cost_unblend,
                    pname: {'blended_cost': cost_blend,
                    'unblended_cost': cost_unblend}}




### cost aggregation parser for days-ago-based time range
def dailyAgg(file_path, lo_day_bdry, hi_day_bdry):

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
                # kilroy does not follow the next bit of logic... clearly tied to DLT pathology but unclear if this is effective
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

    total_blend, total_unblend, total_tagged_blend, total_tagged_unblend, \
    total_untagged_blend, total_untagged_unblend = [*all_costs]
    cur_time = datetime.datetime.utcnow()
    
    # dictionary for substituting full name with shorter name
    resource_name_map = {'Amazon Elastic Compute Cloud': 'EC2', 'Amazon Simple Storage Service': 'S3'}
    
    msg = ' '
    msg += 'TOTAL: ${} / ${} / ${} (All/Tagged/Untagged)\n'.format(str(round(total_blend, 2)),\
      str(round(total_tagged_blend, 2)), str(round(total_untagged_blend, 2)))
    # This is commented out because it is no longer an accurate calculation of the time range reflected in what follows
    # msg += 'daily spend from {} to {} \n'.format(datetime.datetime.fromtimestamp(int(datetime.datetime.utcnow().timestamp() \
    #   - 86400.0 * 2)).strftime('%Y-%m-%d %H:%M:%S') + \
    #   ' UTC to ', datetime.datetime.fromtimestamp(int(datetime.datetime.utcnow().timestamp() - \
    #   86400.0)).strftime('%Y-%m-%d %H:%M:%S') + ' UTC ')
    # msg += '~ ' * 20 
    # msg += '\n'
    
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
    # diagnostic commented out: print("Received event: " + json.dumps(event, indent=2))
    # search tag 'kilroy mod': The following line should reflect your aws key ID and secret key. 
    # !!!!!!Do not make these keys publicly visible!!!!!!
    s3 = boto3.client('s3', aws_access_key_id='XXXXXXXXXXXXXXXXXXXX', aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    # search tag 'kilroy mod': The following line should reflect your 12-digit account number
    # this is hard-coded to match your account ID
    bucket = '123456789012-dlt-utilization'

    #some archaeology: bucket = ['Records'][0]['s3']['bucket']['name']
    #                  key = urllib.parse.unquote_plus(['bucket']['key'], encoding='utf-8')
    
    try:
        # s3 is the boto Client and bucket is the S3 bucket ID string so csv_file_list will be 
        #   a list of the CSV cost log files in this bucket. Actually zipped so we unzip below.
        csv_file_list = s3.list_objects(Bucket = bucket)
        
        s3_resource = boto3.resource('s3')
        key = csv_file_list['Contents'][1]['Key']
        
        # files_to_parse will be a list of relevant files to scan through
        files_to_parse = FilePicker(csv_file_list['Contents'])
        
        # Take a look at the logs to see if we chose the right files to parse from!
        print(files_to_parse)

        # unzip all the files we need
        for f in files_to_parse:
            s3_resource.Object(bucket, f).download_file('/tmp/' + f)
            zip_ref = zipfile.ZipFile('/tmp/'+ f, 'r')
            zip_ref.extractall('/tmp/')

        # read and process the most recently updated file
        file_for_daily_agg = files_to_parse[0]

        # set day boundaries for a time range: These are days-ago, i.e. in the past
        #   The code is lo_day_bdry <= time <= hi_day_bdry so to get one day of data
        #   make the boundaries equal
        lo_day_bdry = 2
        hi_day_bdry = 2
        
        # dailyAgg() returns a big tuple of 2 dictionaries and 6 floats (in that order)
        daily_untagged, daily_aggs, daily_total_blend, daily_total_unblend, daily_total_tagged_blend, \
          daily_total_tagged_unblend, daily_total_untagged_blend, daily_total_untagged_unblend = \
          dailyAgg(file_for_daily_agg.split('.')[0]+'.csv', lo_day_bdry, hi_day_bdry)
        
        # Use ComposeMessage() to assemble the body of the email message
        email_body = ComposeMessage(daily_aggs, daily_untagged, daily_total_blend, daily_total_unblend, daily_total_tagged_blend, 
               daily_total_tagged_unblend, daily_total_untagged_blend, daily_total_untagged_unblend)

        # search tag 'kilroy mod': The following line should reflect your aws key ID and secret key. 
        # Do not make these publicly visible!!!!
        sns = boto3.client('sns', aws_access_key_id='XXXXXXXXXXXXXXXXXXXX', aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

        # search tag 'kilroy mod': Three things to check in the following code:
        #   You must have an SNS topic corresponding to your entry in the TopicArn string
        #   Your notification email will have as its subject whatever you place in the Subject string
        #   The return value (also a string) should reflect your idea of labeling this lambda function
        response = sns.publish(
            TopicArn='arn:aws:sns:us-east-1:123456789012:kilroy_burn_sns',
            Message=email_body,
            Subject='kilroy cost burn summary')
        return 'kilroy cost burn calculation completed!'
    
    # Last piece of the event handler: something went wrong  
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e






```



{% include links.html %}
