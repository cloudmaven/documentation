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


A: This answer is the tip of the iceberg: 'How you log in to a computer on the cloud and run programs.'
See ensuing remarks for a quick terminology overview. First you would get a cloud account from some provider;
we work with Microsoft Azure, Amazon Web Services and Google Cloud Platform. Log in through a browser to their
**Console** and **start an instance**. This is equivalent to renting a computer by the hour. This computer
will have an ip address; and you can log on to *that* machine for example using **ssh** or **PuTTY** (a 
terminal window).  Once there you can start building your computing enviornment, importing data, compiling and 
running programs, and so on; as you would on a desktop machine. In other words: Get back to your research.  
This snapshot of 'moving your work to the cloud' does not yet get to the *why*, which we address below. 
There is much more to the story so to get a sense of this we suggest looking at the case studies provided here.


Q: Why do I want to move to the cloud? 


A: Reduced risk, reduced hassle, lower cost, and massive on-demand compute power should you need it. 
(If you need additional reasons keep reading.) Let's cover these points in slightly more detail.  Traditionally 
you must purchase and maintain computers and then worry about disks crashing. In the cloud someone else has set
up the computers already; and the cloud provider is constantly creating backups of your disk partitions. Cloud 
operating systems are maintained and updated and patched by the cloud provider (although you can also do security 
patches as needed).  In short you never buy and/or maintain hardware and you won't worry about losing your work / data. 
Migrating to more powerful machines is trivially easy so your hardware does not gradually become obsolete. 
You *do* have to learn and implement cost management and security practices; so there is a learning curve. 
When you are not working on cloud machines you turn them off. Your work environment as preserved at negligible
cost (10 cents per GB per month). You do not pay for computing horsepower when you are not using it.  
And should you need massive computing power the cloud has thousands of machines available. You can scale 
your compute task out and complete your processing quickly. 


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
Gigabyte per month on AWS; other vendors such as Microsoft Azure and Google are comparable.


Q: How much does cloud storage cost? 


A: Rapid-access storage costs $0.023 (2.3 cents) per Gigabyte-month on the AWS cloud. Other vendor 
costs are comparable. Low-access storage is cheaper, as low as 25% the cost of rapid-access storage. 


Q: How is cloud storage different from disk space on the cloud? 


A: Storage is distinct from and cheaper than disk space by a factor of four. Content that you do not need 
to access repeatedly frequently is cheaper to place in storage. 


Q: Is there an overview of costs? 


A: For AWS [this diagram](https://luckylittle.gitbooks.io/the-open-guide-to-amazon-web-services/content/figures/aws-data-transfer-costs.png) 
might help but it may also get out-of-date. 


{% include links.html %}
