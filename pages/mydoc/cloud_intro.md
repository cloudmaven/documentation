---
title: Introduction to the Cloud
keywords: cloud, basics
last_updated: October 6, 2016
tags: [cloud_core, basics]
summary: "What the cloud is"
sidebar: mydoc_sidebar
permalink: cloud_intro.html
folder: mydoc
---

![pic1](/documentation/images/cloudcore_Alice_hallway.png)

{% include links.html %}

## Introduction
The purpose of this document -- available [here](http://cloudmaven.org "Cloud Maven technical website") -- is 
to introduce you to cloud computing as a research platform. 

## Some useful links
* The University of Washington has introductory material 
[here](https://itconnect.uw.edu/research/cloud-computing-for-research/ "Intro to cloud computing for research").
#* True Cost of Ownership (TCO) is an important (kilroy: add spreadsheet info) factor and you can explore 
that specifically in the AWS framework [here](https://awstcocalculator.com/).
* If you are interested in using Python to control your AWS computing environment: 
Look into the [boto SDK](http://boto3.readthedocs.io/en/latest/ "Boto 3")
* AWS EC2 instance [descriptions](http://cloudmaven.org "kilroy") 
and [on-demand rates](http://aws.amazon.com/ec2/pricing/on-demand "AWS EC2 on-demand rates")

## Warnings
***The information on this page could start you on an irrevocable course into cloud computing; massively reducing
your waiting time for intensive jobs to complete and enabling you to share your results with your colleagues and
colleagues you have never even met. Proceed at your own risk.***

## Cloud-based Research: The Theoretical Minimum Knowledge You Need

### Introduction
This essay presents cloud computing for research in its essentials, a 'theoretical minimum' that you should know if you are interested in doing research computing on the cloud. (Term borrowed from Leonard Susskind.) The cloud is a powerful flexible computing environment that can change and particularly streamline how you do computing. We present the argument for this here along with caveats and qualifiers. Our goal is to give you a realistic picture of what a cloud transition involves.

### The Case for Cloud
If your computing environment meets your needs then migrating to the cloud could very well be unnecesary. However if
you see room for improvement in your computing then the cloud is worth understanding. Here is a short list of some of the major
advantages of cloud migration.
* You pay for the compute power that you use.
* You do not have to purchase, maintain, update, and re-purchase equipment
* You have access to computing at tremendous scale; from one core to tens of thousands depending on your needs
* You do not have to wait for cloud computing resources to become available
* You can run your computing jobs to completion without interruption
* You can purchase services such as a database without having to install and maintain them
* You can easily build a web presence and use that to share data and information: With collaborators or with the public

### The Case for the eScience Institute. 
See [this website](http://escience.washington.edu/)!

### Skills
In order to successfully carry your computing to the cloud -- in addition to the transfer process -- you and your team will need to learn a new set of skills. Some of the terms are general and some are associated with a cloud vendor you might work with. In general terms you will need to understand account management, security, cost estimation, and computing scale; all in relation to your work. You will also benefit from an approach to research software development that keeps your project on track.  So in summary there is some learning and implementation overhead. We recommend setting aside time for training (either online or in person if this is possible) and setting aside more time for group discussions on how to migrate to the cloud. If your research group sees the benefits and are anxious to get going they/you are likely to find that the cloud learning curve is not as onerous as it might first seem; and it is even fun.

### Origins and Vendor Choice
The public cloud came about as an excess of computing capacity at Amazon.  The company realized they could make available and monetize these compute resources; hence was born Amazon Web Services (AWS), the first large-scale public cloud. Other cloud vendors include Microsoft Azure and Google. We do not advocate any particular cloud vendor over the others. Each has its merits and we try and present some of those here at cloudmaven.org. 

### Cost
How much does the cloud cost? The fast answer is "3 cents per GB-month of storage and 3 cents for an hour of CPU time". 
That is an answer we will qualify and expand on; but just to get you started... 

When you purchase a computer you are (apparently) done paying for it and you can use it until it fails; hopefully for 2 or 
more years. Then you need to purchase another computer. This is the traditional computing model and it makes sense if your
machines are adequate to your computing needs provided that someone can pay for the electricity and cooling and someone 
has the time to maintain the operating system; and provided you have a good back-up strategy in case something bad happens. 
Cloud computing costs money but eliminates a lot of these ongoing maintenance tasks. Cloud computing resources are billed 
using a utility model: You pay for what you use. 

Cost is managed by turning off resources when they are not in use; and by carefully managing how many machines are in use
when running jobs. Both of these tasks can be associated with automatic alarms that can prevent cloud usage from getting
out of control and expensive.

See also the section below on cloud research credits, a way to mitigate the cost of learning if the cloud works for you.

### Machines
Cloud computers typically run a version of Linux or a version of Windows. Furthermore you can choose from among dozens of machine types with varying amounts of memory and computing power. Cloud computers are accessed from (say) your laptop using various Client Applications, starting with **ssh** or **PuTTY**. As a rule you would develop your code locally, test it, and then deploy it to cloud machines where it runs. 

### Development and Testing
The cloud is not necessarily a great place to write code.  Typically we write and test code locally and then test again on the cloud
to verify that everything is working as expected, *before* going to large-scale processing tasks.

### A Success Story
Tim Durham works in genomics at UW and has an analytical pipeline that operates on segments of the human genome; up to 3 billion base pairs. He is working to interpolate information linking human cell types to proteins.  Using the "server room at the end of the hall" Tim can complete small data subset processing runs in a matter of a week or two; in the process possibly restricting other researchers from using those machines. By taking the computing task to the public cloud (AWS and Azure) Tim is able to allocate many times more resources at once and finish a computation in a matter of hours. Hence three important cloud computing positives: No 'shared resource' restriction, no wait time to start processing, and faster processing for tasks that can be parallelized. 

When Tim completes a processing run he turns off the Linux machines he is using and thereby stops paying for them. This is the cloud utility cost model: You pay for what you use. The recovered output data are analyzed and his methods are refined. Once he feels that the configuration is optimized he'll do a single large 'scale up' from 1% to the entire human genome. This task -- built on Apache Spark -- should run in a day and can be repeated in the future if the algorithm is further refined. 

Tim can -- if he so chooses -- make the results of this analysis publicly available through a cloud-hosted website. He could build this out on a Web Framework such as Django and build an API that provides public, programmatic access to the full results or to selected subsets. 'Programmatic access' means that other researchers can pull the results of interest into their workspace using a computer program rather than using a manual approach.

### Research Software Development
Software repositories such as GitHub are enabling research collaborations to better manage software development. This is something of a developing art form (in research) with practices that can be quickly learned and readily implemented; and which will make software more robust, secure, and easier to build. It is highly likely that taking any steps to formalize software development within a research group will be beneficial, particularly as software typically has a half-life of a small number of years. 

In cloud computing software is often written on local computers -- possibly tested there as well -- and then migrated to cloud instances where the actual processing of data, modeling, etcetera takes place in earnest. The manner of development has a direct impact on security and is commensurately more important. 

### Security
The cloud is extremely secure provided that the research group learns and follows appropriate guidelines. Both AWS and Microsoft have HIPAA-aligned technology called out in respective Business Associate Agreements (BAAs). The burden of compliance is placed on the research team; and UW IT is working to make this progress feasible and straightforward.

### Alarms
The cloud is elastic -- designed to expand to meet computing challenges -- but this expansion is frequently automated. Since automation can do things in error, by accident, it is important to know how to cope with an undesirable growth condition using other means, i.e. means outside of the machinery that is causing the growth. This leads to the notion of Alarms. An alarm is how the cloud can be configured to catch circumstances in which resources grow out of control. 

### Research Credit

AWS and Microsoft Azure both have programs to grant cloud credits to approved research programs. The one-page application typically requires one to three months to process and can secure you in the neighborhood of $20,000 in cloud credits good for one year.

https://aws.amazon.com/research-credits/ 
http://azure4research.com

The idea of these programs is to remove the cost risk of learning how to use the cloud. We anticipate that in the course
of a successful cloud adoption process you will learn to cost and budget for cloud computing after the grant is expired.

### Support contracts
You may very well want to pay a surcharge for technical support on your cloud account. You can pay for this using your research credits. It costs you $100 / month on AWS for "Business Level support" (or ten percent of your monthly budget if that is larger). You will 
be connected with skilled cloud professionals who will be able to help you overcome technical obstacles. You can also opt in to
a support contract when you realize you need it.

### Services
This section describes the part of the cloud that you don't know about; but can learn: Services that are often dissociated from machines.

### Getting started

Your access to the cloud proceeds based on having a *cloud account* which is like an email account. Your account ID gets you
access (through a web browser) to a cloud console where you allocate and manage resources. For example suppose you have both
some data and some processing code. You can log in to your cloud account, allocate a machine (for which you will pay an hourly
rate, for example 3 cents per hour) and get login credentials for that machine; all from your browser. Once you have those
credentials you can use WinSCP to copy both your code and your data to your rented cloud computer. You can compile your code
and run an analysis on the data; and you can recover the results again using WinSCP back to your laptop. 

Therefore to get started you will need an account. There are four approaches (at least!):

1. Cloud novice approach: Get a [$100 free credit account on AWS](https://aws.amazon.com/free/) or a [$200 free credit account on Microsoft Azure](https://azure.microsoft.com/en-us/free). Both require you to enter credit card info. This is like giving your hotel your credit card in case you break the TV. 

2. You need some substantial compute power *Today*: Contact us by email. We may be able to quickly (within a few hours) set you up with a temporary User account. You will need to coordinate your usage with us; we will need to make sure you are 'good to go' managing resources; and we will ask that you do some reporting on your experience. This can be a short-term stop-gap if you're stuck. 

3. You need some serious compute power for a year at no cost (requires 2 months to set up): Fill out the [one-page application here](https://aws.amazon.com/research-credits/) for AWS or the [one-page application here](https://www.microsoft.com/en-us/research/academic-program/microsoft-azure-for-research/) for Microsoft Azure. On approval you can receive up to $20k in research credits for a year. Both public clouds are excellent so we do not recommend one over the other. Come visit our office hours if you would like to disucss relative merits further.

4. You need some serious compute power and you have a budget: Contact UW IT to set up a purchase order. This will take a couple of days.

We also wish to emphasize that other public clouds, particularly Google, have fantastic features as well. We are working to 
expand our representation of these other options. 

# Divider
From here down is resource material that Kilroy needs to integrate into this page. Also missing is the DSS path to
spending time with solution architects. 

## Geohackweek UW Cloud Intro November 17 2016

This presentation is from the view of a cloud computing advocacy team at UW Research Computing. 
You can reach us at rob at uw dot edu and amandach at uw dot edu.
We present this as Introduction, Framework, Jargon Dive and Closing; then WRYTYNSP with Amanda.

* Your goal is the same as our goal: Focus on the science.
* CC is successful only when it disappears; it is showing every sign of succeeding.
* If you have challenges in your research computing: You may need to make some changes.
	* If you are the Red Queen you may perceive that you do not have time...
	* This talk is intended to give you a Framework for thinking about cloud computing

## Cloud Computing Framework Elements
* Research in the Data Deluge Era = perfunctory + exploratory
	* GDS

* Cloud pillars (sounds dubious) are compute, storage, network, data management and Services
	
* Cloud management pillars are identity, authentication, security, cost, and training

* Cloud practice pillars are Build, Test, Share 

## jargon

* Third Party
* Stack Overflow
* YouTube
* AWS
* Azure
* S3 / Blob
* EC2: Tim and Tychele
* IAM
* EBS
* RDS
* AMI
* Exit Strategy
* HTC
* HPC and CFD and the Law of Moore
* IOT
* Servers and Clients and APIs 

## Final Remarks

* The cloud is work; but "we like what we are used to" so the challenge is really put to the Red Queens
* Our motto 'Build Test Share' is about research computing (props to eScience) where cloud is one of many means to this end
* That said: The Maven can stand up a data API in 20 minutes on Azure. Take it away Maven.


## Cornell Cloud Forum Notes
[Forum website](http://cio.cornell.edu/community/itcornell-community-conferences/cloud-forum-2016 "Cornell Cloud Forum 2016")

* Gerard Shockley from Boston Univeristy; information from the survey
	* Of particular interest were the remarks on Exit and Entrance strategies; and HIPAA

* Second speaker is Sharif Nijim from Notre Dame
	* Very low-key individual

* Panel discussion
	* Bob Winding Notre Dame
	* Gerard Shockly Boston University
	* Laurie Collinsworth Cornell University
	* Ben Rota Harvard University
	* From the "Future State" slide and related discussion
		* CloudFront WAF
		* VPC Mirror port
		* VDI in the cloud
		* Authentication in the cloud
		* IPS/IDS Palo Alto
		* Trying to avoid choke points
		* Can't replicate AWS tools/facilities; so use those first and augment
		* "We're just trying to solve the learning curve problem."

* Lightning Rounds: Introduced by Jim Behm University of Michigan
	* Phil Robinson (Cornell): Student services IT (SSIT) 
	* Jeff Gumpf: AWS workspaces for grad students
		* Kilroy Absolutely have to pursue this with Nancy / STF Pool A plan
			* $80 per student per ? time ?
	* Susan Kelley (Yale): Bringing IT Partners on campus along for the ride
	* Bob Winding: Research data security NIST 800-171 compliance in GovCloud (ITAR information)
	* Brett Haranin: Cloud adoption, a developer's perspective (skipped)
	* Ben Rota (Harvard): Cost engineering in AWS
	* Scotty Logan: Dirty dancing in the cloud
	* Rob Fatland: Research cloud computing garden path success stories
	* Erik Mitchell: Library and NoSQL
		* UCLA and UC Berkeley; 378e6; NoSQL
	* Sara Jeanes: Cloud contracts and procurement
	* Shawn Bower: The meaning of DevOps
	* Dave (Cornell)
		* access control and mutual bursting
			* https://www.cac.cornell.edu/services/cloudservices.aspx
			* https://federatedcloud.org/

* Mark Fischer talk: Automation on AWS
	* Codify infrastructure decisions
	* Document in code and so on
	* Have a process...
	* And here are our three patterns for solving problems
		* cloud formation template: How to create (and destroy) resources
			* JSON, stack... fire it off with CLI or API or console
			* Create Stack is the button you want to get to in the console
			* Delete Stack is another nice thing... "did I really delete everything I needed to?" > Yes!
			* Configuration as code: Version control! 
		* docker: For environment configuration (to avoid go install all of these packages)
		* Jenkins: DevOps gap-filling glue. "Continuous integration (CI) tool"
			* check out a git repo
			* build a Java app
			* integrate with slack / email / ... 
			* Kilroy worth a look I think: We should understand what all Jenkins can do... "warr files"?
				* Could this be Brian Warr? Probably not.

* Sharif Nijim on moving a Windows-oriented DMS to AWS

* Panel on ERPs in the Cloud: Enterprise Resource Planning (Workday and the like)
	* Jim Behm, University of Michigan
	* David McCartney, Ohio State
	* Glenn Blackler, University of California, Santa Cruze
	* Erik Lundberg, University of Washington

* Stanford talk on security standards and related
	* Bruce Vincent
	* Scotty Logan
		* As last year: We should steal (kilroy) everything this guy does
	* Xueshan Feng 
	* Jim Laney, Rupert Burke (kilroy) at UW IT might be interested in these links
	* https://minsec.stanford.edu/ Stanford's prescriptive system security guidelines
	* http://dataclass.stanford.edu/ is the Stanford classification system

{% include links.html %}
