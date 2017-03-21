---
title: AWS HIPAA
keywords: aws, hipaa
last_updated: January 25, 2017
tags: [AWS, HIPAA, medicine, data_management, case_studies, storage, research_computing, data_science]
summary: "A HIPAA-compliant research system on AWS"
sidebar: mydoc_sidebar
permalink: aws_hipaa.html
folder: aws
---

## Introduction

[This document](aws_hipaa.html) presents a secure data management system, specifically using the 
motivation of managing Private Health Information (PHI) under HIPAA regulations on the public cloud. 
This template applies more generally to secure data management in research computing.

HIPAA regulations require data be encrypted both at rest (e.g. on a storage device) and in 
transit (e.g. moving from one storage device to another).  Our hypothetical situation is described 
in further detail below; it is well to keep these rest/transit encryption notions in mind. 

Please note that while this study uses AWS we are also building out the construct on the 
Microsoft Azure public cloud. 

## Links

- [HIPAA home page](https://www.hhs.gov/hipaa/index.html/)
- [HIPAA on Wikipedia](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)
- [HIPAA Privacy Rule Summary](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html)
- [AWS HIPAA template](https://aws.amazon.com/quickstart/architecture/accelerator-hipaa/)


## Warnings

- ***AWS has nine HIPAA-aligned technologies. A HIPAA-compliant system on AWS means that only these technologies can 
come into contact with PHI.  Other technologies can be used in an ancillary capacity provided they do not interact
directly with PHI data.***
- ***HIPAA compliance is an obligation placed on the data system builder and the medical researcher.
The public cloud is very secure: physically and technologically. 
We contend that data system failure or compromise is most likely to be caused by human error.***
- ***File names may not include PHI. They may include identifier strings that would be indexed in a secure table.***

### Preliminary Work

#### Kilroy stack

- Add K's remarks and J's remarks in here
- AB: How to do determine Account has been registered at AWS as PHI/HIPAA-active?
- Generate and incorporate a scientist workflow diagram with extensive caption per User Story
- Generate and incorporate a complete HCDS architecture diagram near the top of this 
- Create a sub-topic around **L**: In coffee shop, in a data center (out of Med Research), etcetera
  - The 'in transit / at rest' component leaves a sparking wire in **L**: Section on risk added
- Need explanation of public/private subnet collision avoidance
  - Public subnet elements also have private subnet addresses.
  - Verify protocol is that new resources auto-generated will be on the private subnet
    - AB How is this done? We got as far as 'no default' for public and private both
  - Verify automated allocation will choose free ip addresses on the private subnet
  - Verify protocol is to *not* create new resources on the public subnet
  - This is tremendously important so that a new **Wi** is not publicly visible
  - Look at the VPC Routing Table "default subnet" column (verify this is correct)
- Key management story
  - Rename **K2** as **K_Bastion** and describe where it lives on **L**, add to Risk
    - It may make sense to describe chain of custody of **KBastion**
- Free up and assign **B** an Elastic IP address that will persist
  - Verify that this is publicly discoverable and place this fact in Risk
  - Rename **K3** as **K_EC2**
  - Chain of custody of **K_EC2**
  - How do keys work in view of an AMI source?
- EBS Encryption Keys should be a Risk sub-section
  - EBS encryption select has an account default key: Details are listed below
  - Notice that publishing these details is not technically bad for pedagogy... 
    - but I have a bit of a nagging doubt here: Are these "Details" global/permanent?
    - The screencap redacts to be on the safe side; stay with that for now
- Risk due diligence: Check the DLT account T&C; "who is responsible for the risk?" 
- Risk entry: We do not encrypt the boot volume  
- Risk entry: EC2 swap space: How does this touch on PHI?
- How are keys / Roles managed when spinning up / shutting down **Wi**? 
  - For now we allow that **EC2** is the only game in town
- Look at the *JS* *SK* scenario and build out the IAM component for *SK*
  - e.g. turning machines on and off
  - do with console? do with CLI?
  - AB: Help needed!
- Differentiate SQS and SNS
- What is Ansible and what does it get us?
- Can/should the NAT Gateway be used to pull updates from GitHub?  Generalize.
- DDil on elastic IP: NAT Gateway? Bastion? IG? 
- Fix the RT / subnet editing section... gotta get that right
- What are the tradeoffs in building **B** and **M** and **Wi** from AMIs?

#### User story

- A scientist *SK* receives approval from an IRB to work with PHI data. 
  - Intent: Analyze these data in a secure, HIPAA-compliant data system (herein HCDS) 
- *SK* contacts *JS* to build the HCDS as a working environment
  - IRB approval review
  - System **H** is built by *JS*; includes an S3 bucket for inbound PHI data **SDI**
  - Data uploaded to **SDI**
- *SK* is provided with access
  - Keys: **K_Bastion** and **K_EC2**
  - IAM User account with 
  - *K* logs on to the HCDS through a secure gateway 
  - *K* carries out the data analysis over a period of time
    - The system logs all activity 
  - IOT devices distributed to patients report health data to the HCDS 
    - These data supplement the research
- The study concludes 
  - Sensitive data are stored to a secure archive 
  - The HCDS is deleted 
  - Log files are archived to preserve a complete record of operation for the HCDS

#### Plan of action for this HCDS Proof of Concept

0. Write up the procedural
1. Create a system architecture and diagram  
  - Anticipate <new data to EMR> pipeline
  - Anticipate <IOT to VM> pipeline
  - Anticipate changes to <PHI > VM> process
  - AWS is the big box
  - VPC is inside
  - Public and Private subnets are inside VPC
  - NAT gateway inside the Public subnet box
  - Internet Gateway on boundary of VPC
  - S3 Endpoint on boundary of VPC
2. Create artificial data 
  - data manufacturing software 
  - generate source artificial data (from EMR)
  - generate IOT stream
  - anticipate study-to-clinical pipeline
3. Complete system including analytical tools
  - include R, Python, Jupyter 
4. Review with IT personnel (JP first), mgmt, researchers

#### Details to incorporate

- Logging: CloudWatch and CloudXXXXX are AWS logging services; and this is frequently parsed using Splunk
- Intrusion detection! Jon Skelton (Berkeley AWS Working Group) reviewed use of Siricata (mentions 'Snort' also) 
- Include an encryption path for importing clinical data 
- Include a full story on access key management
- The IOT import will -- I think -- be a poll action: The secure VM is polling for new data
- This system should include a very explicit writeup of how the human in the loop can break the system
- Acceptable for data on an encrypted drive to moves through an encrypted link to another encrypted drive? 
To clarify: Must the data be further encrypted at rest first? 
- Filenames may not include PHI. Hence there is an obligation on the MRs to follow this and/or build it into file generation.
- CISO approval hinges on IT, Admin and Research approvals. 

#### Partial list of terminology and concepts

* Ansible
* Regions and Availability Zones on AWS
* Bastion Server 
* Siricata / Snort
* CIDR
* Direct tools like **ssh** and third party apps like Cloudberry 
* Dedicated Instance 
* Lambda Service
* NAT Gateway

#### PHI contact model

"How can your system be an HCDS if you are using Lambda?" We identify tools and 
technologies that do / do not interface directly with PHI.

- Tools that do not come in contact with PHI can be thought of as 'triggers and orchestration'.
- Services that may come in contact with PHI can be described as 'data and compute'

#### HIPAA-aligned technologies

Nine AWS Technologies under the AWS BAA that are HIPAA-aligned. Actually more now and the
accrue 'automatically' as AWS makes progress.

- S3 storage
- EC2 compute instances (VMs)
- EBS elastic block storage: Attached filesystem
- RDS relational database service
- DynamoDB database
- EMR elastic map reduce: Hadoop/Spark engine support
- ELB elastic load balancer
- Glacier archival storage
- Redshift data warehouse

#### Useful Trigger/Orchestration Tools

- Lambda
- Virtual Private Cloud (VPC)

#### Encryption

- HIPAA requires data be encrypted at rest, i.e. on a storage device
- HIPAA requires data be encrypted in transit, e.g. moving from one storage device to another

#### Multiple sources of data

- Electronic Medical Records (EMR)
- A Data Warehouse (tables) 
- A Clinician 
- Sensors stream data from patient

#### Destinations

- S3 bucket
- EBS/EFS 

#### Procedural format

We punctuate the procedural steps needed to build the HIPAA-Compliant Data System (HCDS) 
with short notes on rationale, how things fit together. We also make extensive use of 
very short abbreviations (just about every entity gets one, indicated by **boldface** 
and obsessive re-naming of everything using the Project Identifier Tag (PIT)

### Part 1: Getting started

#### Activity Zero

Your absolute First Priority Step 0 is to designate to AWS that the account you are using
involves PII/PHI/HIPAA data.

#### Saving money

This will be a multi-day effort. Shut down instances to save money at the end of the day.

#### Review objectives

Our main objective is (see Figure below) to use a Laptop or other cloud-external data source
to feed data into a HIPAA-Compliant Data System **HCDS** wherein we operate on that data. 
The data are assumed to be Private Health Information (PHI) or Personally Identifiable 
Information (PII) as described in HIPAA regulations.

#### PIT means Project Identifier Tag (an informal term) 

- Write down or obtain a Project Identifier Tag (PIT) to use in naming/tagging everything
  - This is a handy string of characters
  - In our example here PIT = 'hipaa'. Short, easy to read = better

#### Source computer 

- Identify our source computer as **L**, a Laptop sitting in a coffee shop 
  - This is intentionally a *non-secure* source
  - **L** does *not* have a PIT
  - **L** could also be a secure resource operated by Med Research / IRB / data warehouse

We are starting with a data source and will return to encryption later. The first burst 
of activity will be the creation of a Virtual Private Cloud (VPC) on AWS per the diagram
above. We assume you have done Step 0 above and are acting in the capacity of a
system builder; but you may not be an experienced IT professional. That is: We assume
that you are building this environment and that you may or may not be doing research
once it is built; but someone will.

#### VPC via Wizard versus manual build

The easiest way to create a VPC is using the console Wizard. That method is covered in a 
section below and it can automate many of the steps we describe manually.  We describe 
the manual method to illuminate the components.

#### CIDR block specification

The CIDR block syntax uses a specification like **10.0.0.0/16**. This has two 
components: A 'low end of range' ip address **w.x.y.z** and a width parameter **/N**. 
w, x, y and z are integers from 0 to 255, in total 32 bits of address space.  

**N** determines an addressable space of size s = 2^(32 - N). For example 
N = 16 produces s = 2^16 or s = 65536 available addresses, starting at w.x.y.z.

An example: Suppose we specify 10.0.0.0/16.
Then s = 2^16 so 65536 addresses are available: 10.0.0.0, 10.0.0.1, 10.0.0.2, ...,
10.0.1.0, 10.0.1.0, ..., 10.0.255.255. **y** and **z** together span the address 
space.

These ip addresses are defined in the VPC, contextually *local* within the VPC.

Any subnets we place within the VPC will be limited by this address space.  
In fact we proceed  by defining subnets within the VPC with respective 
CIDR ranges, subranges of the VPC CIDR block.  The first subnet will have 
CIDR = 10.0.0.0/24 with 256 addresses available: 10.0.0.0, 10.0.0.1, ..., 
10.0.0.255. Five of these will be appropriated by AWS machinery, incidentally.
The second subnet will be non-overlapping with CIDR range = 10.0.1.0/24.

Since AWS appropriates five ip addresses for internal use
(.0, .1, .2, .3, and .255) we should look for ways of making 
ip address assignment automatic.  

### Part 2 Creating and populating a Virtual Private Cloud

#### Building the VPC 

Here we abbreviate elements with boldface type. In most cases the entity we create
can be named so to remind you: For consistency we have come up with a Project
Identifier Tag like 'hipaa' so that each entity can be given a PIT name: 'hipaa_vpc'
and so on.

- From the console create a new VPC **V**

  - Give **V** a PIT name 

  - **V** will not use IPv6v.  

  - **V** will have a CIDR block defining an ip address space
    - We use 10.0.0.0/16: 65536 (minus a few) available addresses

  - **V** automatically has a routing table **RT**
    - Select Routing Tables, sort by VPC and give **RT** a PIT name
      - 'hipaa_routingtable'
      - The routing table is a logical mapping of ip addresses to destinations

  - **V** is automatically given a security group **SG**
    - Select Security Groups, sort by VPC and give **SG** a PIT name
      - 'hipaa_securitygroup'

  - Create an associated Flow Log **FL**
    - In March 2017 the AWS console UI was a little tetchy so be prepared to go around twice
    - On the console view of the VPC: Click the Create Flow Log button
      - Assuming permissions are not set: Click on the Hypertext to **Set up permissions**
        - Because: We need to define the proper Role
        - On the Role creation page: Give the Role a PIT name; Create new; Allow
        - You now have an IAM Role for FlowLogs
          - This gives the account the necessary AWS permissions to work with Flow Logs
          - In so doing we fell out of the Create Flow Log dialog so... back around
      - Return to the VPC in the console
      - Click on Create Flow Log
        - Filter = All is required (not "accepted" and not "rejected" traffic)
        - Role: Select the role we just created above
        - Destination log group: Give it a PIT name 
          - Example: hipaa_loggroup

  - Create subnets **Spublic** and **Sprivate**
    - The private subnet **Sprivate** is where work on PHI proceeds
      - CIDR block 10.0.1.0/24
      - **Sprivate** will be firewalled behind a NAT gateway
        - This prevents traffic in (such as ssh)
    - The public subnet **Spublic** is for internet access
      - CIDR block 10.0.0.0/24
      - **Spublic** connects with the internet via an Internet Gateway
      - **Spublic** will be home to a Bastion server **B** 
      - **Spublic** will be home to the NAT Gateway **NG** mentioned above
        - **B** and **NG** are on the public subnet but also have private subnet ip addresses 
          - That is: Everthing on the public subnet also has a private ip address in the VPC. 
          - This will use the private ip address space 
          - Public names will resolve to private addresses within the VPC at need.

  - Create an an Internet Gateway **IG**
    - Give a PIT name as in 'hipaa_internetgateway'
    - Attach hipaa_internetgateway to **V**

  - Create a NAT Gateway **NG**
    - Give it a PIT name
    - Elastic IP assignment may come into play here

  - Create a routing table **RTpublic** 
    - This will supersede the **V** routing table **RT**
      - Give it a PIT name: 'hipaa_publicroutes'


-------------walled off needs repair----------------

    - For **RTpublic**
      - Select the Subnet Associations tab 
        - Edit subnet association for this public subnet. RT > Subnet > VPC
      - Select the Routes tab 
        - Edit (under Routes) and add 0.0.0.0/0 pointing to **IG**


-------------walled off needs repair----------------

Note: The console column for subnets shows "Auto-assign Public IP" and this should be set to
*Yes* for Spublic. Note the column title includes the term *Public IP*. The Private subnet 
should have this set to *No*. If necessary change these entries using the *Subnet Actions* 
button. 

Note: In the table of subnets there is a "Default Subnet" column. In this example both **Spublic** 
and **Sprivate**  have this set to *No* so there is no default subnet. We will change this later.  
The change is made in the routing table **RT** in **V**.

Note: In a routing table an entry reading 0.0.0.0/0 refers to the address space of the internet.


**RT** reads:  
```
10.0.0.0/16         VPC "local" 
0.0.0.0/0           NAT gateway 
```

**RTpublic** (hipaa_publicroutes) has
```
10.0.0.0/16 
0.0.0.0/0      Internet Gateway
```

We now have two RTs. hipaa_routingtable (default for the VPC in general) and for 
Spublic (hipaa_publicroutes). Notice that **RT** operates by default and **RTpublic**
supersedes this on **Spublic**. This means that new resources on **Sprivate** will
by default use **NG** which is what we want. 

VPC 0-entry points at the NAT Gateway: All internet-traffic
will route through the NAT. 

Public subnet has a custom RT which says "all non-local traffic goes out to the IG." = The Internet. 

This has precedence over the main table which sends to NAT.
By default the Private subnet will use the VPC RT to go to the NAT. 
Like one's Router at home.  This allows the private network to talk to 
the Internet and the Internet can't talk to my private subnet. 


### Part 3: Adding EC2 and S3 resources to the VPC
  
#### Building a Bastion Server

- On **V** create a public-facing Bastion Server **B**
  - **B** has only port 22 open (to support ssh) 
  - **B** uses Secure Groups on AWS to limit access to only a subset of URLs
  - **B** would be built from an AMI


m4.large running AWS Linux: Created. DO NOT USE T instances because they are not going to connect to our 
Dedicated Tenancy VPC: Not supported.

Go through all the config steps: Memory, tags, etc etc; Security group is important

Create a new security group with title hipaa_bastion_ssh_securitygroup
Description = allow ssh from anywhere
Notice in the config table "Source" is 0.0.0.0/0 which is "anywhere"; but best practice is to restrict...

IF we allowed only UW but included the UW-VPN then someone could log in from anywhere VIA the UW VPN... 


Key pair: hipaa_bastion_keypair: Generate new, download to someplace safe on **L** and Launch



- On **Sprivate** install a small Dedicated EC2 instance **E**


We are now configuring the S3 Endpoint. 
  In so doing we selected the VPC RT (not the public subnet RT; could use that)
  We are concerned about S3 traffic
  S3 Endpoint is a new type of Gateway that gives S3 access from Private subnet direct into S3 without any traverse of the internet.
  

WARNING: Kilroy: After I added the S3 Endpoint the NAT gateway entry had vanished from my VPC routing table. 
This is bad. Right now the procedure is going to be: After S3 EP go examine RT and re-add NAT gateway if it 
is not properly present. holy cow!!!!!!!!!!!!!!!


Created S3 bucket

### Part 4: Encryption

Suppose on EC2 we create an EBS volume for the PHI
So is the "comes with" EBS volume encrypted? No. Therefore: Keep data on /hipaa
Volume type = General Pupose and the size does affect IOPS; I went for 64GB

For costing and performance include this link: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html

This gets back into optimization; it does not affect our HIPAA story 

Notice the EBS volume has an AZ which **must match** the target EC2 where it is going 

Notice the volume can by encrypted with a check box; and then there is a Master Key issue. 


Using the default key technically encrypts this data at rest. So that's done. 

Working with your own set of keys would be part of risk management: Should the keys be compromised etcetera.
So there is some additional hassle and so on but some potential risk management. 

The question is: Do we want to use one key across multiple environments (the default) or created new keys for 
each new envvironment? How much hassle, etc.

ok done: hipaa_ebs_ec2_private 

Next log in to EC2 on the private subnet:
- log in to the bastion server
- used copy-paste to edit a file on the bastion called ec2_private_keypair.pem
  - I did a bad paste and was missing the -----BEGI
  - on this file we ran chmod 600 on the pem file
  - ssh -i <this file> 10.0.1.248
    - notice this ip address is in the console Description tab when highlighting the private subnet EC2 instance
  - Notice that the pem file on the bastion would immediately compromise the EC2 on the private subnet
    - That sure sucks for you

Using (sudo) fdisk to create the partition on the raw block device (fast: writing the partition table) will blow 
away anything already there. 

Now we did the simple

% aws s3 cp s3://bucket-name/keyname .

The keyname that I used was the filename that I uploaded to this S3 bucket from **L**. 
That file was pushed from **L** using the console but can also be done using the CLI. 

We are intentionally not going to encrypt the boot volume. It can be done; goes on the DD pile. 

We implement server side encryption on S3 next. 
- The file may be unencrypted on **L**
- We upload it to S3 and stipulate "encrypt this when it comes to rest in S3"
- S3 manages this
- We create an associated policy that *only* allows this type of upload
  - Therefore a not-encrypted-at-rest request will be denied

Best way is follow "S3 AWS encryption" links to http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html
Click Server-Side Encryption
Click on Amazon S3-Managed Encryption keys in the left bar to get to 
http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html

Copy the code box contents
Go to console
S3 bucket
Permissions tab
Bucket Policy button
Paste
Replace in two places: actual bucket name

PutObject command: must have server-side-encryption set to AES256 (that is the name of the encryption algorithm) 
  AND
must have server-side-encryption set to true

What about the inbound files: They must be "encrypted in transit" so we get that with an https endpoint to S3: Done. 

Transferring to the instance: scp 

Last encryption note: SSL is used by the CLI be default; so our EC2-private command 'aws s3 ... etc': 
Look at cli/latest/reference for the link on this. This means that S3 to EC2private is encrypted in transit. 
The EBS /hipaa is encrypted at rest. Done. 




### Part 5: Auditing

CloudTrail is logging the API calls to my account. Whether through the console, the CLI, the APIs directly: All logged in 
cloud trail once it is enabled. They all use the same APIs; so we log on the API calls. Logs to S3. 

**Here is the key thing: Enable cloud trail which creates a destination S3 bucket where all of the logging will go.**

Best practice is to turn on Cloud Trail in all of your regions; so you are not blind. "Either you are logging or it is gone."

Cloud Watch is more for monitoring: Performance metrics. 

In both cases there is never PHI data in the log: PRovided ss#s are not in the filenames (for example) 


And S3 has its own internal logging mechanism as well. 
- Create a new bucket hipaa-s3-access-logs with vanilla settings
- Locate the existing inbound data bucket > Properties > Logging > enable > stipulate the access logs bucket; add a tag...

This will have http traffic details; where stuff was coming from for example

#### AWS Config

Cloud trail tells you what's happening in terms of the API
AWS Config tells you what changed

Use them together to see if something is happening / happened of concern

High level set up and then more detailed is possible

Console > MAnagement > Config

Think of Config (like Cloud Trail) as account-wide, not "per resource" so tagging with the PIT is not correct.

My process was pretty default.


So now we have Cloud Trail, S3 logging and Config operating on this account. 
So as we get more sophisticated we could dig in to Cloud Watch. 















## DR
Indicate awareness; up to CISO to provide hurdles



## Risk

This section identifies points if risk and their estimated severity. Severity is described with 
two values: 'When protocol is observed' and 'When protocol is not observed'. We try to provide
examples. Furthermore there is a notion of diminishing returns: A tremendous amount of additional
effort can be incorporated in building an HCDS that provides comparatively small risk reduction.


- Log in to **B** and move **K** to **E** 
  - Observe that material encrypted 
  - Maybe instead we should be tunneling directly to **E** from **L**
- Use an AMI to create a processing EC2 **W**

  - Also with **ENC**
- Create S3 buckets 
  - **S3D** for data
  - **S3O** for output
  - **S3L** for logging
  - **S3A** for ancillary purposes (non-PHI is the intention)

  - Such S3 buckets only accept http PUT; not GET or LIST
- Create an S3 bucke **S3O** for output
- Create an S3 bucke **S3L** for logging
- Create an S3 Endpoint **S3EP_D** in **V**
- Create an S3 Endpoint **S3EP_O** in **V**
- Create an S3 Endpoint **S3EP_L** in **V**
  - "S3 buckets have a VPC Endpoint included... ensure this terminates inside the VPC"
- Create role **R** allowing **W** to read data at **S3EP** from **S3**

#### Advanced steps

- Set up a DynamoDB table to track names of uploaded files
- Set up a Lambda service 
  - Triggered by new object in bucket in the S3 input bucket
  - This Lambda service is managed using a role
- Set up an SQS Simple Queue Service **Q** 
- Create an SNS to notify me when interesting things happen


#### Logging 

- Configure everything above to log to **S3L** using CloudWatch/CloudFront

#### Creating Pseudo Data

#### Transition to operation

#### Residual notes

- Set up Ansible-assisted process for configuring and running jobs on EC2 instances
- Pushing data to S3
  - Console does not seem like a good mechanism
  - Third party apps such as Cloudberry are possible...
  - AWS CLI with scripts: Probably the most direct method
- Compute scale test: Involves setting up some substantial processing power
  - Implication is that the HCDS can intrinsically fire up EC2 instances as needed
  - Launch **W** x 5 Dedicated instances, call these **Wi**
  - Assign S3 access role 
  - Encrypted volumes 
  - S/w pre-installed (e.g. genomics pipelines)
  - Update issue: Pipeline changes, etcetera; 
- **Wi** can be pre-populated with reference data: Sheena Todhunter operational scenario
  - Assumes that a HCDS exists in perpetuity to perform some perfunctory pipeline processing
  - On **B**
    - Create SQS queue of objects in S3
    - Start a **Wi** for each message in queue...
  - Go
    - Latest pipeline... EBS Genomes... chew
    - If last instance running: Consolidate / clean-up
  - SNS topic notifies me when last instance shuts down.
    - Run Ansible script to configure **Wi** (patch, get data file names from DynamoDB table, etcetera)
    - Get Ws the Key from E
    - The Ws send an Alert through the NAT gateway to Simple Notification Service (SNS) 
    - Which uses something called SES to send an email to the effect that the system is working with PHI data 
      - Ws pull data from S3 using VPC Endpoint; thanks to the Route table
      - Ws decrypt data using HomerKey
      - Ws process their data into result files: Encrypted EBS volume. 
      - Optionally the result files are encrypted in place in the EBS volume.
  - Through **S3EP_O** the results are moved to S3.
  - **Wi** sends an Alert through the NAT gateway to SNS 
    - which uses something called SES to send another email: Done
  - **Wi** evaporates completely leaving no trace

## Procedure Log

Create a VPC **V**

![pic0001](/documentation/images/aws/hipaa0001.png)

![hipaa0002](/documentation/images/aws/hipaa0002.png)

- Use the name 'hipaa'; should be unique.
- CIDR as shown is typical.
- Dedicated Instance means: Nobody else allowed here. 

![hipaa0003](/documentation/images/aws/hipaa0003.png)

- I added a tag indicating that I originated the VPC.

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
