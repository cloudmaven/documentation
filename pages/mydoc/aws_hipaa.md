---
title: AWS HIPAA
keywords: aws, hipaa, procedures
last_updated: January 25, 2017
tags: [AWS]
summary: "A HIPAA-compliant research system on AWS"
sidebar: mydoc_sidebar
permalink: aws_hipaa.html
folder: mydoc
---

## Introduction
The purpose of this document -- available at http://cloudmaven.org -- is to present a procedural and a technical background
for creating and operating a HIPAA-compliant research environment on the AWS public cloud. A corresponding effort is underway
on the Microsoft Azure cloud. 


## Program 

1. Create a diagram showing the EMR > PHI data pool > VM with corresponding IRB, researcher and patient
2. Anticipate <new data to EMR> pipeline
3. Anticipate <IOT to VM> pipeline
4. Anticipate changes to <PHI > VM> process
5. Implement Virtual Private Cloud
6. Synthetic data: Generate
7. Create an IOT signal
8. Create IOT pass-through mechanism
9. Establish software tools including Jupyter on VM
10. Review with IT personnel 
11. Review with management
12. Review with researchers

## Concerns

* Logging: CloudWatch and CloudXXXXX are AWS logging services; and this is frequently parsed using Splunk
* Intrusion detection! Jon Skelton (Berkeley AWS Working Group) reviewed use of Siricata (mentions 'Snort' also) 
* Include an encryption path for importing clinical data 
* Include a full story on access key management
* The IOT import will -- I think -- be a poll action: The secure VM is polling for new data
* This system should include a very explicit writeup of how the human in the loop can break the system
* Acceptable for data on an encrypted drive to moves through an encrypted link to another encrypted drive? To clarify: Must the data be further encrypted at rest first? 
* Filenames may not include PHI. Hence there is an obligation on the MRs to follow this and/or build it into file generation.
* CISO approval hinges on IT, Admin and Research approvals. 

## Terminology and Concepts
* Ansible
* Availability Zone
* Bastion Server (abbreviated **B**)
* CIDR
* Cloudberry
* Dedicated Instance 
* HIPAA [Health Insurance Portability and Accountability Act](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)
* Lambda Service
* NAT Gateway
* Worker

### Conceptual distinction on PHI contact

Herein we identify tools and technologies that do / do not interface directly with Private Health Information:
* Tools that do not come in contact with PHI can be thought of as 'triggers and orchestration'.
* Services that may come in contact with PHI can be described as 'data and compute'

### HIPAA-aligned technologies
Nine AWS Technologies under the AWS BAA that are HIPAA-aligned:
* S3
* EC2
* RDS
* EBS
* DynamoDB
* EMR
* ELB
* Glacier
* Redshift

### Useful Trigger/Orchestration Tools
* Lambda
* Virtual Private Cloud (VPC)

### Encryption
* HIPAA requires data be encrypted at rest, i.e. on a storage device
* HIPAA requires data be encrypted in transit, e.g. moving from one storage device to another

## Aggregated Notes

### Multiple sources of data
* Electronic Medical Records (EMR)
* A Data Warehouse (tables) 
* A Clinician 
* Sensors stream data from patient

### Destinations
* S3 bucket
* EBS/EFS 

{% include links.html %}
