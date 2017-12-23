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


Brief answers to common questions on migrating research computing to the cloud:
What's possible, what are the pitfalls.  



## Q: What is the *cloud*?


The cloud is a massive, secure, reliable ensemble of computers, storage, networking and computing 
services available for public use on a utility payment basis. The cloud is a hence a computing 
environment that scales with demand in an elastic manner.


* You pay for the compute power that you need / use

* You do not purchase, maintain, update, patch, service and/or recycle computer hardware 

* You access computing at unlimited scale; from one core to tens of thousands depending on your needs

* You do not have to wait for cloud resources to become available

* You run your computing jobs to completion without interruption

* You purchase services such as databases without needing to install and maintain them

* You can easily build a web presence and use that to share data with collaborators or with the public


## Q: As I am accustomed to my computing environment *persisting*... how do I think about the cloud?  
### (It seems that my work could *evaporate* at any moment!!!)


Cloud platforms are designed and operated as multiply-redundant persistent resources.  


This is rather novel and important and is therefore worth repeating so allow us to phrase it another way: 
The traditional *on premise* computing environment persists as a physical object but eventually it wears out 
and fails. Say it has a lifespan of some 4 or 5 years.  On the cloud a computing environment is created and 
maintained with multiple redundancy in perpetuity.  There are no dedicated computers and therefore nothing breaks 
fails (or evaporates).  Under this model the effort on your part shifts to cost management; paying for these 
resources under the utility model. 


This approach to computing is fairly novel and involves a shift in thinking. Another aspect that
goes with this and also takes some getting used to is the scale up / scale down model of cloud operation. 
Let's consider these in turn for a moment. 


When executing a computational task on a small cluster of computers you have an idea of how long it will 
take to finish.  Modifying this task to run on a larger cluster might require time and effort; but comes
with the benefit of finishing faster. On the cloud the 'larger cluster' can be enormous; it is instantly
available; and it costs the same per compute task as the small cluster. Why? Because on the cloud ten 
computers running for 100 hours costs the same as 1000 computers running for one hour broadly speaking. 
This is scaling *up*.


When you are developing code you may not need powerful computers. On the cloud you move your work environment 
to a small cheap computer. You can also **Stop** your cloud computer when it is not in use -- say over the 
weekend -- so that you are paying only a few cents to store the digital image of your work environment. 
Everything can be restarted again in a matter of a few minutes as needed. This is scaling *down*.



## Q: What is the cloud good for? 


Reproducible research. Data science. Collaboration. Data sharing. Data security.



## Q: What is the cloud not good for? 


If you can do all of your research computing on a local machine -- say on your laptop -- then perhaps you don't need to
migrate to the cloud.  There is some learning involved; and there are monthly bills; and while you need not pay overhead
on your cloud computing (at UW) you do need to manage your account. So if your computing environment is not an impediment
to progress for the foreseeable future then we suggest "If it ain't broke don't fix it." 


On the other hand: Read further if your computing environment is in some way hindering progress in your research.  


If you do not feel you can spare some time (a few days to get started at the outset) to learn the ins and outs of cloud 
technology then the cloud may not be for you. The cloud can feel a little rough around the edges like many emerging technologies 
will; so you would need to be prepared for that. Without that headspace doing a migration to the cloud will be a painful
and potentially disastrous experience; so beware!


If you are doing very compute-intensive research... for example suppose you purchase a block of computers and run them full 
blast for upwards of 60% of the time for four solid years (and you don't need the results any faster than they come) -- then
operating your own hardware may well be more cost-effective than the same computing power rented on the public cloud. 


At 50% utilization and below that the public cloud will start to break even and other factors will come into consideration;
mostly involving how you and your research group spend their time. Cloud break-even with on premise computers (that you own)
will vary from one group to another; and we can help you with this evaluation. 


Data security does not belong in the category of 'what is the cloud not good for?'. The reason for this is that the 
public cloud is extremely secure in comparison with privately-held resources; again with the caveat that one must learn 
how to manage a secure environment on said cloud. However even in this case we recommend paying attention to what the cloud
makes possible, particularly with respect to data-sharing and collaboration. Entry-level cloud experimentation is 
easy to try out and quite cheap.


## Q: How do I get Research Credits on the public cloud? 


Both [Microsoft](http://https://www.microsoft.com/en-us/research/academic-program/microsoft-azure-for-research/) and 
[Amazon Web Services](https://aws.amazon.com/research-credits/) 
-- two of the major public cloud vendors in addition to Google -- 
may choose to provide free credits to research teams after evaluating a short proposal. 
Google might respond positively to a direct communication which would amount to the same thing but there is no
official program running for transitional cloud research credits for the Google Cloud Platform at this time.


### Q: How much funding is available in these programs?


Thousands to tens of thousands of dollars worth of cloud credits. (No actual dollars, to be clear.)


### Q: What should my proposal emphasize to increase my chances of receiving an award? 


Three things beyond outlining the computational nature of your research. First that you are interested in going 
'all in' on cloud computing.  Second you understand and appreciate the advantages of using the cloud as enumerated thus 
and such. In other words: Indicate that the cloud does stuff you need to do.  Third that you regard an award to be 
transitional support to help you evaluate the cloud platform.  That is: You do not regard a cloud credit grant as 
an ongoing source of funding.  This plus a summary of your research and why it is cool we find works well.


### Q: Why do these companies give out these grants? 


Mindshare. They want cutting edge researchers such as yourself to invest in their technology. They realize it 
can be a big leap to understand and use their cloud platform; so they are essentially providing an incentive to
try it out on a serious (computational) scale.



## Q: How much does the cloud cost? 


- Archival is $50 per Terabyte per year: With a few hours latency to pull items out of storage
- Object storage runs $0.30 per GByte per year; or if you like $300 per Terabyte per year.  This means instantaneous access to any stored object.
- A powerful computer will cost you $0.50 per hour.
- Attaching a 1 Terabyte disk volume to that computer will cost you an additional $100 per month
- Uploading data to the cloud is free
- Downloading data from the cloud costs $0.10 per Gigabyte
- Anything you are not activel using (think system and data drives) can be placed in object storage (explained below) to drastically reduce operating cost.


### Q: Why do I have to pay so much to get my own data back?


The short answer is that data ingest is free and egress is expensive because cloud providers like to
weight the cost in favor of extended tenancy. The fact is they like having your business. But this is 
not really a bad situation for a cloud practitioner.  It comes down to another shift in perspective.
The cloud paradigm raises the question 'Do I *need* to get my data back?' and 'What is *back* anyway?' 



### Q: What if my funding agency requires me to keep my data around for five years? 


We suggest multiplying your expected data volume by the archival rate for five years. Budget that and 
pay it in advance. At the end of that time you can allow the data to evaporate... or you may find it 
has some further value to your community; in which case it is in an ideal location.


## Q: What is meant by **object storage**?


This question is really about cost management on the cloud -- the central idea -- while at the same
time explaining this useful bit of cloud jargon '*object storage*'.


Object storage is a key concept in using the cloud because it is what makes cloud computing cost-effective. 
There is a really [nice description of it on Wikipedia](https://en.wikipedia.org/wiki/Object_storage) that we
recommend reading; but in brief: Suppose your data are represented by a set of luggage. When you place 
those data on a file system the luggage is open and the contents are all readily accessible. You can 
instantly reach into any pocket of any garment or grab the toothbrush or the phone charger.
That's a file system. Object storage in this metaphor is a coat check counter. The whole piece of luggage 
goes in and you can get it back out whenever you like.  But you can't use it interactively the way you can 
with the file system. The object that you check might be a single file or it might be a tar ball of an
entire file system. Object storage does not have any practical restriction on object size.


Now why does this make the cloud cost-effective? Because the cloud also has file systems (aka 'block
storage') available for use; and just like on any computer this is how you store and manage your software 
and data. The block storage is mounted on a cloud computing instance precisely as an attached drive.
This is not an option with object storage. 


When not in use the cloud makes it very easy to bundle digital resources from block storage into object storage 
where the cost to maintain them is significantly less. Object storage is cheap whereas block storage (file systems) 
cost more. In the metaphor it is comparing the cost of a coat check to the cost of a hotel room.  


Here is a specific example to help illustrate the difference in cost.  For one month object storage 
costs 2.4 cents per Gigabyte; and this is based on the literal size of the object being stored. 
In contrast a block storage device, i.e. a file system costs 10 cents per Gigabyte per month; but for 
its designated volume regardless what is on that volume. A 30% full 1 Terabyte drive will cost $100 per 
month on the Amazon cloud (ten cents per Gigabyte). Take a snapshot of that drive and it will occupy 
only 300 GBytes because the volume is only 30% full. This snapshot object will cost only $7.20 per
month in object storage. This idea also applies to special snapshots that capture the state of 
an operating system. These snapshots -- called *machine images* -- can be stored in object storage
when the machine (computer) is not needed. Here a powerful computer might cost $1 per hour whereas
the machine image might require only 8 Gigabytes; so the per month cost goes from $720 to 19 cents.


## Q: Which cloud should I use? 


You should use either Amazon Web Services, Google Cloud Platform or Microsoft Azure. 
We support these three with no strong preference because each has its merits. 
And if you find a different cloud you like better then use that. 



## Q: What are some links I should know about to learn more? 


* The University of Washington has introductory material 
[here](https://itconnect.uw.edu/research/cloud-computing-for-research/ "Intro to cloud computing for research")
* Learn about using Python to control a cloud computing environment [here](http://boto3.readthedocs.io/en/latest/ "Boto 3")
* Learn about [available machines from Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/)
* Learn about [available machines on the Google Cloud Platform](https://cloud.google.com/compute/docs/machine-types)
* Learn about [available machines from Amazon Web Services](http://aws.amazon.com/ec2/pricing/on-demand "AWS EC2 on-demand rates")



## Q: What is the eScience Institute 


The [**eScience Institute**](http://escience.washington.edu/)
is our originating organization at the University of Washington. 
We are here to help you with data science.


## Q: Are cloud computers limited in connection speed or machine power? 


We contend that the cloud does not really lag behind in this regard.  Selecting the Azure cloud for an example: 
The M128s machine (December 2017) has 128 cores and 2 Terabytes of RAM. Azure also features both RDMA and 
Infiniband inter-node communication technologies. 


A strength of the cloud in fact is that it keeps pace with technology. Purchasing today's state-of-the-art 
computer means using that machine until either it fails or you replace it; both time-consuming propositions. 
In contrast every six months or so the cloud features a whole new generation of hardware with more computing power 
per node and faster interconnect technology. Migrating into these new options is straightforward and generally
not time-consuming.


## Q: What are the skills I need to pick up to use the cloud?


You will need to understand account management, security, cost estimation, and computing scale; all in relation to your 
work which we assume depends on data-driven research computing.  We recommend setting aside time for training (online or 
in person if possible) and discussions on how to migrate to the cloud.  The good news is that the cloud learning curve is 
not too bad; and it is even pretty fun.


****************************


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


## Q: How do I *access* the cloud?


- Start a *cloud account*. It will be associated with your email account. 
- Go to the providers cloud access website and log in. 
- Use this website to carry out basic tasks 
- Grab a cloud computer and log in remotely: Use ssh or PuTTY or some other terminal emulator
- Move your code and data to this computer
- Compute


There are more details but this is the basic framework.


## Q: Cloud XYZ has a free entry-level account. Should I try that? 




Sure, we support this idea. You go through a form to set up your account; but this may not be your long-term cloud account.
It is a place to start learning the ropes. Once your account is established you can do a *great deal* of computing on small 
low-cost resources without running up a bill, a great way to get started.  But beware: If the company requests a credit card 
number from you and you accidentally burn through the initial credit allotment (typically $100 or so) you will find your 
card being charged. 



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
