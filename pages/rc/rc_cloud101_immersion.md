---
title: Cloud 101 Hands-on Immersion Day
keywords: research, computing
last_updated: March 16, 2017
tags: [research_computing]
summary: "Cloud computing basics hands-on training by UW Research Computing and the UW eScience Institute"
sidebar: mydoc_sidebar
permalink: rc_cloud101_immersion.html
folder: rc
---

**Date:** Tuesday, Apr. 4, 2017

**Location:** University of Washington Husky Union Building, Room 250. [Parking information](http://depts.washington.edu/thehub/home/directions/)

**Time:** 8.30am to 5pm 


---
 
## Objective
This one-day, hands-on immersion course will introduce participants to  three major cloud providers (Amazon Web Services, Microsoft Azure and Google Cloud Platform) with two focused 'get stuff done' activities. First: Web framework building: Participants will learn to provision compute resources and build a lightweight system to encourage collaboration and data sharing. Second: Scale computing: Participants will be introduced to configuring and running tasks on the high performance computing (HPC) service on AWS. In this process participants will also learn to compare costs between different cloud providers and on-site computing infrastructure.  

---

## Pre-requisites 
 
- Know the basics of Linux 
- Programming basics: Python
- Get temporary "education" accounts on [Google Cloud Platform](https://cloud.google.com/)
- We will be creating accounts for you on AWS and Azure using your UW Net ID
- Install [Miniconda](https://conda.io/miniconda.html), a free Python environment and package install manager. 
- Install [PyCharm](https://www.jetbrains.com/pycharm/), a Python IDE (free Professional version for UW students/faculty, or use the free community version)

---
- Desirable: Attend Software Carpentry at UW eScience, March 27th-28th, 2017 to learn Linux, Git and Python.  
- Desirable: Install a version of Visual Studio 
 
**Please let us know ahead of time if you have exhausted your free education credits so we can get more for you! We will not be providing these credits on the day of the workshop.**

## Course Outline 
* Welcome and logistics, breakfast provided (8.30am -- 9am)
* Introduction to cloud computing (9am -- 9.45am) 
  [Tutorial](https://cloudmaven.github.io/cloud101_intro/)
  - What is the cloud? Why use it?  
  - Choosing a cloud provider: Available services, ease of migration, cost, pervasiveness in your field, etc 

* Introduction to the 3 primary cloud providers: AWS, Azure & GCP (9.45am -- 11.30am; 15 minute break at 10.45am) 
  [Tutorial](https://cloudmaven.github.io/cloud101_cloudproviders/)
  - Introduction to the consoles 
  - Build a virtual machine on all three platforms
  - View available compute options 
  - Basics of getting data in and out of your virtual machine
  - Includes the AWS and Azure CLI and the GCP SDK/Cloud Shell 
  
* Basics of costing (11.30am -- 12.00pm)
  [Tutorial](https://cloudmaven.github.io/cloud101_costing/)
  - Learn costing of core elements and extras including services
  - Cloud storage, ingress and egress costing 

* Web frameworks (12.00pm -- 12.30pm)
  [Tutorial](https://cloudmaven.github.io/cloud101_webframework/)
  - Wiring up a Django web framework to a data resource
  - Work with Leaflet to create a webmap
  
* Lunch provided (12.30pm -- 1.30pm)

* Build a web framework for collaborative data sharing (1.30pm -- 2:45pm + coffee break) 
  [Tutorial](https://cloudmaven.github.io/cloud101_webframework/)
  - Deploy a Django web app on AWS Elastic Beanstalk using PyCharm
  - Deploy a Django web app on Azure using Pycharm and Azure CLI
  - Deploy a Django web app on Google App Engine using the CLI
  - Build a simple API that will display results hosted on a cloud storage device to the website you just created  

* AWS CFN cluster (3.15pm -- 4.30pm)
  [Tutorial](https://cloudmaven.github.io/cloud101_cfncluster/)
  - Introduction to the AWS spot market 
  - Provisioning virtual machines for cfncluster; Master - Worker model 

* Take-aways and wrap-up (4.30-4.45pm) 
* Q&A until 5pm as necessary

{% include links.html %}
