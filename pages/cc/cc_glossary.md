---
title: Cloud Computing Glossary
keywords: cloud, glossary
last_updated: October 6, 2016
tags: [research_computing]
summary: "A glossary of terminology"
sidebar: mydoc_sidebar
permalink: cc_glossary.html
folder: cc
---

## Introduction
The purpose of this glossary is to provide you a research-oriented guide to some of the common terms used in cloud computing. Jocelyn is now editting this file.

## Links

## Warnings
***There are two listings here: Common terms followed by General glossary***

***Terms that refer to a specific cloud or technology may include a reference 
to that context in [square brackets]***

***All cost estimates are in US Dollars and should be independently 
verified. They have tended to decrease with time.  Listings here may 
become out of date.***

## Common Terms

Amazon Web Services (AWS): The public cloud provided by Amazon

Microsoft Azure: The public cloud provided by Microsoft 

Google Cloud Platform (GCP): The public cloud provided by Google

IAM: Identity and Access Management

## General Glossary

- AMI: Amazon Machine Image, a stored copy of a cloud VM that can be used to create an actual cloud VM.
- CFD: Computational Fluid Dynamics, a common computational task in research that is very HPC-oriented.
- EBS: Elastic Block Storage (AWS), a file system mounted on an EC2 instance typically used for data and software.
- EC2: A cloud Virtual Machine or cloud VM on AWS.
- HPC: High Performance Computing, often indicates parallelized compute work that *does* require considerable communication between processes and computers.
- HTC: High Throughput Computing, often indicates compute work that is highly parallel with little requirement for inter-process communication.
- IAM: Identity and Access Management; umbrella term for managing your cloud account resources including Users and their permissions.
- IOT: Internet of Things, the distribution of embedded devices that typically communicate across a network to a central location which is in turn often implemented on the cloud. 
- RDS: Relational Database Service (AWS), a database that you make use of without having to maintain an underlying cloud VM. 
- S3: Bulk storage service on AWS.
- Stack Overflow: A website building a knowledge base of answers to common questions. Excellent resource.
- YouTube: An excellent free resource -- in fact a website repository of instructional videos related to building research computing solutions. 


- Account administrator: A person with administrative privileges associated with a cloud account (i.e. a billing account).

- Alarm: kilroy

- AMI: Amazon machine image (AWS)

- API: Application Program Interface, an automated mechanism for exchanging information between two computers. 

- API Gateway: A service provided by AWS that supports data access via an API

- Billing: The process of tracking and breaking down cloud utility spending based on tagging assets.

- Blob storage: A storage service entity on Azure.

- Client: Computers that consume information from Servers and/or provide information to Servers. 

- Cloud account: A virtual entity with permission to use a particular public cloud with an associated billing mechanism. The cloud 
account is used to appropriate and release resources which have associated billing rates. For example a cloud account might 
include a virtual machine that runs continuously for one month at a rate of ten cents per hour. At the end of one month 
this resource would incur a $72 charge. 

- Container: A virtualization of a computing environment (such as **Docker**) as a 'user space instance'. 
Synonymous: Container, partition, virtualization engine, jail. From the perspective of a running program
or from that of a User: A container appears to be a typical computer. However while computers provide 
visibility of all resources a container provides visibiltiy only of assigned resources. 

- Data signal: A conceptual wire carrying information, typically backed up by physical hardware.

- [EBS](http://www.rightscale.com/blog/cloud-industry-insights/amazons-elastic-block-store-explained): Elastic Block 
Storage; disk memory associated with EC2 instances on AWS. Cost estimate $0.10 per (Gbyte-month)

- EC2: Elastic Cloud Compute instance, a virtual machine on AWS

- EFS: Elastic File System (AWS), similar to NFS. 

- Elastic: Commonly used as shorthand for "available in large quantities on request" to emphasize that you can
allocate extensive computing resources on the cloud when needed and then relinquish them when no longer
needed. As an idealized example: Suppose a parallelizable compute job requires 100 hours on your machine. 
On the cloud you can appropriate 100 such computers at once and complete the job in 1 hour. 

- Endpoint: A connection point for a data signal. 

- GitHub AWS version: kilroy

- Group: A virtual association of resources within a cloud account.

- [HIPAA](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act): Health insurance portability 
and accountability act. In short: A set of standards for securely managing Private Health Information (PHI).

- Hypervisor: A computer that creates and runs virtual machines (VMs) through some combination of software, firmware
and hardware. A hypervisor is also called a VMM for *virtual machine monitor*. See more under 'Virtual Machine'.

- Virtual Machines: A 'heavy weight' systems implemented on a host system 
and managed by a hypervisor which provides the VM access to the kernel of the host operating system.
This has the advantage that a VM can run *any* operating system regardless of the kernel's 
operating system in contrast to a lighter-weight container approach which shares OS type with 
the kernel. 

- IAM User: A user account created by an account administrator for specific use by a project participant.

- IOT: Abbreviates 'Internet of Things', typically embedded devices that send and possibly receive information from 
some environment. This environment might for example be a computer lab, a street intersection, a hospital room, 
or a remote glacier.

- Key pair: A means of accessing kilroy.

- Lambda: An AWS service (dissociated from a VM) that can carry out a wide variety of activities under restriction 
of "must take a short amount of time".

- MFA: Multi-Factor Authentication, a means of protecting resources

- ML: Machine Learning, referring to a large class of methods in computer science which typically carry out 
classification tasks based on learned rules. Learning is either guided or unguided, meaning that either a 
test dataset with correct assignment information is used; or the algorithm simply operates on statistical 
distributions of data. Sub-categories include email filtering, text interpretation, audio transcription, 
vision, neural networks, deep learning, cluster analysis, Bayesian networks and genetic algorithms. See
the entry for SciKitLearn for the most common Python-based ML environment. 

- NIC: kilroy

- That thing on AWS that is a NIC: kilroy

- NLTK: Natural Language Toolkit, a suite of Python libraries and programs for Natural Language Processing (NLP).

- Policy: kilroy

- Project: Shorthand for a body of work within a research program, assumed to have some computational elements.

- RDS: Database service on AWS

- Role: kilroy

- S3: Storage on AWS

- Scalability: The capability to handle a growing work load, a term used in cyber-infrastructure to indicate
that a given system can accommodate an increase in demand for resources by allocating more (for exampl on 
the public cloud) or a decrease in demand by down-sizing thereby (again on the cloud) reducing cost of operation.

- Scaling horizontal versus vertical: Horizontal scaling means expanding resources by adding nodes (or removing them); 
for example by adding commodity (low-cost) nodes to a cluster performing a distributed compute task. In contrast vertical
scaling means making a single node in a system more (less) powerful. Examples include adding CPUs and adding RAM.

- Scheduler kilroy

- Scikit-learn: A machine learning library for Python designed to interoperate with NumPy and SciPy.

- Server: A Computers acting as an information resource. More extensively a server can be thought of as
a compute entity acting as the distal resource in a server-client relationship. Servers typically "listen" 
for signals and respond. There is implicitly a multi-layered underlying infrastructure that manages the 
"how" of these communication exchanges, from wires and voltages up through communication protocols.

- Snapshot

- [Spot Market](aws_spot_market.html): 

- Thing: AWS, an entity that can have a Role.

- Third Party: A company or other entity -- but not a cloud provider -- which builds and provides something useful to you 
(the first party) related to research computing and perhaps relevant to a cloud platform (provided by a second party). 
Example: The PuTTY ssh application is third party software that facilitates connecting to cloud VMs on Windows.

- Utility model: 

- VM: Virtual machine (traditional term). We use the term here to indicate a computer; usually a computer 
operated by a public cloud vendor. On AWS a VM is called an EC2 instance. 

- VPC: Virtual Private Cloud (AWS)

{% include links.html %}
