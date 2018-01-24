---
title: Frequently Asked Questions
keywords: cloud, basics
last_updated: December 27, 2017
tags: [research_computing]
summary: "What you need to know about using the public cloud for research"
sidebar: mydoc_sidebar
permalink: faq.html
folder: pages
---

![cc_intro0001](/documentation/images/cc/cc_intro0001.png)


## Introduction


Brief answers to common questions on migrating research computing to the cloud:
What's possible, what are the pitfalls.   If you are interested in using the cloud
for coursework -- particularly JupyterHub technology -- please see our additional
content found in the left sidebar under **Curriculum**.



## Q: What is the *cloud*?


The cloud is a massive, secure, reliable ensemble of computers, storage, networking and computing 
services available for public use on a utility payment basis. The cloud is hence a computing 
environment that scales with demand in an elastic manner. It's fairly new and it gets you out
of the business of dealing with computer hardware; so it can save you time. On the public cloud...


* you pay for the compute power that you need / use

* you do not purchase, maintain, update, patch, service and/or recycle computer hardware 

* you access computing at unlimited scale; from one core to tens of thousands depending on your needs

* you do not have to wait for cloud resources to become available; they always are

* you run your computing jobs to completion without interruption

* you purchase services such as databases without needing to install and maintain them

* you can easily build a web presence and use that to share data with collaborators or with the public


## Q: As I am accustomed to my computing environment *persisting*... how do I think about the cloud?  
### (It sounds like on a cloud my work could *evaporate* at a moment's notice!!!)

<br>


Cloud platforms are designed and operated as multiply-redundant persistent resources.  


This is novel and key; therefore allow us to phrase it another way: 
Traditional *on premise* computing persists as physical objects, say under your desk. Eventually these devices
wear out and fails.  Say your computers have a lifespan of some 4 or 5 years; so you periodically have a
replace/ugrade task to deal with.  On the cloud a computing environment is created and maintained with multiple 
redundancy, in perpetuity.  There are no dedicated computers. Nothing breaks or fails or evaporates.  Under 
this model the effort on your part shifts to cost management; paying for these resources under the utility model. 
The actual bits may migrate (securely) across physical systems in the cloud; but this is done for you.


This approach to computing involves shifts in thinking. Not everyone is ready for that today; so we 
advocate migration to the public cloud for folks who are conceptually ready and for whom it makes fiscal 
sense; and / or to whom there are other big advantages. These include the ability to scale resources; so let's 
describe that briefly. 


When executing a computational task on a single computer or on a cluster you have an idea of how long it 
will take.  Perhaps it takes some time; and perhaps these are shared resources so you have a certain wait
time before they are available to you. Modifying this task to run on a larger cluster means it will finish 
faster. On the cloud a 'large cluster' can be enormous and instantly available; and as a utility it costs 
the same per compute task as the small cluster. That is, on the cloud ten computers running for 
100 hours costs the same as 1000 computers running for one hour broadly speaking.  


Conversely when you are developing code you may not need a large cluster of powerful computers. On the cloud 
you would move your work environment to a small cheap computer. You can also **Stop** your cloud computer 
when it is not in use, say over the weekend. You pay only a few cents to store a digital image of your work 
environment.  Everything can be restarted again in a matter of a few minutes on Monday.



## Q: What is the cloud good for? 


Reproducible research. Data science. Collaboration. Data sharing. Data security.



## Q: What is the cloud not good for? 


If you can do all of your research computing on a local machine -- say on your laptop -- then perhaps you don't need to
migrate to the cloud.  There is some learning involved; and there are monthly bills; and while you need not pay F&A overhead
on your cloud computing (at UW) you do need to manage your account. So if your computing environment is not an impediment
to research progress for the foreseeable future then we suggest 'If it ain't broke don't fix it.' 


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


A final comment on mindset. One line of reasoning goes as follows: 'if I spend $4000 on the cloud -- say running a massive 
compute task -- then that $4000 is spent, gone. *Whereas* if I had spent $4000 on a computer... and run the same job to
completion... then I still have the computer and I can run more jobs on it because it isn't gone!' While this is in a sense
accurate it is also glosses over our main assertion: A careful cost comparison allows you to make an informed choice
on whether the cloud makes sense for you.  Just to begin with: $4000 is equivalent to more than 8 years of compute time 
on a modestly powerful computer (based on spot rates on AWS for an m5.xlarge with 4 vCPUs).  We work with researchers
at UW to make accurate comparisons.


## Q: How do I get Research Credits on the public cloud? 


Before we answer that let's go over a couple things at the outset. First research credits are granted by a
cloud vendor to a research faculty member (or other affiliated person) and these are then applied to the monthly 
cloud bill until they are exhausted or they expire. Second these grants are on the order of hundreds to thousands 
of credit-dollars.  They are intended to help you try out the cloud without an initial cash outlay; so it mitigates your 
risk. Thirdly in our experience the real barrier to getting on the cloud is not funding.  It is the time required 
to learn how to use the cloud. This is what we are here to help you with: Is the cloud the right place to go? 
What's involved in getting there? How do you manage your account, keep your data secure, and get back to focusing 
on your research? Those are important to resolve and this is why we suggest 
[contacting us](http://escience.washington.edu/office-hours/#CloudComputing).


The cloud vendors -- through credit grants and other promotions -- hope to prime the pump of cool research 
happening on *their* cloud platform; and we think that is awesome provided 
it is win-win for both the cloud vendor and for you the researcher. 


From this preamble we conclude on a cautionary note: Treating these incentivizing credit grants as a source of
research funding can be a bit of a trap.  It creates a dependency on something out of your control and it can 
obscure the more central issues we outline above. With this in mind let's now review the situation with
the three major cloud providers: AWS, Azure and Google. 


[Microsoft Azure](http://https://azure.microsoft.com) formerly had a cloud credit program called **Azure For Research**. 
To the best of our knowledge this program is shutting down or discontinued but Microsoft is a very research-oriented company 
so they are very open to engaging in conversations about your research program. 
[Amazon Web Services](https://aws.amazon.com/research-credits/) has a formal research credit granting program
where they evaluate a short proposal that you would write. 
Google, like Azure, will also respond positively to direct communication on research projects; however they do not 
currently have an open proposal-based program for granting credits to the best of our knowledge.  
Engaging with these vendors is a matter of initiatives and theirs. However please
[contact us](http://escience.washington.edu/office-hours/#CloudComputing)
if you need help with grant writing pertaining to the cloud including cost estimation; or if you need 
an intro-connection to the vendors. 



### Q: How much funding is available as cloud research credit grants?


Research credit grants traditionally run thousands to tens of thousands of dollars in cloud credits. 
(No actual dollars, to be clear.)  They generally require you to do a cost estimation.


### Q: What should my proposal emphasize to increase my chances of receiving a cloud credit award? 


Three things beyond outlining the computational nature of your research. First that you are interested in going 
'all in' on cloud computing.  Second you understand and appreciate the advantages of using the cloud as enumerated thus 
and such. In other words: Indicate that the cloud does stuff you need to do.  Third that you regard an award to be 
transitional support to help you evaluate the cloud platform.  That is: You do not regard a cloud credit grant as 
an ongoing source of funding.  This plus a summary of your research and why it is cool we find works well.


### Q: Why do these companies give out these grants? 


Mindshare. They want cutting edge researchers such as yourself to invest in their technology. They realize it 
can be a big leap to understand and use their cloud platform; so they are essentially providing an incentive to
try it out on a serious (computational) scale.


## Q: I'm a faculty member teaching a course and I'd like to do that on the cloud. Can I get sponsorship from a cloud vendor? 


Our response to this question is in three parts (and we suggest that first reading the preceding section might be helpful). 


First: 
You can 
[contact us](http://escience.washington.edu/office-hours/#CloudComputing)
and we will put you in touch with the cloud vendors to discuss this with them. (It is beyond our current purview.) 
Second: We do work closely with a number of faculty members on the technical aspects of 
teaching a course that uses the public cloud; so if you are interested in help with *that* then again
just get in touch.  
Third: We are working on developing -- in collaboration with the cloud vendors -- a sort of entry process 
to standardize use of the cloud in the classroom. This will cover all facets including how cloud resources 
are paid for. We will reflect our progress on this here at [cloudmaven](http://cloudmaven.org).  


## Q: How much does the cloud cost? 


- Archival is $50 (or less) per Terabyte per year; and note these qualifiers on retrieval from archives
  - The wait time for retrieval is a few hours and runs $10 per Terabyte...
  - ...and you can pay more to retrieve archival data in minutes
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


## Q: Can you provide a brief glossary of cloud jargon?


- Elastic: A term that generically indicates the cloud's capacity to scale up and scale down as needed
- Stack Overflow: A knowledge base of answers to common questions; a great solution resource for cloud computing
- YouTube: A tutorial knowledge base:  thousands of video walk-throughs; a great narrative resource for learning cloud computing 
- IOT: Internet of Things, a distribution of embedded devices that communicate with one another and with the cloud
- Server: A computer that acts as an information resource in relation to one or more Clients
- Client: A computer that acts as an information consumer in relation to one or more Servers 
- API: Application Program Interface, a means of exchanging information between two computers 
- Object storage: Digital storage with metadata but limited file access; see the dedicated section on this topic above
- Virtual Machine: Abbreviated VM, a computer emulation that is for all intents and purposes simply a computer you can use for research
- Instance: A computer or VM on the cloud that you appropriate for use for some amount of time
- Image: A digital representation of the state of a computer that can be stored and recovered from storage (as a tar ball for example)
- Identity and Access Management (IAM): An umbrella term for managing cloud account resources including Users and permissions
- Archival: A form of data storage that costs on the order of $50 per Terabyte per year
- Azure: The public cloud provided by Microsoft
  - Blob storage: The Azure object storage technology
- GCP: Google Cloud Platform, a public cloud provided by Google
  - Google Cloud Storage: The Google object storage technology
- AWS: Amazon Web Services, the public cloud provided by Amazon
  - S3: The AWS object storage technology, short for *simple storage service*


## Q: Why is your group's motto '*Build ~ Test ~ Share*'? 


We feel that research computing needs to advance to keep pace with data volume and complexity. Three ways in particular
of accomplishing this are touched on by the Build Test Share motto:


- Build quickly using new tools like Python's machine learning library SciKitLearn
- Establish confidence in your software by creating a test framework
- Take advantage of data-sharing technologies to increase the value of your work to your colleagues


## Q: What is the cloud's operating system? 


Cloud machines are available running Linux or Windows. Furthermore there are many different versions of these operating
systems available; and in addition to that using machine *images* there are libraries of pre-built customized operating
systems that may align with your particular needs. 


## Q: How powerful is a cloud computer? 


Here as with operating systems you have a vast array of choices: Cloud machines vary in power and memory capacity
and number of cores from something like a raspberry pi to the most powerful state-of-the-art machine available on
the market today. See the links above concerning choices of machine type from the three cloud providers we follow.


## Q: What is cluster computing on the cloud?


Cluster computing refers to aggregates of computers that in some way divide up a large computing task and work
on it in parallel. In the case where there is a lot of talk between computers (or 'nodes') this is often termed
High Performance Computing. When the task does not involve a lot of interconnection it is sometimes called
High Throughput Computing. The latter is easier to implement because the inter-node communication can be complicated.


Cluster computing on the cloud is common practice and heavily supported. Several examples are documented
at [this website](http://cloudmaven.org) for example.


## Q: Do I just treat the cloud like any other computer as I develop my research code? 


Yes and no.  If your computing is straightforward then pretty much yes. If you are heading into high performance
computing, multi-threading, and the like: It is a good idea to take a test-and-verify approach where you do not
assume that everything in the cloud works perfectly. This warning particularly applies to complex workflows 
that do not self-check as they make progress. What we are warning against here is something like this: You
build and run a complex set of programs on the cloud which appropriate a lot of compute resources.  The job 
completes having cost you $4000 in resources.  You examine your output files only to discover they contain garbage. 
Why did this happen? Some aspect of the migration of your workflow to the cloud did not go as expected. Therefore: 
Test in smaller stages before running the $4000 job. 


## Q: Do you have any cloud success stories you can share?


Yes; we share one here and refer you to our other content on this website, particularly the various case studies.


Tim Durham works in genomics at UW and has an analytical pipeline that operates on segments of the human genome; up to 3 billion base 
pairs. He is working to interpolate ('impute') information linking human cell types to proteins.  Using the "server room at the end 
of the hall" Tim can complete small data subset processing runs in a matter of a week or two; in the process possibly precluding other 
researchers from using those machines. By taking the computing task to the public cloud (Tim used both AWS and Azure) he is able to 
allocate many times more resources at once and finish a computation in a matter of hours. Hence three important cloud computing 
positives: No 'shared resource' impediment, no wait time to start processing, and faster processing for tasks that can be parallelized. 


When Tim completes a processing run he turns off the Linux machines he is using and thereby stops paying for them. This is the 
cloud utility cost model in action. The recovered output data are analyzed and his methods are refined. Once he reached an optimal
configuration he did a large run and wrote the corresponding research paper. His work made use of a technology for memory-intensive
analysis called Apache Spark.



## Q: What does your assertion that the cloud is secure mean? 


The cloud is extremely secure provided that the research group learns and follows appropriate guidelines. Both AWS and Microsoft have 
agreements with UW that permit the construction of HIPAA-compliant secure computing environments for working with personal health
information. We are working to make implementation of these environments straightforward to facilitate medical research. 


## Q: Can I configure the cloud to catch problems before the problems runs out of control? 


Yes; and this is another ongoing area of learning and development in our group. Our first big milestone has been implementation
of daily spend in the Inbox. Contact us for more information.


## Q: How do I get in touch with you? 


Look us up at the [eScience Institute's WRF Data Science Studio](http://escience.washington.edu/wrf-data-science-studio/).


{% include links.html %}
