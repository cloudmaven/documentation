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


## Program for building this page

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



This is a resource PDF [here](/documentation/pdf/Doc42_HIPAA_on_AWS.pdf) 
This is yet to be inlined. 

{% include links.html %}
