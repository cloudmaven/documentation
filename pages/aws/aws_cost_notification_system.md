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
and note the connectivity of AWS components as you go. To this end we begin with a short glossary.



### Glossary


- **Lambda**: A function (piece of code) that runs automatically on AWS. You configure it but you do not 'set up a VM' on which it runs
- **SNS**: The AWS Simple Notification Service(SNS) which permits you to format and send emails automatically. In our case this action will be triggered by a Lambda function
- **S3**: Object storage on AWS, i.e. the place where *objects* are placed and accessed. An object in the S3 object store is for our purposes analogous to a file in a file system
- **spend**: The amount of money you owe at the end of a period of time (here: one day / one week) due to the resources you have used on AWS
- **tag**: A key-value pair associated with a resource. The number of tags you associate with a resource is unlimited; but the keys must be unique
- **Owner**: A reserved tag key where the value is an IAM User username 
- **IAM**: Identity and Access Management, the sphere of actions in AWS that control user accounts, roles, policies, and groups
- **IAM User**: A user identity assigned to a person that includes a username and authentication (password; possibly multi-factor authentication; public/private keys etcetera)
- **group**: On AWS a set-like construct that IAM Users can be assigned to
- **role**: On AWS a set-like construct that inanimate things like Lambda functions can be assigned
- **policy**: A text document assigned to something that uses a particular (JSON) syntax to define what *is* / *is not* permitted for an assignee. 


### What is the story line here?


Now that we have some reference terminology let's go ahead and describe what we are going to assemble.


#### The situation


You or one of your minions is the *Account Manager* for an **AWS** public cloud account provided via an intermediary company called **DLT**.
Your objectives are two-fold: You want to carry out your research computing tasks on the public cloud using this account; and you want to manage your costs 
and spending rates to minimize how much money you spend. 


#### The desired end result 


In your Inbox every day you and your selected account minders will receive an email summary of yesterday's spend on AWS.
The first piece of data is a bulk cost and this is followed by a cost breakdown by users. You will see at a glance how much you are burning 
and whether you've had an unauthorized access breach.  This is measure of security against accidental cost overruns.


#### The *how* of this end result 


Again if terms are unfamiliar you are referred to the glossary above. 


In relation to your account: DLT has allocated an S3 bucket with a standardized name in which they record -- as text lines -- the hourly cost 
of virtually all of the account resources. An EC2 instance that has run for one hour at a cost of $0.17 will appear as a time-tagged entry 
in this cost ledger.  We refer to this ledger in S3 as the DLT billing record. 


The DLT billing record is updated only twice daily.  This update will be configured by you or your minions to trigger a Lambda function.
The Lambda function has permission to scan through the DLT billing record (comma separated text) to sum the costs of resources based 
split out on the basis of tags. The costs of untagged resources are also calculated. The summary of this costing exercise is then 
produced and distributed to an email distribution list using SNS.    


## Introduction


The Email notification system is designed to send cost summary on a daily basis to subscribed emails. This system is based on AWS Lambda 
serverless computing framework, Simple Notification Service (SNS) and Simple Storage Service (S3). The figure below illustrates the system 
architecture.  


![pic0001](/documentation/images/aws/aws_cost_notification_system_001.png)

DLT has set up a pipeline that keeps billing record in an S3 bucket, named as 509248752274-dlt-utilization in the 
US East(N.Virginia) region. This bucket gets updated on a daily basis. All the billing information is recorded 
in compressed csv format. The daily update will trigger the Lambda service, which is currently called "billing_test_jin" 
in the US East(N.Virginia) region. This service consists of Python scripts that will download and parse the billing 
record from the S3 bucket. The script will also aggregate cost information based on tags and resource type (e.g. 
Elastic Computing Service). For untagged billing, the script will summarize cost by resource ID if the resource ID 
appears in the file. Once the Lambda done with these, the SNS will be triggered. The SNS is currently named 
as "Billing_Notification" in the same region with the S3 bucket and the Lambda. 
The SNS will send Lambda cost summary to subscribed emails.

A detailed walkthrough of this system can be seen from the following.

## More details...

### 1, Billing Information in the S3 bucket

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
