---
title: Rosetta computing at scale
keywords: research_computing, data_science
last_updated: October 6, 2016
tags: [Rosetta, scale, research_computing, AWS, organic_chemistry, data_science, research_credits, case_studies]
summary: "Rosetta peptide design studies on the AWS cloud"
sidebar: mydoc_sidebar
permalink: acs_rosetta.html
folder: acs
---

## Introduction

This page presents a success story: Massive-scale cluster computing on the Amazon Web Services public cloud. 
The computations use the **Rosetta** molecular design software to explore small protein (peptide) structures
using a fixed number of amino acids.  These protein structures (scaffolding) could be used to target 
binding sites in therapeutic medicine.


This case study shows that a *moderately large* compute task runs quickly and cost-effectively 
on the public cloud. The computing machines are maintained by AWS so no time-consuming process of 
purchasing, configuring, operating, maintaining and updating compute clusters was involved.

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


## CC*IIE Remarks

This component of the NSF-sponsored CC*IIE project looks at doing large-scale compute tasks on the public cloud. 
The primary objective is to match cost to compute by spinning up a certain number of compute instances, 
getting them to run pieces of the complete task, and then shut down quickly to minimize cost. 
We first approach this on AWS using a standard mechanism called Cloud Formation Network clustering ('cfncluster'). 
We also want to use the AWS Spot market since this cuts instance cost by up to 80% per virtual machine.
The scale of the task ran into some obstacles because the Spot market instance pool is a small subset of 
the complete AWS instance pool. We overcame this limitation using a new service from AWS called **Batch**.


### Objective and Approach

- Science objective: Explore possible structures of proteins built from a small number of amino acids
- Technical objective: Paralellize analysis software to show large-scale compute power on the public cloud

To generalize this process the following steps would be typical:

- Identify the research problem that requires large-scale computing
- Configure the AWS User account
- Configure the execution software and the data structure 
- Configure **cfncluster**, **EnginFrame** or **Batch** to run the job at scale on the AWS Spot market
- Recover the results and close the compute infrastructure


### Solution


- The Spot market proved to have limited capacity; that is, a limited number of available instances
  - This is due to the two-tier resource allocation: Regions on a high level and Availability Zones on the sub-level
  - cfncluster only works within one Availability Zone (AZ)
  - The number of Spot instances within a single AZ was insufficient
  - Desired capacity: On the order of 200 [c4.8xlarge](https://aws.amazon.com/ec2/instance-types/) compute instances
- The project migrated to the [**AWS Batch**](http://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) 
service to allocate Spot market instances across Availability Zones within a single Region


### Results
- This **Batch** solution resulted in 160 c4.8xlarge instances running for 53 hours on a single compute task
producing 5 million positive structural results; at a fraction of the On Demand rate
- The Rosetta compute produced 5 million peptide structures using 313,000 virtual CPU hours at a cost of $3477.
- The results are documented below and in considerable detail [at this wiki](https://github.com/cloudmaven/Rosetta/wiki).
- Key numbers 
  - 53: wall clock hours required to complete calculations
    - 391: Wall clock hours needed to complete the same task on the Researcher's available on-premise HPC resources
    - $800,000: Cost for on-premise hardware capable of producing this result in 53 hours
    - 230: The number of such calculations that could be run for this amount
  - 164: Number of C4.8xlarge EC2 instances allocated on average from the AWS Spot market (max 200)
    - 5904: Equivalent number of vCPUs (virtual processors)
    - $0.40: Spot market cost per instance-hour
      - showed no significant cost variation over the task duration, nor impact on market price
      - $0.012 per vCPU-hour. Careful optimization saved more than $600 over other instance choices
    - $3477: Task compute cost (covered by an AWS research credit grant)
  - 5.2 million: Number of positive results (peptide scaffold structures)



## Related Links


- [Peptide design paper: Gaurav Bhardwaj and others](http://www.nature.com/nature/journal/v538/n7625/full/nature19791.html)
- [AWS Batch service](https://aws.amazon.com/batch/)
- [Baker Lab Rosetta software suite](https://www.bakerlab.org)
- [Rosetta (from COMOTION)](https://els.comotion.uw.edu/express_license_technologies/rosetta)
- [Procedural Documentation](https://github.com/cloudmaven/Rosetta/wiki)
- [Rosetta Commons website](https://www.rosettacommons.org/docs/latest/Home)
- [Rosetta Commons 'Scripts'](https://www.rosettacommons.org/docs/latest/scripting_documentation/RosettaScripts/RosettaScripts)
- [Compiling Rosetta](https://www.rosettacommons.org/docs/latest/build_documentation/Build-Documentation)


## Remark on **AWS cfncluster** in relation to **AWS Batch**


- The AWS Spot instance pool is smaller in capacity than the AWS On Demand pool and typically
features much better cost-per-hour rates.  We found that this smaller pool can constrain compute 
scale; so a major part of this effort was determining how to overcome this constraints. 
We did so via choice of region combined with adoption of the Batch service to allocate tasks 
across AWS availability zones (AZs) within that region.  
For more detail please refer to our [Rosetta wiki](https://github.com/cloudmaven/Rosetta/wiki).



## Science background


AWS research credits provided for this work have contributed significantly to the challenge 
of large scale sampling of peptide scaffolds -- stable structures that would be the basis for 
developing new therapeutics. This section is a brief sketch of the scientific basis. 


On DNA: Human DNA consists of 3 billion base molecules arranged in pairs as rungs of a helical ladder. 
The base pair sequence records how to construct proteins in the following manner:  Each base (nucleotide) 
can have one of four values abbreviated A, C, G, or T.  Three bases in a row can be thought of as three 
digits in base-4; for example AAG or TCA. That is, this triple is a number from 0 to 63.  These 
triples map to one of 20 left-handed amino acids (with some values degenerate and others 
'not assigned'.)


On amino acides: Common to all life on earth these 20 naturally occurring molecules are the building 
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
(HPC) which includes the compute task described in this case study.  The public cloud represents an 
alternative approach where low/falling cloud costs, increasing convenience, read-to-use services and outsourced 
system administration are factors to consider. At what point is cloud computing cost-equivalent to 
on-premise computing?  Here are two views of the break-even concept.


### Hard Break-even


Take the lifespan of a purchased computer to be three years.  In this case study the compute task ran 
for 53 hours on the AWS cloud and cost $3500. When an equivalent single computer costing $3500 requires 
3 years to complete the same task we could say that cloud cost has reached parity with on-premise 
cost. It is worth noting however that the on-premise solution takes 500 times longer to finish the 
computation.  We estimate the time to complete the compute task described here would be 246 days which
is 849 days sooner than the hard break-even of three years.  This means that a head-to-head comparison
with 100% CPU utilization for three years favors the on premise computer today. It is when the
purchased computer is not being used at 100% capacity that the cloud cost begins to be comparable. 


### Soft Break-even


Soft break-even brings wall-clock time and other factors into consideration. At what point does waiting 
for compute tasks hinder the researcher's progress? In this case study the Researcher is fortunate to have 
access to an on-premise cluster that would complete the same task in two weeks. On that cluster the completion 
time scales with the size of the computation: A four-times-larger compute task would require two months
whereas on the public cloud time to complete is unchanged: The larger task will still only require 
wall clock time on the order of 48 hours. 

This matter of personal or wall-clock time is *prima facia* a strong argument for working when 
possible on a cloud platform. We note that cloud vendor [*research credits*](p_research_credits.html) 
enable a Researcher to explore this benefit with relatively low financial entry risk. 


A final remark on human versus computer time: If human time becomes a factor in computing then a
suitable question might be: How many computers do I need to purchase to reach an acceptable human 
or 'wall clock' time for my computations to run? Again if this computation can be followed by 
another and another in succession: That is 100% CPU use and it justifies purchasing dedicated 
hardware. However the other side of the coin is that a research team may not have this level of
processing requirement or they may not have this level of funding. 


## Some contextual terms and concepts for large computing tasks on AWS


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

- T2 Micro: An EC2 instance that costs very little and can configure the heavy processing (cost saving strategy).

- Key Pair: A digital signature contained as a file that grants ssh access to an EC2 instance without user/password login
  - Crucial concept: Never include Key Pair files in GitHub repositories; this can cost you tens of thousands of dollars

As noted: For more on large compute tasks on AWS please refer to the [Rosetta wiki](https://github.com/cloudmaven/Rosetta/wiki)

{% include links.html %}
