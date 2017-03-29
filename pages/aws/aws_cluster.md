---
title: AWS Cluster
keywords: aws, cfncluster, procedures
last_updated: January 26, 2017
tags: [AWS, scale, research_computing, containers, research_credits]
summary: "Clusters on AWS"
sidebar: mydoc_sidebar
permalink: aws_cluster.html
folder: aws
---

## Introduction

This page runs through a build of a compute cluster on the AWS public cloud. 

The important vocabulary:

- PIT: Project Identifier Tag, a unique string you designate like 'himat'
- queue: A stack of jobs
- Master: A VM charged with managing a cluster
- Worker: A VM charged with executing sub-processes
- Scheduler: Software that starts sub-processes within a compute task
- qsub: (Linux) submit a job to a processing queue
- qstat: (Linux) get queue status
- qdel: (Linux) delete a job from the queue
- host: List Worker nodes

## Links

## Warnings

- ***Assumed: You have an AWS account - sanitized***

## Let's Go!

- Start an EC2 instance 
  - It will be a 'base of operations' for this project
    - Therefore give it a PIT name like 'himat_config_EC2'
  - Refer to the [EC2 page here](aws_ec2.html)
  - This instance can be small and cheap, for example a **T2.micro**.
  - Give it the Amazon Linux operating system e.g. Amazon Linux AMI
  - Provide it with some default EBS
  - Place it on the cloud101 VPC and on the cloud101_public_subnet
  - Include it in the cloud101_securitygroup 
    - Notice *ssh* is allowed 'from anywhere' (security risk!)
  - Review and launch; and in the process download a new key pair 
    - You can use an existing key pair as well; but you must be sure you have it on hand
    - This will be a '.pem' file extension. 
      - If you are Windows using PuTTY you will need to convert to a .ppk file format
      - This is done using the PuTTYGen application

As an aside: When I set this up I did some background work as well: I created a VPC, placed
inside of that a public subnet, created and attached an Internet Gateway, added an entry in
the Route Table and so forth.



  

{% include links.html %}
