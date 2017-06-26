---
title: Costing cloud in proposals
keywords: aws
last_updated: January 26, 2017
tags: [research_computing, account_management, cost]
summary: "Costing the cloud in proposals"
sidebar: mydoc_sidebar
permalink: p_costing.html
folder: p
---

## Introduction


The purpose of this page is to provide guidelines for proposals that incorporate cloud computing, specifically 
towards helping you (the proposal author) estimate costs for your project. 

## Links

- [AWS Grants](https://aws.amazon.com/grants/)
- [Azure Research Credits](https://www.microsoft.com/en-us/research/academic-program/microsoft-azure-for-research/)
- [AWS monthly cost calculator](http://calculator.s3.amazonaws.com/calc5.html)


## Warnings

- ***Research credits should be thought of us stopgap support, not as research support***
  - By research support we mean: A long-term research computing subsidy
  - By stopgap we mean the researcher uses cloud research credits to...
    - ...evaluate the feasibility of the public cloud 
    - ...tide over until standard research budgets can cover cloud costs
  - Research credit awards typically last 12 months; grants are scaled to a cost estimate


## Overview


- Review your status and options with regard to cloud research credit grants. 
- Verify with the funding agency that cloud computing will be a welcome component of your proposal.
- Remember that the authors of this website have office hours and are happy to consult with you.
- Create a cost plan per year
  - Estimate the compute power per machine and number of VMs you will want to secure
  - Estimate the cost of associated memory
  - Estimate the cost of separate storage
  - Estimate your egress cost (cost of retrieving data from the cloud)
  - Estimate the cost of other services you intend to use
- As necessary: Provide justification of your choice of cloud
  - You can compare to alternative cloud providers
  - You can refer to the advantages of using the cloud over purchasing and maintaining equipment
  - Cite case studies presented here at [cloudmaven.org](http://cloudmaven.org) 
  - Remember that the case for cloud includes strengths: 
    - Computing scale
    - Data security
    - Advanced tools and services
    - Similarity of compute environment to local machines
    - Rapidly growing user base and commensurate open resources from which to build your solutions


## Cloud Research Credits


Generous research credit grants (circa 2017) are commonly provided by cloud vendors, specifically
Microsoft Azure and AWS (and GCP grants may materialize as well). These grants can have a value as high 
as $20,000 and a typical duration of 12 months. They are considered non-renewable after that time. 

Having a research credit grant of this type is independent of writing a grant proposal to a funding 
agency such as NIH or NSF. If a cloud research credit grant is secured by you en route to writing a
proposal to an agency like NSF: You may wish to reference that grant in your proposal as a means 
of defraying computing costs in year one of the proposed effort. 

Research credit cloud accounts are distinct from paid accounts secured under the UW BAA with AWS and Azure. 
Those accounts have legal terms associated with them (see respective overview pages herein: 
[Azure overview](az_overiew) and [AWS overview](aws_overview.html).


## FAQ


Q: How fast/powerful is a given instance?  

A: You can read about instance types on the vendor's cloud console 
and/or information pages. For example AWS EC2 instances are 
written up [here](https://aws.amazon.com/ec2/instance-types/).  
From the Linux command line you can issue commands.


```
% lscpu
% cat /proc/cpuinf
```

{% include links.html %}
