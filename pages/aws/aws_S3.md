---
title: AWS S3
keywords: research_computing
last_updated: January 26, 2017
tags: [research_computing, Jupyter]
summary: "Configuring Python in a JupyterHub"
sidebar: mydoc_sidebar
permalink: aws_S3.html
folder: rc
---

## Introduction

This page covers AWS S3 object storage (buckets) and permission management.

## Links

## Warnings

## 


Suppose we want to copy data in a bucket called 'examplebucket' on account X to my account Y. 
Notice that bucket addresses include paths, the analog of folders and sub-folders. Within that 
bucket / folder structure exist objects that are the analog of files. That is what we want an IAM
User on account Y to be able to copy from account X. More specifically we want them to have List
and Read permissions. List will cover the entire bucket, across paths. Read can be granted at
the Path and Object level. This means that the account X manager -- supposing they do not want
account Y User to see other content -- must create a dedicated S3 bucket for the material being
shared with account Y User.


Permission exists in three levels: User, bucket and object. 


- User level (does this User have S3 access?)
- Bucket level (covered by the bucket Policy, given below)
- Object level (covered by the bucket policy, given below)


Procedurally on account X the S3 bucket 'examplebucket' should be created; and for the sake of 
clearing the decks (say on the console) the Policy should be completely deleted so it is a blank 
slate. Upon selecting the bucket this is the Permissions tab and the Bucket Policy sub-tab. 


At this point nobody gets to List or Read (copy) anything. 


Next the account X person goes to the Policy tab and creates and saves the policy given below. Please refer to
[this web page](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-walkthroughs-managing-access-example2.html)
for a more comprehensive walk-through.


The account ID is a 12 digit number; I use 123456789012. 
The Sid key is short for 'Statement ID', an optional identifier that you provide for the policy statement. 
You can assign a Sid value to each statement in a statement array. In services that let you specify an ID element, 
such as SQS and SNS, the Sid value is just a sub-ID of the policy document's ID. In IAM, the Sid value must be 
unique within a JSON policy. We use it here to declare the important point of the policy.


```
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Sid": "Share List and Read on bucket with some other account",
         "Effect": "Allow",
         "Principal": {
            "AWS": "arn:aws:iam::123456789012:root"
         },
         "Action": [
            "s3:GetBucketLocation",
            "s3:ListBucket"
         ],
         "Resource": [
            "arn:aws:s3:::examplebucket"
         ]
      }
   ]
}
```

Now that we have come this far it is time to test this...


{% include links.html %}
