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


Q: How does the cloud work? 


A: See the ensuing questions to get a quick overview of the terminology. Taking that as read the first step
is to get a cloud account and log in to the provider's website (console) using a web browser. Here you will 
find many options including **start an instance**. This you can do immediately: It is equivalent to renting 
a computer by the hour. Once you have started the instance -- which we also call a cloud computer or a cloud
virtual machine -- you can log in to that machine and start building a computing enviornment. You can allocate 
associated disk space, upload files, install software and quickly get back to your research.  This is the 
simplest picture of moving your work to the cloud. There is much more to the story, however. To get a sense of 
this vast 'what else?' we suggest looking into the case studies provided at this website. 


Q: Why do I want to move to the cloud? 


A: One way to answer this is to say 'Using the cloud drastically reduces your risk and gains you time.'
Traditionally you have to purchase and maintain computers; and worry about them crashing and losing your
work. Cloud providers do a huge amount of back-up work -- invisible to you -- so that 


Q: How fast/powerful is a given cloud computer?  


A: Cloud computers -- also called *instances* or *Virtual Machines* -- exist in many configurations and
power levels. A small low-power machine will cost perhaps $0.01 USD to operate per hour and a pretty 
powerful machine might cost $0.40 per hour. The most powerful machines you can find on the cloud can cost
$15 per hour.  You can read about cost and power at the cloud vendor's website. At UW we focus on three
vendors: AWS, Microsoft Azure and Google Cloud Platform.  From an instance command line you can issue 
commands to learn more:


```
% lscpu
% cat /proc/cpuinf
```


Q: How much does a cloud computer cost? 


A: One penny per hour for a simple, low-power instance. $0.40 for a very powerful machine.


Q: How much does cloud disk space cost? 


A: RAM memory on a cloud instance is part of the cost of that instance. Disk space costs $0.10 per 
Gigabyte per month on AWS and other vendors are comparable.


Q: How much does cloud storage cost? 


A: Rapid-access storage costs $0.025 (2.5 cents) per Gigabyte-month on the AWS cloud. Other vendor 
costs are comparable. Low-access storage is cheaper, as low as 25% the cost of rapid-access storage. 


Q: How is cloud storage different from disk space on the cloud? 


A: Storage is cheaper than disk space by a factor of four; so content that you do not need to access 
repeatedly and rapidly is cheaper to hold in storage. If you are analyzing some data files you might 
copy them from storage to disk space attached to an instance to decrease access time. 



{% include links.html %}
