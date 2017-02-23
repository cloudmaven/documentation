---
title: AWS HIPAA
keywords: aws, hipaa, procedures
last_updated: January 25, 2017
tags: [AWS, HIPAA]
summary: "A HIPAA-compliant research system on AWS"
sidebar: mydoc_sidebar
permalink: aws_hipaa.html
folder: aws
---

## Introduction
The purpose of this document -- available at http://cloudmaven.org -- is to present a hypothetical data management system
for Private Health Information (PHI) on the AWS public cloud that is compliant with HIPAA regulations. These regulations 
in particular require data be encrypted both at rest (i.e. on a storage device) and in transit (i.e. moving from one storage
device to another).  Our hypothetical situation is described in further detail below. Please note that we are also building
out this construct on the Microsoft Azure public cloud. 

## Links
- [AWS HIPAA template](https://aws.amazon.com/quickstart/architecture/accelerator-hipaa/)

## Warnings
- This web page represents our best attempt at designing a HIPAA-compliant data management solution but at no point do we state or 
imply that if you follow these procedures you are HIPAA-compliant.***
- ***AWS has nine HIPAA-aligned technologies. A HIPAA-compliant system on AWS means that only these technologies can come into contact
with Private Health Information.  One may certainly use other technologies in such a system provided they do not touch PHI.***
- ***HIPAA compliance is an obligation placed on both data system builders and on health researchers as system users.  It is our
contention that failure to comply and/or data compromise is most likely be caused by human error. The public cloud is not 'more vulnerable'
than on-premise systems; on the contrary it is less vulnerable both physically and in terms of robust secure technologies.***

## User story

A scientist *K* receives approval from an IRB to work with PHI data. The intent is to analyze these data for patterns
in a secure, HIPAA-compliant environment, abbreviated HCDS for 'HIPAA-compliant data system'. 
*K* contacts a technology expert *J* and a research data provider *S* with a request for the data and the HCDS. 
After due diligence both are provided and *K* is given an ssh key. *K* logs on to the HCDS through a secure gateway 
and carries out the data analysis over a period of time. During this period IOT devices distributed among patients 
report anonymized health data to the HCDS where they are used to supplement the research analysis. When the study 
concludes any sensitive data are stored to a secure archive external to the provided system; and the system itself 
is dismantled. Log files are retained and archived that contain the complete record of operation of the HCDS. 

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
  * [HIPAA Privacy Rule Summary](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html)
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
  * Triggered by new object in bucket in the S3 input bucket
  * This Lambda service is managed using a role
* Set up database
* Push data to S3
  * No PHI in filenames
  * Look into Cloudberry
  * AWS CLI
* Launch W x 5 Dedicated; assign S3 access role; encrypted volumes, s/w pre-installed (pipelines)
  * Update issue: Pipeline changes, etcetera
* W can be pre-populated with reference data (Sheena scenario)
* Sheena redux
  * B
    * Create SQS queue of objects in S3
    * Start a W for each message in queue...
  * Go
    * Latest pipeline... EBS Genomes... chew
    * If last instance running: Consolidate / clean-up
* SNS topic notifies me when last instance shuts down.
  * Run Ansible script to configure Ws (patch, get data file names from DynamoDB table, etcetera)
  * Get Ws the Key from E
  * The Ws send an Alert through the NAT gateway to Simple Notification Service (SNS) 
    * Which uses something called SES to send an email to the effect that the system is working with PHI data 
      * Ws pull data from S3 using VPC Endpoint; thanks to the Route table
      * Ws decrypt data using HomerKey
      * Ws process their data into result files: Encrypted EBS volume. 
      * Optionally the result files are encrypted in place in the EBS volume.
  * Through the VPC Endpoint the results are moved to S3.
  * Ws send an Alert through the NAT gateway to Simple Notification Service (SNS) 
    * which uses something called SES to send another email: Done
  * Ws evaporate completely leaving no trace
  * B returns to quiescent state. 


## Procedure

Create a Virtual Private Cloud

![pic0001](/documentation/images/aws/hipaa0001.png)

![hipaa0002](/documentation/images/aws/hipaa0002.png)

We use the name 'czarhipaa'; this should be unique.

CIDR as shown is typical.

Dedicated Instance means: Nobody else allowed here. 

![hipaa0003](/documentation/images/aws/hipaa0003.png)

Now it exists; time to fill it with stuff.

### Pro Tip
You can be more cost-effective by not making this Dedicated but then your PHI-Using instances will have to be launched Dedicated. 
This is carte blanche Dedicated and so is more expensive. We do not consider this option in this tutorial because we are erring on 
the side of caution rather than cost. 


### Create a subnet

![hipaa0004](/documentation/images/aws/hipaa0004.png)

![hipaa0005](/documentation/images/aws/hipaa0005.png)

Public subnet addresses will be of the form: 10.0.0.2, .3, .4, ... .254

![hipaa0006](/documentation/images/aws/hipaa0006.png)

Take note of the AZ: 

![hipaa0007](/documentation/images/aws/hipaa0007.png)

We could do multiple public sub-nets by creating more than one in multiple Azs; that is a big-time concept.

Now the private one: 

![hipaa0007](/documentation/images/aws/hipaa0007.png)

![hipaa0008](/documentation/images/aws/hipaa0008.png)

![hipaa0009](/documentation/images/aws/hipaa0009.png)

![hipaa0010](/documentation/images/aws/hipaa0010.png)

Attach it to the VPC: 

![hipaa0011](/documentation/images/aws/hipaa0011.png)

![hipaa0012](/documentation/images/aws/hipaa0012.png)

Now for the NAT Gateway

![hipaa0013](/documentation/images/aws/hipaa0013.png)

Choose the public one in czarhipaa

![hipaa0014](/documentation/images/aws/hipaa0014.png)

![hipaa0015](/documentation/images/aws/hipaa0015.png)

Notice we Created a New EIP

![hipaa0016](/documentation/images/aws/hipaa0016.png)

Now the Route Table

![hipaa0017](/documentation/images/aws/hipaa0017.png)

![hipaa0018](/documentation/images/aws/hipaa0018.png)

![hipaa0019](/documentation/images/aws/hipaa0019.png)

Here they are (including the default main one): 

![hipaa0020](/documentation/images/aws/hipaa0020.png)

![hipaa0021](/documentation/images/aws/hipaa0021.png)

Edit and modify as shown:

![hipaa0022](/documentation/images/aws/hipaa0022.png)

Save

And then under Subnet Associations tab: Edit: 

![hipaa0023](/documentation/images/aws/hipaa0023.png)

Now let us go back to the Route Table selector

![hipaa0024](/documentation/images/aws/hipaa0024.png)

![hipaa0025](/documentation/images/aws/hipaa0025.png)

![hipaa0026](/documentation/images/aws/hipaa0026.png)

Subnet Associations tab: 

![hipaa0027](/documentation/images/aws/hipaa0027.png)

![hipaa0028](/documentation/images/aws/hipaa0028.png)

Now for the Endpoint

![hipaa0029](/documentation/images/aws/hipaa0029.png)

Notice that this has Full Access; we will restrict access at a later step.

![hipaa0030](/documentation/images/aws/hipaa0030.png)

end as of Jan 27 2017.

{% include links.html %}
