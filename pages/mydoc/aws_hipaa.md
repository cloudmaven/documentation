---
title: AWS HIPAA
keywords: aws, hipaa, procedures
last_updated: January 25, 2017
tags: [AWS]
summary: "A HIPAA-compliant research system on AWS"
sidebar: mydoc_sidebar
permalink: aws_hipaa.html
folder: mydoc
---

## Introduction
The purpose of this document -- available at http://cloudmaven.org -- is to present a procedural and a technical background
for creating and operating a HIPAA-compliant research environment on the AWS public cloud. A corresponding effort is underway
on the Microsoft Azure cloud. 


## Program 

1. Create a diagram showing the EMR > PHI data pool > VM with corresponding IRB, researcher and patient
2. Anticipate <new data to EMR> pipeline
3. Anticipate <IOT to VM> pipeline
4. Anticipate changes to <PHI > VM> process
5. Implement Virtual Private Cloud
6. Synthetic data: Generate
7. Create an IOT signal
8. Create IOT pass-through mechanism
9. Establish software tools including Jupyter on VM
10. Review with IT personnel 
11. Review with management
12. Review with researchers

## Concerns

* Logging: CloudWatch and CloudXXXXX are AWS logging services; and this is frequently parsed using Splunk
* Intrusion detection! Jon Skelton (Berkeley AWS Working Group) reviewed use of Siricata (mentions 'Snort' also) 
* Include an encryption path for importing clinical data 
* Include a full story on access key management
* The IOT import will -- I think -- be a poll action: The secure VM is polling for new data
* This system should include a very explicit writeup of how the human in the loop can break the system
* Acceptable for data on an encrypted drive to moves through an encrypted link to another encrypted drive? To clarify: Must the data be further encrypted at rest first? 
* Filenames may not include PHI. Hence there is an obligation on the MRs to follow this and/or build it into file generation.
* CISO approval hinges on IT, Admin and Research approvals. 

## Terminology and Concepts
* Ansible
* Availability Zone
* Bastion Server (abbreviated **B**)
* CIDR
* Cloudberry
* Dedicated Instance 
* HIPAA [Health Insurance Portability and Accountability Act](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)
* Lambda Service
* NAT Gateway
* Worker

### Conceptual distinction on PHI contact

Herein we identify tools and technologies that do / do not interface directly with Private Health Information:
* Tools that do not come in contact with PHI can be thought of as 'triggers and orchestration'.
* Services that may come in contact with PHI can be described as 'data and compute'

### HIPAA-aligned technologies
Nine AWS Technologies under the AWS BAA that are HIPAA-aligned:
* S3
* EC2
* RDS
* EBS
* DynamoDB
* EMR
* ELB
* Glacier
* Redshift

### Useful Trigger/Orchestration Tools
* Lambda
* Virtual Private Cloud (VPC)

### Encryption
* HIPAA requires data be encrypted at rest, i.e. on a storage device
* HIPAA requires data be encrypted in transit, e.g. moving from one storage device to another

## Aggregated Notes

### Multiple sources of data
* Electronic Medical Records (EMR)
* A Data Warehouse (tables) 
* A Clinician 
* Sensors stream data from patient

### Destinations
* S3 bucket
* EBS/EFS 

### Notes
* Encryption software such as PGP produces a Key.
* On AWS create a VPC
* On the VPC create a public-facing Bastion Server B
* B has an Elastic IP address: This will persist
* Inside the VPC create public and private subnets using a Routing Table. 
  * NAT Gateway with Routing Table.
* On private subnet place a small Dedicated EC2 instance E.
  * B has only port 22 open (ssh) 
  * B uses Secure Groups on AWS to limit access to certain URLs. 
* Using ssh / WinSCP copy Key to BS. From there move Key to E. 
* Create an AMI to do processing. Call this W.
* Create Role that allows a W to read from and write to S3.
* Set up Ansible-assisted process for configuring and running jobs on EC2 instances
  * What is Ansible?
* Set up S3 buckets for input and output 
* Input buckets only accept http PUT. No GET or LIST.
* S3 buckets have a VPC Endpoint included: Terminates inside the VPC.
* Set up a DynamoDB table to track names of uploaded files.
* Set up a Lambda service 
  * Triggered by 'new object in bucket' in the S3 input bucket
  * This Lambda service is managed using a role
* Set up database
* Some entity pushes data to S3. 
  * File names must not contain PHI. 
  * Uses a 3rd party app such as Cloudberry
    * What is Cloudberry?
  * Uses the AWS CLI
  * Uses an API call (this is a programmatic way to keep PHI out of file names)
    * Lambda notices this, appends the file names to DynamoDB and pings the BS. 
    * The BS tries to run a new processing job
* Launch five W instances, dedicated
* Assign them S3 access role
* W have encrypted volumes
* W have a pipeline pre-installed
  * The pipeline may be update and the AMI could subsequently be updated as well
* EBS volumes come pre-loaded with reference data (non-PHI) that the pipeline might use
* Sheena's notes
  * Bastion Server Setup
    * Get worker public key from S3 (which allows us to ssh from bastion into worker if need be) 
    * Create SQS queue of all objects (samples) listed in S3 bucket 
    * Kick off a worker instance for each message in the queue
  * Setup and Execution
    * Grab latest pipeline code, install
    * Create EBS Genomes volume from snapshot
    * Grab message from SQS which is really a file for analysis in S3
    * Grab fastq files from S3.
    * Run analysis
    * Write message to done queue.
    * If last instance running, grab certain analysis files from S3 to create run level output
* SNS topic notifies me when last instance shuts down.
  * Run Ansible script to configure Ws (patch, get data file names from DynamoDB table, etcetera)
  * Get Ws the Key from E
  * The Ws send an Alert through the NAT gateway to Simple Notification Service (SNS) 
    * Which uses something called SES to send an email 'system is working on PHI data'. 
      * Ws pull data from S3 using VPC Endpoint; thanks to the Route table
      * Ws decrypt data using HomerKey
      * Ws process their data into result files: Encrypted EBS volume. 
      * Optionally the result files are encrypted in place in the EBS volume.
  * Through the VPC Endpoint the results are moved to S3.
  * Ws send an Alert through the NAT gateway to Simple Notification Service (SNS) 
    * which uses something called SES to send another email: 'We're done now.'
  * Ws evaporate completely leaving no trace. 
  * B returns to quiescent state. 

## Procedure

We use the name 'czarhipaa'; this should be unique.

CIDR as shown is typical.

Dedicated Instance means: Nobody else allowed here. 

Now it exists; time to fill it with stuff.

### Pro Tip
You can be more cost-effective by not making this Dedicated but then your PHI-Using instances will have to be launched Dedicated. 
This is carte blanche Dedicated and so is more expensive. We do not consider this option in this tutorial because we are erring on 
the side of caution rather than cost. 

Next: Create a subnet

Public subnet addresses will be of the form: 10.0.0.2, .3, .4, ... .254

Take note of the AZ: 

We could do multiple public sub-nets by creating more than one in multiple Azs; that is a big-time concept.

Now the private one: 

Attach it to the VPC: 

Now for the NAT Gateway

Choose the public one in czarhipaa

Notice we Created a New EIP

Now the Route Table

Here they are (including the default main one): 

Edit and modify as shown:

Save

And then under Subnet Associations tab: Edit: 

Now let's go back to the Route Table selector…

And now Subnet Associations tab: 

[HIPAA Privacy Rule Summary](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html)

{% include links.html %}
