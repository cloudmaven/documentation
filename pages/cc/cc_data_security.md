---
title: Data Security on the Cloud
keywords: cloud, introduction
last_updated: October 6, 2016
tags: [research_computing]
summary: "Keeping your data secure on the cloud"
sidebar: mydoc_sidebar
permalink: cc_data_security.html
folder: cc
---

# Data security


## Introduction

The cloud -- and your data therein -- is extremely secure: Provided you and your research group learn and follow security guidelines. 
On this page we describe essential security practices, the primary one being: Learn the ropes and how to avoid common mistakes.
Under the **security** umbrella you may hear terms related to HIPAA compliance. HIPAA is a domain of federal regulation for information
about people. The associated cloud technology can be translated as *extremely secure*.


## CC*IIE Remarks


### Objective and Approach


A research team must operate freely on data that is considered private or protected. 
We conform to the stringent security requirements for HIPAA compliance as generally applicable to very securely 
holding and operating on project data.  This breaks down in down into four sub-topics.


1. Encryption of data at rest and in motion
2. Maintaining a secure virtual machine
3. Logging access to the environment
4. Research team education and practice


### Solution


We build on the AWS technology stack: 


- S3 bucket storage must require encryption on ingress. 
- A Virtual Private Cloud (VPC) with a private sub-net for sequestered virtual machines
- Configure virtual machines via an NAT gateway to block unwanted external access
- Enabled Cloud Watch / Cloud Front logging and associated access alarms
- Bastion server and key-protected tunneling
- Access management procedures for research group members
- Education: How to protect access keys, how to stop virtual machines to manage cost etcetera


### Results


Our end-result is a template for starting, operating, and shutting down a secure computing environment.



## Encryption 


- Data are encrypted in transit by means of secure socket layers, i.e. using *https* connections directly to S3 buckets.
  - Transport Layer Security (current) and Secure Sockets Layer (predecessor) are both referred to as **SSL** 
  - The [Wikipedia page](https://en.wikipedia.org/wiki/Transport_Layer_Security) provides a good overview
- Similarly data are moved to and from attached EBS volumes using SSL via an S3 endpoint: Data signals are routed entirely within the AWS cloud structure.
- S3 buckets are assigned a policy whereby they do not receive / ingress data unless these data are requested to be encrypted. 
- Similarly EBS attached volumes are required to be encrypted. 

- [AWS Key Management](https://aws.amazon.com/kms/)

## Secure Computing Environment (VMs)


## Logging


## Training and best practices for research team members


## Additional facets of data security


### Access Control


For both AWS and Azure public clouds, Identity and Access Management (IAM) controls access to cloud services and resources. 
The account administrator creates users and groups, assigns permissions and monitors access. 


### Data preservation 

- [AWS Snapshot](http://docs.aws.amazon.com/storagegateway/latest/userguide/WorkingWithSnapshots.html)
- [Azure Information Protection](https://www.microsoft.com/en-us/cloud-platform/azure-information-protection) 



{% include links.html %}
