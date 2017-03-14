---
title: Rosetta scale computing case study
keywords: research_computing
last_updated: October 6, 2016
tags: [Rosetta, scale, research_computing, AWS, organic_chemistry,data_science,research_credits, case_studies]
summary: "Rosetta molecular engineering software on the AWS cloud"
sidebar: mydoc_sidebar
permalink: acs_rosetta.html
folder: acs
---

## Introduction

The purpose of this page is to step through the implentation and execution of a Rosetta task 
on the AWS public cloud using pre-built Amazon Machine Images (AMIs). 

## Links

## Warnings

## Roadmap

- cfncluster: Cloud Formation Network cluster, an association of EC2 instances and software to carry out a parallel processing task in coordination with a Scheduler.
- Sun Grid Engine (SGE): The Scheduler we use in coordination with cfncluster in this case study. 
- Configuration Instance: A small AWS EC2 instance (T2) used to set up and run the cfncluster.
- Master: An AWS EC2 instance with necessary EBS volume attached running as the Master node of a cfncluster under SGE.
- Worker: An AWS EC2 Spot market instance of some type (e.g. c3.8xlarge is the powerful option) that is executing tasks on virtual CPUs / threads. 
- Rosetta AMI: The machine image used to spin up one Master and many Worker nodes
- Task: One run of Rosetta requiring (typically) 8 minutes on a fairly powerful machine; compute intensive, reports back (a small data volume of) results to the Master node. 
- Small Test 1: 300 nodes running about 16 parallel tasks at 6 minutes each using a static random number seed, i.e. each task uses the same seed; identical calculations.
- Small Test 2: Same as Small Test 1 but with unique random number seeds generated for each task. Tasks now require on average 8 minutes on c3.8xlarge and some may run much longer.
- Big Test: Specifics to be determined; possibly several Small-Test-2 runs in parallel for example; must be scientifically useful; run time <= 2 hours; larger number of EC2 Worker instances.
- Optimization benchmarking: Studying the consequences of choice of EC2 instance, task loading, other configuration settings. 
- Time optimization: Analysis of instances and settings to complete a given Job in minimal time.
- Cost optimization: Analysis of instances and settings to complete a given Job at lowest cost in USD.

Update
- Implementation done, Small Test 1 concluding. 
- Small Test 2 is pending. 
- Big Test to follow. 


## Set up

Log in to your IAM User account on AWS. 

Start an EC2 instance; using a T2 Micro will work well; they cost very little and this instance will
be used to configure the heavy processing so it does not need processing power.

![acs_rosetta0001](/documentation/images/acs/acs_rosetta0001.png)


Now let's suppose someone has come here in advance and set up the AMI that I wish to use. 
That is the case for now; and we will generalize to an arbitrary AWS User in the future. Here we go. 

![acs_rosetta0002](/documentation/images/acs/acs_rosetta0002.png)
![acs_rosetta0003](/documentation/images/acs/acs_rosetta0003.png)

When I hit Launch I have a conversation about choice of Key Pair

![acs_rosetta0004](/documentation/images/acs/acs_rosetta0004.png)

Rather than use something existing I'm going to simply create and download a new key pair. 

![acs_rosetta0005](/documentation/images/acs/acs_rosetta0005.png)
![acs_rosetta0006](/documentation/images/acs/acs_rosetta0006.png)

Following the usual procedure to log in using PuTTY we quickly arrive at

![acs_rosetta0007](/documentation/images/acs/acs_rosetta0007.png)

We now proceed in the Linux operating system on this cfncluster control instance. It will 
be used to create the execution environment on other EC2 instances, specifically instances running on the AWS Spot market.

```
% sudo pip install cfncluster
```

This creates (in my home directory) a directory called .cfncluster. 
I can verify that this installed by running 

```
% cfncluster
```

The output confirms that the command is present (installed). 

Next we build a *config* file in the .cfncluster directory with the following contents: 

```
[aws]
aws_region_name = us-west-2
aws_access_key_id = ### REDACTED ###
aws_secret_access_key =  ### REDACTED ###

[global]
update_check = true
sanity_check = true
cluster_template = rosetta_cfn_test

[cluster rosetta_cfn_test]
vpc_settings = public
key_name = my_IAM_User_keypair_filename_with_no_extension
compute_instance_type = c4.8xlarge
master_instance_type = c4.8xlarge
initial_queue_size = 2
max_queue_size = 300
maintain_initial_size = false
scheduler = sge
base_os = ubuntu1604
custom_ami = ami-11df6571
master_root_volume_size = 30
compute_root_volume_size = 30
cluster_type = spot
spot_price = 0.72
scaling_settings = custom

[vpc public]
master_subnet_id = subnet-4a37992d
compute_subnet_id = subnet-4b37992c
vpc_id = vpc-5c891c3b

[scaling custom]
scaling_cooldown = 20
```

Notice that for 'key_name' you must enter the key pair file name 
associated with your IAM User identity without any extensions.

Notice and check that max_queue_size is set to 300. (The original was a value of 2 
which is not correct (but safe).) This is the maximum number of spot instances we will 
be spinning up in the subsequent processing. 

Notice that the access keys are redacted. These are IAM User credentials. You must supply these 
from an IAM User account (perhaps your own). This IAM User must have adequate permissions. 
kilroy these should be stated. kilroy whether blanket 'admin' is sufficient should be made clear.

Look at the file **job_submission.sh**. There is a command argument *-nstruct* with a subsequent
integer value such as 1000. This file will not be put to use on this machine; but will be copied to
the Master machine shortly. Once there the *nstruct* parameter will have important implications 
for the Rosetta processing task; so we will revisit this before starting that task. 

(The *nstruct* number is a number of random seeds that the Rosetta job will create. 
Kilroy this needs further elaboration. We want to ensure that the nstruct value is large enough 
that the number of jobs we launch (number of instances x jobs per instance) does not exceed the 
number of random seeds we have available. Perhaps this number could be set to 1 million? 

Next we will use the cfncluster meta-command to 'create' a cfncluster: Three AWS instances
that act as the starting point for the Rosetta processing run.

```
$ cfncluster create rosetta-identifier
```

Note that 'rosetta-identifier' can be any recognizable indentification string.

We expect the *create* task to take a few minutes. 

### What is **cfncluster create** doing? 

First it is going to create a trackable presence on the AWS console under Cloud Formation. 
Let's take a look at that by finding Cloud Formation on the AWS Console.

![acs_rosetta0008](/documentation/images/acs/acs_rosetta0008.png)

Here is the general outline of what is happening:

The **cfncluster create** command is building three EC2 instances from one existing AMI with some 
additional configuration to follow. The first EC2 instance will be a Master instance and the
other two are Worker instances. All three machines will be on standby once they start; they have 
no work to do yet. 

cfncluster builds all three instances according to the rules we set up in the config file; and 
the build will also include the job_submission.sh file that we noted above has an 'nstruct' 
parameter. 

**cfncluster create** will install Sun Grid Engine on the Master Server. It will run some 
other boilerplate scripts taken from S3 storage.  The Rosetta configuration files are pre-loaded 
on the AMI.  The Workers, while they are not doing any work yet, are ready to go as they have the 
Rosetta software and the Rosetta configuration files pre-installed.  


### Starting Rosetta

After **cfncluster create** finishes we will log in to the Master and use the qsub command to submit 
the Rosetta job. This will in turn create a job queue: A long list of processing tasks (perhaps 
100,000 of them). These jobs will be schedule one by one, that is: Assigned to the Worker nodes. 

Each Worker node will have some number of 'virtual CPUs' available for running Rosetta jobs in 
parallel. These are compute-intensive jobs and each may complete in a matter of a few minutes. 
The number of jobs is given as 100,000 as this (for our initial implementation) is due to a 
sufficient sample density in a Monte Carlo simulation. 

While we may run 100,000 jobs these may be distributed across perhaps only 300 Workers. These 
Workers will (for this example) be powerful machines, each with the capacity to run 36 jobs 
simultaneously. The jobs we expect to take about 8 minutes each; so in the course of an hour we 
expect about 7 x 36 or 252 jobs to run. Multiplying this by 300 we expect 75600 jobs to complete
in an hour. 

Since the two initial Workers will be insufficient to process the job list we have a mechanism
for increasing the number of Workers. When there are jobs waiting and no Workers available 
the SGE scheduler request that cfncluster spin up more instances. Cfncluster will do so until it 
hits the maximum limit (300) that we specified in the *config* file. 

These 300 Workers will each process multiple threads/tasks.  When the job queue is empty the Workers 
will be terminated; but not until after they have streamed their results back to the Master. 

{% include links.html %}
