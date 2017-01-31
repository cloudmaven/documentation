---
title: AWS EC2
keywords: aws, ec2, instances
last_updated: January 26, 2017
tags: [AWS]
summary: "EC2 instances on AWS"
sidebar: mydoc_sidebar
permalink: aws_ec2.html
folder: aws
---

# EC2 on AWS

## Introduction
The purpose of this page is to go into some detail about the provisioning and use of AWS EC2 (Elastic Cloud Compute) 
virtual servers; which are just computers available for you to use. 

## Links

- [EC2 Instance pricing](https://aws.amazon.com/ec2/pricing/on-demand/)
- [AWS Calculator](http://calculator.s3.amazonaws.com/index.html)
- [Elastic Block Storage](https://aws.amazon.com/ebs/)
- [Elastic File System](https://aws.amazon.com/efs/)
- [AWS training fundamentals](https://aws.amazon.com/training/course-descriptions/bigdata-fundamentals/)

## Warnings
*** There are two really important things to understand before you start using EC2 instances:
1. Never place your access keys in a public repository such as GitHub.
2. Never allocate EC2 resources and leave them running idle. This will cost you money. Learn to shut them down.
***

## Informal introduction

An EC2 (Elastic Cloud Compute) instance is a computer; or you may prefer the term 'virtual server'. It runs the Linux or Windows 
operating system just like a box under your desk might. However: If you need to increase your computing capacity or expand 
your storage: There are many many such EC2 instances available at a moment's notice. 

Please refer to our read our Cloud Core drop-down for more on how cloud computing may be suitable for your project, 

## Details and terminology

Amazon Web Services (AWS) EC2 instances come with a host of features and terminlogy. Briefly: 

- AMIs
- Elastic Block Storage (EBS) 
- Snapshots of EBS volumes
- EC2 Resources
- Elastic File System (EFS)
- Elastic IPs 
- Access keys and 'Key Pairs'
- S3 storage and access
 
## Setting up an EC2 Instance

The 'compute' part of the cloud begins with Virtual Machines that are called Elastic Cloud Compute = ECC = EC2 ***instances***. 
To get started with EC2 instances you would log on to the AWS console, click on the EC2 icon and follow the buttons to create a 
new instance; which takes a few minutes. And then you can log in to that machine and use it like any other computer. It has an 
operating system that you choose, it has some amount of computing power that you choose, it has some amount of RAM that you 
choose and it has very little disk space. 

This is the big Aha: You also want to attach some disk space in the process as well. The generic term for disk space is a disk volume. You can 
attach these volumes (more than one is fine) in the spin-up process or you can attach them later. This is Elastic Block Storage (EBS). A single 
EBS volume can be up to 16 Terabytes. 

Let's assume EBS is where you'll keep your data; and so to safely make a back-up copy of that EBS volume you can periodically take snapshots of it. 
The snapshots bundle up all the stuff in the volume and put that (like a big zip file) in S3 storage. That storage is completely separate from the 
EC2 instance and its attached EBS volumes. You can also bundle up an image of the entire EC2 instance into storage. This is a snapshot combined 
with some additional instructions on setting up the instance; and together these comprise an AMI for Amazon Machine Image. So there are two levels 
of granularity in backing up your work: Snapshots and AMIs. 

Now how much does this cost? The EBS costs ten cents per GB-month. Storage costs three cents per GB-month; so if you have a lot of data this is 
considerable cost savings, putting your EC2 instance in storage by means of an AMI; or putting your disk volume in storage by means 
of a snapshot. The EC2 instance itself (not considering the cost of the EBS) will vary with which machine you chose. A cheap machine is free 
(T2.micro). A basic, simple low-power machine will cost three cents per hour. A fairly powerful machine will cost perhaps 40 cents per 
hour. You can also rent super-powerful machines for several dollars per hour. Since that adds up it is important to know that you can turn these 
machines off (without losing your data) so that you are not paying for them when you are not using them. 

### What this page is / isn't
Now this document is in preparation; so it does not cover everything in this topic. For example it does not cover how to 
save money by using the Spot Market and it does not cover turning EC2 instances on and off and setting Alarms to inform you 
when they are possibly doing something expensive. We'll build all of this into these documentation pages; but the main point 
of this page at the moment is Resources: The short list of items that you tend to build and associate with EC2 instances. 
This includes AMIs, Snapshots, Key Pairs, and Elastic IPs. 

## Making an AMI
An EC2 instance: We take as a given. (Although we don't have down "Encrypted" but let's just flag that with kilroy. Notice I 
can create an AMI quite easily using the menu. Here is the configuration page: 

![ec20001](/documentation/images/aws/aws_ec20001.png)


part 1 end


## Resource Overview

Returning to the EC2 Resource summary: Let's take a look at what's what here term by term: 
![ec20002](/documentation/images/aws/aws_ec20002.png)

In this region I'm not (apparently) running any instances. 

### Elastic IP 

An Elastic IP is a convenient persistent ip address associated with my account (and with a particular machine unless that machine gets blown away). 
It is said to be 'publicly routable': It is visible/findable on the internet. 

AWS will hand us some number of these on demand for very little money. If we do not request this, however, then the default is a temporary public ip 
address that is only good as long as the instance is up and running. Shut it down and that ip evaporates. 

An Elastic IP is persistent on my account and could even be detached and re-attached to something else. This is like having a 
piece of public plumbing at my dispoal to a resource that I want to share for example.  This ip stuff is distinct from a DNS 
entry. The latter is a person-friendly string associated with an ip address (free or maybe for a nominal fee). 

### Dedicated Host
A Dedicated Host is a physical computer which permits only me (my AWS account) to be connected. It does not thread in other virtual operating systems or 
other accounts.  This is an important concept in HIPAA compliance.

### Snapshot

A Snapshot is always drawn from, i.e. is an image of some Elastic Block Storage (EBS). An 8GB Snapshot is quite likely the root 
volume of an AWS Linux EC2 instance. However if you attach more EBS -- like say 2TB -- to that instance you can make a separate larger Snapshot. 

### AMI 

An AMI is a Snapshot together with some instructions for standing up an EC2 instance. Hence: When you create an AMI part of that process is a Snapshot 
or Snapshots of all the EBS volumes associated with that instance.

### Snapshot to AMI Conversion in Linux

You can "upgrade" a Snapshot to an AMI in Linux but it is more complicated for Windows. And this is a little bit vague: Do 
we mean that the snapshot is of the Root volume or an attached volume? The rebuilt AMI -- in the case where the original AMI 
instructions are unavailable -- will be built out rather generically. This is one of these digressions that can drive one 
crazy so let's leave it there for now.

part 2 end




{% include links.html %}
