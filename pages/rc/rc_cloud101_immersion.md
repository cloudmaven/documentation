---
title: Cloud 101 Hands-on Immersion Day
keywords: research, computing
last_updated: January 26, 2017
tags: [research_computing]
summary: "Cloud computing basics hands-on training by UW Research Computing and the UW eScience Institute"
sidebar: mydoc_sidebar
permalink: rc_cloud101_immersion.html
folder: rc
---

**Registration is now closed**

**Date:** Tuesday, Apr. 4, 2017
**Location:** University of Washington Husky Union Building, Room 250. [Parking information](http://depts.washington.edu/thehub/home/directions/)
**Time:** 8.30am to 5pm 


---
 
## Objective
This one-day, hands-on immersion course will introduce participants to  three major cloud providers (Amazon Web Services, Microsoft Azure and Google Cloud Platform) with two focused 'get stuff done' activities. First: Web framework building: Participants will learn to provision compute resources and build a lightweight system to encourage collaboration and data sharing. Second: Scale computing: Participants will be introduced to configuring and running tasks on the high performance computing (HPC) service on AWS. In this process participants will also learn to compare costs between different cloud providers and on-site computing infrastructure.  

---

## Pre-requisites 
 
- Know the basics of Linux 
- Get temporary "education" accounts on AWS, Azure and Google Cloud Platform 
- https://aws.amazon.com/education/awseducate/ 
- https://azure.microsoft.com/en-us/community/education/ 
- https://cloud.google.com/
- Install [PyCharm](https://www.jetbrains.com/pycharm/), a Python IDE (free Professional version for UW students/faculty, or use the free community version)

---
- Desirable: Attend Software Carpentry at UW eScience, March 27th-28th, 2017 to learn Linux, Git and Python.  
- Desirable: Install a version of Visual Studio 
 
** Please let us know ahead of time if you have exhausted your free education credits so we can get more for you! We will not be providing these credits on the day of the workshop. **

## Course Outline 
* Welcome and logistics, breakfast provided (8.30am -- 9am)
* Introduction to cloud computing (9am -- 9.45am) 
  - What is the cloud? Why use it?  
  - Choosing a cloud provider: Available services, ease of migration, cost, pervasiveness in your field, etc 

* Introduction to the 3 primary cloud providers: AWS, Azure & GCP (9.45am -- 12.15pm; 15 minute break at 10.30am) 
  - Introduction to the consoles 
  - Build a virtual machine on all three platforms; compare costs 
  - View available compute options 
  - Learn costing of core elements and extras including services 

* Basics of cloud storage and how to get data in and out of your virtual machine 
  - To include the AWS and Azure CLI and the GCP SDK/Cloud Shell 
  - Cloud storage, ingress and egress costing 

* Lunch provided (signing up: Please indicate any dietary restrictions) 

* Build a web framework for collaborative data sharing (1.15pm -- 2:45pm + coffee break) 
  - Overview: Wiring up a Django web framework to a data resource 
  - Deploy a Django instance on AWS Elastic Beanstalk 
  - Deploy a Django web framework on Azure using Visual Studio (Can be demo only; Visual studio not required) 
  - Build a simple API that will display results hosted on a virtual machine to the website you just created  

* AWS CFN cluster (3.15pm -- 4.30pm) 
  - Introduction to the AWS spot market 
  - Provisioning virtual machines for cfncluster; Master - Worker model 

* Take-aways and wrap-up (4.30-4.45pm) 
* Q&A until 5pm as necessary

{% include links.html %}
