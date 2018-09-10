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


This is	a walk-through of installing a daily burn (cost) email on your AWS + DLT account. 


What does this mean? 
Magda's Second Law states "Keeping track of one's cloud computing spending should require **close to zero effort**;
otherwise the barrier may lead to a lapse in vigilence and undesirable further consequences." 


Now: To deconvolve the Statement of Purpose sentence at the top: 
DLT is the AWS re-seller at the University of Washington. You want to have
your AWS account *through them* for reasons given elsewhere at this website. Once you do you can enable hourly
cost accounting as rows in a file kept in an S3 bucket. From there you will want an automated script (we write
ours in Python) to run once per day -- a cron job -- to tot up how much you have spent and send this to you 
in an email. The amount spent should be the email Subject so that as you glance through your Inbox every day 
you will exert close to zero effort to notice (hopefully) that your spend yesterday was as expected. If your
spend ever rises in an alarming fashion: You may be able to catch this through careful deployment of AWS alarms.
However in cases where alarms fall short this email notification is a good thing to have in place.


##### Qualifiers 


- We use the informal English expression 'burn' to mean 'spend of money'. 'I burnt $7' means 'I spent $7'.

- This walkthrough uses AWS components (and therefore jargon): Lambda functions, SNS, S3, CloudWatch, IAM Role, IAM Policy. 

- These terms are described briefly below and elsewhere at this website in more detail. 

- On successfully following these steps: You will receive an email each day telling you at a glance what your spend was **two days ago**.  

- We can not provide the spend for *one* day ago because this information is not delivered to the accounting bucket in real time. 
  - This is a how AWS + DLT work at this time.  The past 24 hours burn would be much better but not available at this time.

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
one week) due to the resources you have used on AWS, aka **burn**
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
You will see at a glance how much you are burning to use the cloud. You will also notice any strange spikes
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


The costs of untagged resources are tallied and reported in the body of your burn email.  This is based on
the **Owner** tag, a key which should have a value equal to one of your IAM User IDs. By summing by Owner
you can determine cost/burn over any time period for a user or set of users.  Perhaps you are running two 
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
  - An example name: 'daily_burn_notify_lambda_role' 
- Create the role


##### Qualifier


An earlier version made use of IAM User Access Keys. We now avoid using them: More secure.


### 2 Lambda


- Go to the Lambda services page and select the **N. Virginia** region at the upper right
- Create a new Lambda function: Choose to author it from scratch
- Give it a name like **daily_burn_notify_lambda**
- Choose the Python 3.6 runtime
- Choose the role from step 1 above: **daily_burn_notify_lambda_role**
- Click the button **Create function** at lower right. This should take you to a 'congrats' message at the top of your new Lambda page
  - Notice there are two tabs available: Configuration and Monitoring
  - Both tabs are important and for now we will stay on the Configuration tab
- Scroll down past the **Designer** panel and the **Function code** panel to the Environment variables panel
  - Enter a Key value string: accountnumber
  - Enter a Value string: 1234567890 (in other words: Enter your 12-digit account number, not literally 123456789012)
  - This will be referenced in the Lambda Python code so that you do not need to hardcode your account number
- Scroll down further to the Basic settings panel
  - Set the Memory (MB) slider to 256 MB
  - Set the Timeout values to reflect 2 min 10 sec 
- The remaining lower panels can be left as-is
  - Notice that the Execution role panel should list the role you created in step 1
- Scroll back up to the **Function code** panel
  - Delete the three or so lines of code already in the code window
  - Paste in the code block given here: 


```
```

- Edit this file to customize it to your own account
  - Search for 'kilroy mod' to find the section at the end that is amenable to customizing
- Note down the arnString value for use in the SNS setup (below)
  - In this case it would be 'arn:aws:sns:us-east-1:123456789012:burn_notify_sns'
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
    - Set the target as the Lambda function name: **daily_burn_notify_lambda** 
    - Move forward to Configure details in Step 2
    - Give this rule a Name 'daily_burn_notify_trigger'. Add a Description and click the button 'Create rule'
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
- Enter the topic name per the Python code above: burn_notify_sns
- Enter a topic abbreviation, 10 characters
  - Example: burnnotify
- Continue to topic details and click Create subscription
  - Choose type = email and add your email address plus any others you think should receive notifications
- Click on Create subscription to send a confirmation email to yourself; and then confirm that 


You should now start receiving daily cost/burn summaries in your Inbox. 
Verify that this works using the Test button on the lambda function page.


### 5 Validation and Debugging


You should be able to Test your lambda function now. If it fails you'll have to debug it. 


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


#### The Lambda function monitoring tab


- This tab is very useful is something is not working properly with your lambda function
- The monitoring tab is selected near the top of your lambda service page in the AWS console
- Dashboard charts indicate the lambda has been triggered
- The link to View logs in Cloudwatch is also helpful; diagnostics printed by the lambda show up here
  - Set print statements in the lambda; save the lambda; trigger it using the Test button; diagnose 



{% include links.html %}
