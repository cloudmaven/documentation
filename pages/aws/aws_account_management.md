---
title: AWS Account Management
keywords: aws
last_updated: January 26, 2017
tags: [AWS, cloud_basics, console, api, account_management]
summary: "AWS account management"
sidebar: mydoc_sidebar
permalink: aws_account_management.html
folder: aws
---


## Introduction


This page describes core AWS account management tasks in brief and then again in further detail. We assume that either
you are operating a research-credit based account provided directly from AWS or you are using a paid account established 
through the DLT third party provider. We make this and other distinctions as we go. 

For UW Researchers: It is also possible for you to create an account directly with AWS but we recommend looking into
DLT-based accounts first as they provide some particular benefits such as egress waiver to 15% of your monthly bill.


## Links
- [AWS](http://aws.amazon.com)
- [DLT portal for new AWS accounts](https://customerportal.dlt.com/internet2/)
- [Rotating access keys: Documentation](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html?icmpid=docs_iam_console#Using_RotateAccessKey)
- [Confederate a UW NetID with AWS (wiki)](https://wiki.cac.washington.edu/pages/viewpage.action?pageId=78712235)
- Smart phone: [Activating MFA](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html) and [De-activating MFA](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_disable.html)


## Warnings


- ***Do not start using a new AWS account until you have trained up on how to keep the account secure.***


## So you want to open a paid AWS account


We assume you are at the University of Washington or are a covered *affiliate* of the University. 


- Establish a Blanket Purchase Order
- Email the UW help desk help at uw dot edu with the subject AWS Account. Ask for instructions on how to proceed. 


## Account set-up


- Set up your account to have "all green checkmarks". This means you are logged out and back in as an **admin**.
  - After a year or so you may be encouraged to 'rotate your access keys'; see the link provided above
  - One of those checkmarks is enabling MFA or Multi-Factor Authentication. Do this.
    - It is a little bit of a pain but it gets you another measure of security for your cloud account
    - Your MFA device is probably a smart phone. Here are the links for procedures to...
      - [Activate](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html) 
      - [De-activate](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_disable.html)
- Start and Stop an EC2 instance: Know what it costs, what EBS is, and log in to it before you Stop it.
- Study up on cloud tech, enough to understand cost, security and capacity; and then make a plan. 


## Cost tracking via tags


On AWS you can allocate assets such as S3 storage buckets and EC2 compute instances. These in turn cost money
(either actual money or credits if you have them available) and you probably care about how much. To this end
you can tag each asset with any one of a number of supported keys. A tag is a key-value pair such as

```
Name: Kilroy
Discipline: Genome Sciences
Religion: Pastafarian
```

After a month of using your AWS account suppose you want to see how much your resources are costing you sorted
by discipline. First go back in time and tag everything; then use the AWS Console to sort by your values. 

DLT will sort values for the following keys. Notice they are business-oriented and that there are ten
generic 'CA' keys that you can make mean anything you like. You could for example decide to use CA003 
to record room temperature when you create the tag; and you could later sort on those temperatures. 
So again: You can tag with *any* key string you like but DLT will be able to sort on the following:

```
Application
CA001
CA002
CA003
CA004
CA005
CA006
CA007
CA008
CA009
CA010
Company
Contract
CostCode
CreationDate
Creator
Department
DeptCode
Environment
Grant
Location
Name
Order
Organization
OU
Owner
Payer
Product
Project
ProjectName
ProjectNumber
ProjectType
ResponsibleParty
Role
Service
Status
Use
```

For the HPC Club account we will be using the Project key to tag resources. Each student researcher will have
an assigned project string, let's call that <xyz>. It will be typically the student's name or something easily 
recognizable like that.  The asset should be tagged Project: <xyz> and when it is possible to name the 
asset or service it should be named <xyz>-etcetera. 


{% include links.html %}
