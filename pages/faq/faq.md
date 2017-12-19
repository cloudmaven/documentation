---
title: Frequently Asked Questions
keywords: cloud, basics
last_updated: December 18, 2017
tags: [research_computing]
summary: "What you need to know about using the public cloud for research"
sidebar: mydoc_sidebar
permalink: faq.html
folder: pages
---

![cc_intro0001](/documentation/images/cc/cc_intro0001.png)


## Introduction


Here we briefly answer common questions about migrating research computing to the cloud.  
We aim to show how the cloud can work for you; and we also try and keep you out of some
common pitfalls. 



## Q: What is the *cloud*?


The public cloud is a massive ensemble of computers, storage, networking and other computing services 
where you to configure, use and pay for the computing power you need. That is, the cloud is a computing
environment that scales in an elastic manner. You can use it for research computing without needing 
to purchase, maintain, upgrade, patch, or recycle computer hardware. The public cloud is secure, reliable 
and cost-effective.  Additional features include...


* You pay for the compute power that you use.

* You do not have to purchase, maintain, update, and re-purchase equipment

* You have access to computing at tremendous scale; from one core to tens of thousands depending on your needs

* You do not have to wait for cloud computing resources to become available

* You can run your computing jobs to completion without interruption

* You can purchase services such as a database without having to install and maintain them

* You can easily build a web presence and use that to share data and information: With collaborators or with the public


## Q: I am accustomed to my computing environment *persisting*... how do I come to terms with the cloud sounding
like my work could evaporate at any moment?


kilroy left off here...


## Q: What is the cloud not good for? 


If you can do all of your research computing on a local machine -- say on your laptop -- then you don't need to
migrate to the cloud.  The rest of this answer presumes that you have larger, possibly growing compute tasks that you
need to perform. 


If you do not feel you can spare the time (a few days, say) to learn cloud technology then the cloud may not be
for you. The cloud feels a little rough around the edges right now like any new technology. Really you want to 
read further only if your computing environment is hindering your progress in research.


If you have an unlimited amount of patience; and you do not need your compute tasks to finish any time soon:
You may not need to invest time learning how to work on the cloud.  


If you purchase a block of computers and run them full blast for something like 60% 70% 80% 90% 100% of the time: 
They may be more cost-effective than the same amount of computing purchased from a public cloud vendor. Down at 50% 
and lower (let's call this your compute duty-cycle) the public cloud will break even or be *more* cost-effective as 
a utility where you pay for what you use.


## Q: How do I get Research Credits on the public cloud? 


Both [Microsoft](http://https://www.microsoft.com/en-us/research/academic-program/microsoft-azure-for-research/) and 
[Amazon Web Services](https://aws.amazon.com/research-credits/) 
-- two of the major public cloud vendors in addition to Google -- 
may choose to provide free credits to research teams after evaluating a short proposal. 


### Q: How much funding is available?


Thousands to tens of thousands of dollars worth of cloud credits.


### Q: What should my proposal emphasize to increase my chances of receiving an award? 


Three things. First you are interested in going 'all in' on cloud computing. 
Second you understand and appreciate the advantages of using the cloud as enumerated thus and such.
Third that you understand and regard an award to be transitional support to help you evaluate the cloud 
platform (i.e. you do not regard a cloud credit grant as an ongoing source of funding). 
This plus a thoughtful summary of your research we find works well.


### Q: Why do these companies give out these grants? 


They want cutting edge researchers such as yourself to invest in their technology. They realize it can be
a big leap to understand and use their cloud platform; so they are essentially providing an incentive to
try it out on a serious (computational) scale.



## Question: How much does the cloud cost? 


- Archival is $50 per Terabyte per year: Some latency time to pull items out of storage
- Object storage runs $300 per Terabyte per year: Instantaneous access to any stored object
- A powerful computer will cost you $0.50 per hour
- Attaching a 1 Terabyte disk volume to that computer will cost you an additional 100.00 per month
- Uploading data to the cloud is free
- Downloading data from the cloud costs $0.10 per Gigabyte



## Question: Which cloud should I use? 


You should use either Amazon Web Services, Google Cloud Platform or Microsoft Azure. 
We support these three with no strong preference because each has its merits. 
And if you find a different cloud you like better then use that. 






## Q: What are some links I should know about to learn more? 


* The University of Washington has introductory material 
[here](https://itconnect.uw.edu/research/cloud-computing-for-research/ "Intro to cloud computing for research").
* Learn about using Python to control a cloud computing environment [here](http://boto3.readthedocs.io/en/latest/ "Boto 3").
* Learn about [available machines (on the AWS Cloud)](http://aws.amazon.com/ec2/pricing/on-demand "AWS EC2 on-demand rates").



## The Case for Cloud

If your computing environment meets your needs then migrating to the cloud could very well be unnecesary. However if
you see room for improvement in your computing then the cloud is worth understanding. Here is a short list of some of the major
advantages of cloud migration.


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


## Q: Can you provide a quick glossary to cover cloud jargon?


- Elastic: A term that generically indicates the cloud's capacity to scale up and scale down as needed
- Stack Overflow: A knowledge base of answers to common questions (useful resource)
- YouTube: Replete with thousands of helpful instructional videos; a resource for learning cloud computing 
- IOT: Internet of Things, a distribution of embedded devices that communicate with one another and with the cloud
- Server: A computer that acts as an information resource in relation to one or more Clients
- Client: A computer that acts as an information consumer in relation to Servers 
- API: Application Program Interface, a means of exchanging information between two computers 
- Azure: The public cloud provided by Microsoft
  - Blob: Bulk or 'object' storage service on Azure
- GCP: Google Cloud Platform, a public cloud provided by Google
- AWS: Amazon Web Services, the public cloud provided by Amazon
  - S3: Bulk storage service on AWS
  - EC2: A cloud Virtual Machine or cloud VM on AWS
  - EBS: Elastic Block Storage (AWS), a file system attached to an AWS EC2 instance 
  - IAM: Identity and Access Management; umbrella term for managing your cloud account resources including Users and their permissions
  - RDS: Relational Database Service (AWS), a database that you make use of without having to maintain an underlying cloud VM
  - AMI: Amazon Machine Image, a stored copy of a cloud VM that can be used to create an actual cloud VM


## Q: Why is your team motto '*Build ~ Test ~ Share*'? 


We feel that research computing needs to advance to keep pace with data volume and complexity. Three ways in particular
of accomplishing this are touched on by the Build Test Share motto:


- Build quickly using new tools like Python's machine learning library SciKitLearn
- Establish confidence in your software by creating a test framework
- Take advantage of data-sharing technologies to increase the value of your work to your colleagues


## Q: How do I get in touch with you? 


Look us up at the [eScience Institute's WRF Data Science Studio](http://escience.washington.edu/wrf-data-science-studio/).


{% include links.html %}
