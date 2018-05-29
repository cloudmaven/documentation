---
title: Introduction to the Cloud
keywords: cloud, basics
last_updated: January 26, 2017
tags: [research_computing]
summary: "What the cloud is..."
sidebar: mydoc_sidebar
permalink: cc_what_is_the_cloud.html
folder: cc
---

![cc_intro0001](/documentation/images/cc/cc_intro0001.png)

## Introduction


Some 95% plus of the questions we are asked about cloud computing are answered on this page. Think of this as a 
narrative version of an FAQ; and please scroll down if you don't see the topic you're interested in.


(**This page is undergoing a major revision so pardon the dust**)


## Question: How do I get Research Credits on the public cloud? 


To rephrase the question: 'I hear that both Microsoft and Amazon Web Services (public cloud vendors) provide free 
credits for research projects. Is this the case? How does it work?'


Answer: Yes; in both cases you as a researcher can apply for and in many cases receive an allotment of cloud
credits. The typical amount awarded is on the scale of thousands of dollars -- strictly as credits, not as 
actual money -- and it comes with a conceptual caveat. We (the UW cloud consultants) want you to understand 
the context and the caveat for these grants so you can increase your chances of writing a successful proposal;
and so you know what to expect as you move on from there. 


Three things to know. First is again: Yes 
[Microsoft](http://https://www.microsoft.com/en-us/research/academic-program/microsoft-azure-for-research/)
and 
[AWS](https://aws.amazon.com/research-credits/) 
will both gladly provide research credits in response to 
a short but thoughtful research computing proposal. Please read those respective pages for details on 
their programs.  


Our interpretation of the situation is this -- this is the second thing to be aware of -- that these companies
very much *value* intellectual investment in their public cloud platforms. What they have to gain by giving 
away credits in this manner is a *transition proposition*. They are betting that you the research scientist
will like the cloud so much that you will give up on buying computers and move your research to their cloud. 
We happen to think this is a great idea as well; in many but not necessarily all cases. Further down on this
page we will give you more detailed views on 'is the cloud right for me?'.  


So the idea the cloud vendors have is to get researchers through this cloud phase transition by lowering that 
initial barrier of paying for those initial cloud cycles. Therefore we suggest sending the message in your proposal 
that the proposal is in your view a stage in transition to using the cloud for research computing in the long
term. This is your evaluation period... and as such it is not a source of ongoing funding. In fact -- supposing you 
fall into this category of 'early cloud adopter' -- you might start writing cloud computing into grant 
proposals today to NSF or NIH or NASA or whomever so that when your cloud credit grant runs out you can keep forging 
ahead with your research. 


As we make our way in this new frontier of computing we find that some research teams do not anticipate 
the (typically one year) end of their credit support.  In some cases they apply again; 'Can we get some 
additional funding?' Sometimes this works and sometimes it does not. But of course our point is that it
misses the idea that these grants are transitional; so there, now you know the second thing.


The third item is this: Having a cloud computing account comes with some administrative overhead. It is not 
as intense or time consuming as owning and operating your own hardware. But there are some things to learn 
and understand; and that is what we're here to help you with. That is: We are running a consultancy which 
includes Cloud 101 courses and informal conversations and office hours and so on. So get in touch with us
if you are new to using the cloud; or have questions; or want to share your expertise with us. 




## Question: How much does the cloud cost? 

## Question: Which cloud should I use? 


The purpose of this document -- available [here](http://cloudmaven.org "Cloud Maven technical website") -- is 
to introduce you to the public cloud as a research computing platform: Capable of powerful computation, secure,
cost-effective, and potentially broadening your team's capabilities. 

## Links
* The University of Washington has introductory material 
[here](https://itconnect.uw.edu/research/cloud-computing-for-research/ "Intro to cloud computing for research").
* True Cost of Ownership (TCO) is an important (kilroy: add spreadsheet info) factor and you can explore 
that specifically in the AWS framework [here](https://awstcocalculator.com/).
* If you are interested in using Python to control your AWS computing environment: 
Look into the [boto SDK](http://boto3.readthedocs.io/en/latest/ "Boto 3")
* AWS EC2 instance [descriptions](http://cloudmaven.org "kilroy") 
and [on-demand rates](http://aws.amazon.com/ec2/pricing/on-demand "AWS EC2 on-demand rates")

## Warnings
***The information on this page could start you on an irrevocable course into cloud computing; massively reducing
your waiting time for intensive jobs to complete and enabling you to share your results with your colleagues and
colleagues you have never even met. Proceed at your own risk.***

## Overview
This essay presents cloud computing for research in its essentials, a 'theoretical minimum' that you should know if you 
are interested in doing research computing on the cloud. (Term borrowed from Leonard Susskind.) The cloud is a 
powerful flexible computing environment that can change and particularly streamline how you do computing. We present 
the argument for this here along with caveats and qualifiers. Our goal is to give you a realistic picture of what 
a cloud transition involves.

## The Case for Cloud
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

## The eScience Institute 
The **eScience Institute** is our originating organization at the University of Washington. They can help you with
computing challenges beyond the cloud. For more please [visit](http://escience.washington.edu/)!

## Skills
In order to successfully carry your computing to the cloud you and your team will need to learn a new set of skills. 
You will need to understand account management, security, cost estimation, and computing scale; all in relation to your 
work which we tend to assume depends on data-driven research computing. 
We recommend setting aside time for training (online or in person if possible) and setting aside more time for 
discussions on how to migrate to the cloud. If you and your group see the benefits and are anxious to get going 
the good news is that the cloud learning curve is not too bad; and is even pretty fun.

## Vendors
The public cloud came about as an excess of computing capacity at Amazon.  The company realized they could make 
available and monetize these compute resources; hence was born Amazon Web Services (AWS), the first large-scale 
public cloud. Other cloud vendors include Microsoft Azure and Google. We do not advocate any particular cloud vendor 
over the others. Each has its merits and we try and present some of those here at cloudmaven.org. 

## Cost
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

## Machines
Cloud computers typically run a version of Linux or a version of Windows. Furthermore you can choose from among dozens of 
machine types with varying amounts of memory and computing power. Cloud computers are accessed from (say) your laptop 
using various Client Applications, starting with **ssh** or **PuTTY**. As a rule you would develop your code locally, test 
it, and then deploy it to cloud machines where it runs. 

### Clusters

When you need compute power the cloud is a great resource. Cluster and Schedulers technologies are in place that enable you
to grab hundreds to thousands of machines as needed, run your compute task to completion, and then just as quickly release
those resources back into the general pool. Inter-node connection speed on the cloud is catching up to on-premise compute
cluster solutions via technologies like Infiniband. 

## Development and Testing
The cloud is not necessarily a great place to write code.  Typically we write and test code locally and then test again on the cloud
to verify that everything is working as expected, *before* going to large-scale processing tasks.

## A Success Story
Tim Durham works in genomics at UW and has an analytical pipeline that operates on segments of the human genome; up to 3 billion base 
pairs. He is working to interpolate information linking human cell types to proteins.  Using the "server room at the end of the hall" 
Tim can complete small data subset processing runs in a matter of a week or two; in the process possibly restricting other 
researchers from using those machines. By taking the computing task to the public cloud (AWS and Azure) Tim is able to allocate 
many times more resources at once and finish a computation in a matter of hours. Hence three important cloud computing positives: 
No 'shared resource' restriction, no wait time to start processing, and faster processing for tasks that can be parallelized. 

When Tim completes a processing run he turns off the Linux machines he is using and thereby stops paying for them. This is the 
cloud utility cost model: You pay for what you use. The recovered output data are analyzed and his methods are refined. Once he 
feels that the configuration is optimized he'll do a single large 'scale up' from 1% to the entire human genome. This task -- built 
on Apache Spark -- should run in a day and can be repeated in the future if the algorithm is further refined. 

Tim can -- if he so chooses -- make the results of this analysis publicly available through a cloud-hosted website. He could 
build this out on a Web Framework such as Django and build an API that provides public, programmatic access to the full 
results or to selected subsets. 'Programmatic access' means that other researchers can pull the results of interest into their 
workspace using a computer program rather than using a manual approach.

## Research Software Development
Software repositories such as GitHub are enabling research collaborations to better manage software development. This is 
something of a developing art form (in research) with practices that can be quickly learned and readily implemented; and 
which will make software more robust, secure, and easier to build. It is highly likely that taking any steps to formalize 
software development within a research group will be beneficial, particularly as software typically has a half-life 
of a small number of years. 

In cloud computing software is often written on local computers -- possibly tested there as well -- and then migrated 
to cloud instances where the actual processing of data, modeling, etcetera takes place in earnest. The manner of 
development has a direct impact on security and is commensurately more important. 

## Security
The cloud is extremely secure provided that the research group learns and follows appropriate guidelines. Both AWS and Microsoft have 
HIPAA-aligned technology called out in respective Business Associate Agreements (BAAs). The burden of compliance is placed on the 
research team; and UW IT is working to make this progress feasible and straightforward.

## Alarms
The cloud is elastic -- designed to expand to meet computing challenges -- but this expansion is frequently automated. Since 
automation can do things in error, by accident, it is important to know how to cope with an undesirable growth condition using 
other means, i.e. means outside of the machinery that is causing the growth. This leads to the notion of Alarms. An alarm is 
how the cloud can be configured to catch circumstances in which resources grow out of control. 

## Research Credit
AWS and Microsoft Azure both have programs to grant cloud credits to approved research programs. The one-page application 
typically requires one to three months to process and can secure you in the neighborhood of $20,000 in cloud credits good for one year.

[Amazon cloud research credit page](https://aws.amazon.com/research-credits/)
[Azure cloud research credit page](http://azure4research.com)

The idea of these programs is to remove the cost risk of learning how to use the cloud. We anticipate that in the course
of a successful cloud adoption process you will learn to cost and budget for cloud computing after the grant is expired.

## Support contracts
You may very well want to pay a surcharge for technical support on your cloud account. You can pay for this using your research 
credits. It costs you $100 / month on AWS for "Business Level support" (or ten percent of your monthly budget if that is 
larger). You will 
be connected with skilled cloud professionals who will be able to help you overcome technical obstacles. You can also opt in to
a support contract when you realize you need it.

## Services

'Services' is a pretty general term; but here it means specifically things you 
This section describes a part of the cloud that you may not know about; but can learn: Services that are often dissociated from machines.

### Getting started

Your access to the cloud depends on you having a *cloud account* like an email account. Your account ID gets you
access through a web browser to a cloud console where you allocate and manage resources. Suppose you have both
data and code on your Windows PC. You want to get a powerful machine to run some analysis; here are the steps:

- Log in to your cloud account

- Allocate a Linux machine (for which you will pay an hourly rate, for example 47 cents per hour

- Download the login credentials for that machine

- Use WinSCP to copy your code and data to that rented cloud computer 

- Compile and run your code

- Recover the results using WinSCP 

There are many more details but this example covers the basic framework of getting something done on the cloud. 
To get started you will need an account. There are at least four approaches open to you:

- Cloud novice approach: Get a [$100 free credit account on AWS](https://aws.amazon.com/free/) 
or a [$200 free credit account on Microsoft Azure](https://azure.microsoft.com/en-us/free). 
Both require you to enter credit card info. This is like giving your hotel your credit card in case you break the TV. 

- You need some substantial compute power *Today*: Contact us by email. We may be able to quickly (within a 
few hours) set you up with a temporary User account. You will need to coordinate your usage with us; we will 
need to make sure you are 'good to go' managing resources; and we will ask that you do some reporting 
on your experience. This can be a short-term stop-gap if you're stuck.

- You need some serious compute power for a year at no cost (requires 2 months to set up): Fill out the 
[one-page application here](https://aws.amazon.com/research-credits/) for AWS or 
the [one-page application here](https://www.microsoft.com/en-us/research/academic-program/microsoft-azure-for-research/) 
for Microsoft Azure. On approval you can receive up to $20k in research credits for a year. Both public clouds are 
excellent so we do not recommend one over the other. Come visit our office hours if you would like to disucss relative merits further.

- You need some serious compute power and you have a budget: Contact UW IT to set up a purchase order. This will take a couple of days.

We also wish to emphasize that other public clouds, particularly Google, have fantastic features as well. We are working to 
expand our representation of these other options. 

## Abbreviated Glossary (See our [more complete glossary](cc_glossary.html) as well.)

- Third Party: A company -- not a cloud provider -- that builds or provides something useful (like the PuTTY application for example)
- Stack Overflow: A website building a knowledge base of answers to common questions. Excellent resource.
- YouTube: A website replete with instructional videos related to building solutions on the cloud. Excellent resource.
- AWS: Amazon Web Services, the public cloud provided by Amazon.
- Azure: The public cloud provided by Microsoft.
- S3: Bulk storage service on AWS.
- Blob: Bulk storage service on Azure.
- EC2: A cloud Virtual Machine or cloud VM on AWS.
- IAM: Identity and Access Management; umbrella term for managing your cloud account resources including Users and their permissions.
- EBS: Elastic Block Storage (AWS), a file system mounted on an EC2 instance typically used for data and software.
- RDS: Relational Database Service (AWS), a database that you make use of without having to maintain an underlying cloud VM. 
- AMI: Amazon Machine Image, a stored copy of a cloud VM that can be used to create an actual cloud VM.
- HTC: High Throughput Computing, often indicates compute work that is highly parallel with little requirement for inter-process communication.
- HPC: High Performance Computing, often indicates parallelized compute work that *does* require considerable communication between processes and computers.
- CFD: Computational Fluid Dynamics, a common computational task in research that is very HPC-oriented.
- IOT: Internet of Things, the distribution of embedded devices that typically communicate across a network to a central location which is in turn often implemented on the cloud. 
- Servers: Computers that act as information resources: dispensing and archiving in relation to one or more Clients.
- Clients: Computers that consume information from Servers and/or provide information to Servers. 
- API: Application Program Interface, an automated mechanism for exchanging information between two computers. 

## Final Remarks

- The cloud takes some work to learn.
- Our motto 'Build ~ Test ~ Share' is about the new way of doing research computing; cloud computing is just one element of this shift.
- Don't hesitate to get in touch with us to find out more.


{% include links.html %}
