---
title: Rosetta scale computing case study
keywords: research_computing, data_science
last_updated: October 6, 2016
tags: [Rosetta, scale, research_computing, AWS, organic_chemistry, data_science, research_credits, case_studies]
summary: "Rosetta peptide design studies on the AWS cloud"
sidebar: mydoc_sidebar
permalink: acs_rosetta.html
folder: acs
---

## Introduction

This page presents a research-to-cloud success: a case study in which powerful 
molecular design software is run at large scale on the AWS public cloud to explore
the possible scaffolding-like structures of small proteins called peptides.  This new 
approach to protein design rapidly generates encyclopedic results that could be used 
to create new therapeutic medicines.

The study shows that a *moderately large* compute task runs quickly and cost-effectively 
on the public cloud. This result contrasts with the traditional time-consuming process 
of purchasing, configuring, operating, maintaining and updating a compute cluster which
in turn would compute more slowly.

This success on the AWS public cloud uses key technologies and methods that we describe
in further detail below. The methods described are applicable to any research computing 
task that can be broken into many independent parallel computational threads. 
Components include:

- The [Baker Lab Rosetta software suite](https://www.bakerlab.org)
- Powerful [EC2 compute instances](https://aws.amazon.com/ec2)
- The [AWS Spot market](aws_spot_market.html)i
- [Optimization analysis](https://aws.amazon.com/ec2/pricing/on-demand/) of cloud computing instance types
- The AWS [**Batch**](https://aws.amazon.com/batch/) service
- The [AWS Research Credit Grant program](https://aws.amazon.com/grants/)

## Links

- [Peptide design paper published by the Researcher](http://www.nature.com/nature/journal/v538/n7625/full/nature19791.html)
- [AWS Batch service](https://aws.amazon.com/batch/)
- [Baker Lab Rosetta software suite](https://www.bakerlab.org)
- [Rosetta (from COMOTION)](https://els.comotion.uw.edu/express_license_technologies/rosetta)


- [Procedural Documentation (temporary wiki)](https://github.com/robfatland/Rosetta/wiki)


## Preliminary Remarks

- The AWS Spot instance pool is smaller in capacity than the AWS On Demand pool and typically
features much better cost-per-hour rates.  We found that this smaller pool can constrain compute 
scale in default usage patterns; so a major part of this effort was determining how to overcome 
these constraints. We did so via choice of region combined with adoption of the Batch service 
to allocate tasks across AWS availability zones (AZs) within that region. 
This procedure is described in detail below. 

- This work was directed by the first author of the above-cited
[paper on peptide design](http://www.nature.com/nature/journal/v538/n7625/full/nature19791.html),
Gaurav Bhardwaj.  He is herein referred to as **The Researcher**.

## Overview

- Objectives 
  - Explore possible structures of proteins built from a small number of amino acids
  - Paralellize the analysis software on the public cloud
  - Begin to demonstrate the compute power of the public cloud
- Means: The Rosetta peptide design software implemented on the AWS public cloud
- Key numbers from the main compute task
  - 53: wall clock hours required to complete calculations
    - 391: Hours needed to complete the same compute task on the Researcher's available HPC resources (Hyak)
    - $800,000: Cost for on-premise hardware capable of producing this result in 53 hours
    - 230: The number of these analysis tasks that could be run on AWS for $800,000
  - 164: Number of C4.8xlarge EC2 instances allocated on average from the AWS Spot market (max 200)
    - 5904: Equivalent number of vCPUs (virtual processors)
    - $0.40: Spot market cost per instance-hour
      - showed no significant cost variation over the task duration, nor impact on market price
      - $0.012 per vCPU-hour. Optimization saved > $600 over other instance choices
    - $3400: Task compute cost (covered by an AWS research credit grant)
  - 5.2 million: Number of positive results

## Science background

AWS research credits provided for this work have contributed significantly to the challenge 
of large scale sampling of peptide scaffolds -- stable structures that would be the basis for 
developing new therapeutics. This section is a brief sketch of the scientific basis. 

Common to all life on earth there are 20 naturally occurring amino acids that are the building 
blocks of proteins. Smaller chains of such amino acids are called peptides. Once a particular sequence
of amino acids is bonded together end-to-end and released its rotational degrees of freedom may 
permit it to fold up into an energetically favorable structure. This structure may in turn serve 
some chemical/biological function. The Rosetta software can analyze the manner of folding thereby 
connecting a hypothetical amino acid sequence to a protein structure, also called a *scaffold*.

The practical challenge is the matching of such structures to naturally occuring geometries of 
interest within the organism's molecular landscape, often described using a 'lock and key' 
analogy: A given therapeutic molecule could be designed to fit a particular binding site 
for example on a cell wall, thereby either enhancing or restricting some metabolic process
at that location.  One ultimate aim then would be to comprehensively sample all possible shapes 
such that a large number of highly stable 'keys' are ready to be molded or slightly re-configured 
into any desired shape.

The compute task described here samples the space of possible peptide structures. These structures 
must prove to be feasible and stable before they can be subjected to further analysis. Ultimately 
a design of interest (from the computation) may be synthesized as an actual physical protein in 
the laboratory (a fascinating process) which would then be subjected to chemical analysis to 
validate that its structure is indeed as predicted by the software.

## Cost tradeoffs

Purchasing and maintaining dedicated hardware is the traditional approach to high performance computing
(HPC) such as the work described here. This approach suffers from two limitations

The public cloud represents an alternative approach wherein falling costs, increasing convenience, 
read-to-use services and outsourced system administration are factors in its favor. At what point 
is cloud computing cost-equivalent to on-premise computing?  We suggest two views of the 
break-even point.

### Hard Break-even

Take the lifespan of a purchased computer to be three years.  In this case study the compute task ran 
for 53 hours on the AWS cloud and cost $3400. When an equivalent single computer costing $3400 requires 
3 years to complete the same task we could say that cloud cost has reached parity with on-premise 
cost. It is worth noting however that the on-premise solution takes 500 times longer to finish the 
computation.  We calculate that the time to complete the compute task would be 246 days today, 
849 days sooner than the hard break-even of three years. 

### Soft Break-even

Soft break-even brings wall-clock time into consideration. At what point does waiting for compute tasks
hinder the researcher's progress? In this case study the Researcher is fortunate to have access to an
on-premise cluster that would complete the same task in two weeks. On that cluster the completion time 
scales with the size of the computation: A four-times-larger compute task would require two months
whereas on the public cloud time to complete is unchanged: The larger task will still only require 
wall clock time on the order of 48 hours. 

This matter of personal or wall-clock time is *prima facia* a strong argument for working when 
possible on a cloud platform. We note that cloud vendor [*research credits*](p_research_credits.html) 
enable a Researcher to explore this benefit with relatively low financial entry risk. 

## Key Terminology 

- Batch service: An AWS service suited to larger-scale resource allocation on the AWS Spot market
- cfncluster service: Abbreviated term for *Cloud Formation Network cluster*, an association of technologies
that facilitate engaging many EC2 instances for parallel processing tasks in coordination with a Scheduler.
- Sun Grid Engine (SGE): A Scheduler commonly used on AWS that coordinates with *cfncluster*
- Configuration Instance: A small EC2 instance used to configure and run *cfncluster*
- Master: An AWS EC2 instance (with EBS volume attached) running as the Master node of a *cfncluster* 
under the SGE Scheduler
- Worker: An AWS EC2 instance (for example from the Spot market pool) executing a large compute task

- Optimization benchmarking: Studying the consequences of choice of EC2 instance, task loading, other configuration settings. 
- Time optimization: Analysis of instances and settings to complete a given Job in minimal time.
- Cost optimization: Analysis of instances and settings to complete a given Job at lowest cost in USD.

## kilroy stack (open issues)

- AMI story
- The cfncluster terminology is heavy; Batch is light
- Elaborate on IAM User account permissions as key for cfncluster operations
  - blanket 'admin' is over-sufficient and backing off of this should be stated
- Remarks on the wiki
  - "In what follows we try to emphasize what you *do* need to change on the forms; hence 
    if there is no comment you should leave the default value as-is."
  - S3 region = US Standard (there is no N. Virginia) should be called out
  - Elastic ip: 34.205.126.203
  - On create VPC page: On Wizard setup: Do not click "Add Endpoint"
  - Must modify the CIDR block description in HIPAA and link to that (actually it belongs elsewhere...)
  - Page 4: At top: Motivate "what kind of EC2 do we start with?"
    - Point out that the Community AMI describes capabilities, not EC2 instance type: Separate concepts
    - In particular we must carefully elaborate: The EC2 instance in the next step (c4.4xlarge) is a
      model for building an AMI; and this AMI may subsequently be pulled into a *different* EC2 type
      such as a c4.8xlarge. This is ok: The scaling to machine power is automated.
  - Page 4: Selection is Ubuntu and Docker 16.04; other features like Kubernetes does not factor in
  - The EC2 launch key pair section should be beefed up with references to the GitHub warning and so on
  - Emph on the prefix ubuntu at

## (fossil) cfncluster / Rosetta configuration steps

The Rosetta work by Srihari Vignesh is currently captured 
at [this wiki](https://github.com/Sriharivignesh/Rosetta-Protein-Folding-Project/wiki).

The remarks on tracing the wiki steps are up above in the kilroy stack section.

The following content is from earlier, i.e. it is residual from earlier progress focused
on using cfncluster.

See [this page](acs_rosetta.html) for the screen captures: All from console and terminal.

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
aws_access_key_id = ...etc
aws_secret_access_key = ...etc

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

For 'key_name' enter the key pair file name associated with an IAM User identity 
without any extensions.

Check that max_queue_size is set to 300. (The original was a value of 2 which is too small 
but a safe starting value.) This is the maximum number of Spot market instances that may
be allocated. 

The access keys above are redacted for reasons of form: Although they could be included we
blank out such information to encourage awareness of security issues. These access keys are
IAM User credentials supplied from an IAM User account. The IAM User must in turn have adequate 
permissions to carry out cfncluster operations. 

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

After **cfncluster create** finishes log in to Master and use **qsub** to submit 
the Rosetta job. This creates a job queue: A long list of processing tasks (for example
100,000) which are to be executed. These jobs will be scheduled one by one: Assigned to 
Worker nodes. 

Each Worker node has a number of 'virtual CPUs' available for running Rosetta jobs in 
parallel. These are compute-intensive jobs. Each may complete in a matter of a few 
minutes.  The large number of jobs is typical from required sample density in a 
Monte Carlo task. 

kilroy left off here
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
