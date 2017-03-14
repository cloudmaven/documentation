---
title: Compute Power
keywords: cloud, introduction
last_updated: October 6, 2016
tags: [research_computing]
summary: "Compute power in the cloud"
sidebar: mydoc_sidebar
permalink: cc_compute_power.html
folder: cc
---

## Introduction
The purpose of this page is to describe in some depth the available processing power on the public cloud. 

**There is an 'effectively unlimited' pool of computers available on the public cloud, a reservoir you can
tap to address your computing tasks.**

## Links
[AWS Instance Types](https://aws.amazon.com/ec2/instance-types/)
[Azure Virtual Machine types] (https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/)

## Warnings

- ***Cloud accounts initially limit the number of virtual machines you can allocate to prevent you
from accidentally running up a huge bill. Only ask for this limit to be raised when you are certain
you know what you are doing.***

## Basic Thesis

We develop here a framework for describing and tackling large computing tasks on the cloud. 
This includes drawing a distinction between available instance types or `cloud VMs` (Virtual Machines). 
(See the cloudmaven [overview page](cc_what_is_the_cloud) and the [glossary](cc_glossary) for the basic 
terminology.) In general the more powerful the cloud VM the more it costs per hour. At the same time
it will complete a given task more quickly; so there is the potential to benchmark different instance
types to find an optimal solution. To first order you can probably skip this, however, in favor of 
simply understanding how to match your instance choice to your compute task.

Incidentally: On the AWS cloud you may cut your costs using the [Spot market](aws_spot_market.html); 
this detail is not discussed further on this page. 

Your cloud account may have a native limit to how many VMs you can engage at one time. If this
is insufficient for your work you can contact the cloud vendor and request a limit increase. This
should be granted fairly quickly but be warned: The reason that limit is in place to begin with is
to prevent you from accidentally allocating a large number of cloud VMs and thereby running up a 
large bill. If your objective is to run a large number of VMs at once you should proceed in powers 
of ten (3 to 30 to 300 to 3000) to make sure that your ensemble is behaving as you expect.

There are two extremes of large compute task, roughly speaking; which we call HPC and HTC. 
HPC stands for High Performance Computing and in a narrow definition it refers to tasks spread 
across many VMs which require inter-VM communication. The classic example is a solution to a 
computational fluid dynamics problem in which a volume is subdivided among VMs or 'nodes'. 
In this case a particular cell may evolve over one time step and must share its new boundary
conditions with another node concerned with an adjacent cell. This requires all of the nodes
to proceed in lockstep as the system evolves in time, where each tick of the clock requires a
period of inter-node communication. This is typically done using special purpose hardware such 
as *Infiniband*. (kilroy citation needed) 

On the cloud this kind of inter-node communication speed is an emerging technology. The state of the 
art is rapidly changing and (kilroy need more here) you will want to look at the cloud vendor
websites to see what is currently available. 

The other extreme for large compute tasks are those in which inter-node communication is not a
bottleneck. This is referred to as High Throughput Computing or HTC. It is also sometimes called
*embarrassingly parallel* computing, and by other euphemistic names. The positive feature of this
type of computing is that multiple tasks can be started on multiple nodes. These can run to 
completion and report back their end results. These results are ultimately collated into some
synthesis process to arrive at an end result. As an example see our 
[AWS case study on Rosetta](acs_rosetta.html).

This spectrum of **HPC** to **HTC** gives an important element of our large compute task framework. 
In the HTC case we can manage large numbers of parallel jobs using a **Scheduler** such as 
Sun Grid Engine. In principle any compute task can be completed in roughly the same amount of time
by simply allocating more nodes.  In the HPC case we have a more complex situation and therefore 
more work to do to ensure thata inter-node communication is not creating a bottleneck.
 
## Threads, vCPUs, hyperthreading, blades and all that jazz

## Machine characteristics 

### Distinction between metal and various VM configurations

### AWS view: General purpose, compute-intensive, memory-intensive, burst, others

### Azure view of things

### GPU-centric

### Top of the line VMs

## Attached drive strategies

### EBS

### EFS

### Buckets and blobs

## HPC and interconnection speed

{% include links.html %}
