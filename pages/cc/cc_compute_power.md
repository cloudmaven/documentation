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

This page describes available processing power options on the public cloud. The basic rate per hour is
taken to be *on demand* meaning that once you secure the machine you keep it for as long as you like. 
There are also pre-emptible instances which can be taken out of your control on short notice. These are
available in lower quantity and at considerably reduced cost (40% to 20% or less of the on-demand rate typically.)


## Links

[AWS Instance Types](https://aws.amazon.com/ec2/instance-types/)
[Azure Virtual Machine types] (https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/)


## Basic Thesis


On cost: The more powerful the cloud VM the more it costs per hour; and obviously it will complete a given task 
more quickly; so there is the potential to benchmark different instance types to optimize.  To first order 
however one can take them to be cost-equivalent and simply work empirically by timing your compute tasks. 


On limits and runaway cost: Contact your cloud vendor and request a limit increase if you are unable to
get the number of machines at once that you need. A limit is initially in place
to prevent you from running up a huge bill accidentally via a typo in a configuration file. If for example
your script requests 20 machines but you type '200' you could find yourself spending thousands of dollars
per hour. Another good way to incur these kinds of accidental charges is to allow your access keys to 
wind up on GitHub. So there are some pitfalls in using the cloud without knowing what you are doing; 
and there is consequently a learning curve.  The first rule is 'always test at small scale before scaling
up'. The second rule is 'know how to operate without putting your account access at risk of theft.'


On computing scale we do enjoy sharing this [AWS case study using the Rosetta protein folding software](acs_rosetta.html).

 
## GPU-based cloud instances

Using a very coarse comparative of $/GPU/hour on V100s we get AWS and Azure both $3.06, Google $2.76. 
Preemptible costs are $0.80 to $0.94/GPU/hour, again no panic but Google is slightly cheaper. Not all 
GPU-capable instances are represented here; there are older generation units that run comparatively less. 
And of course these data are subject to change. 


|Vendor|Name|$/h|Description                                                                                      |
|:---|:---|:-------------:|:--------------------------------------------------------------------------------------|
| AWS | p3.2xl   | 3.06 (1.36) | 4 core E5-2686 v4; 1 V100 GPU x (5120 CUDA + 640 Tensor cores) |
|        | p3.8xl   |12.24 (3.77) | 16 core E5-2686 v4; 4 V100 GPU x (5120 CUDA + 640 Tensor cores) |
|        | p3.16xl  |24.48 (7.47) | 32 core E5-2686 v4; 8 V100 GPU x (5120 CUDA + 640 Tensor cores) |
|        | g3.4xl   | 1.14 (0.35) | 8 core E5-2686 v4; 1 M60 GPU x (2048 cores, 8 GiB video memory) |
|        | g3.8xl   | 2.28 (0.68) | 16 core E5-2686 v4; 2 M60 GPU x (2048 cores, 8 GiB video memory) |
|        | g3.16xl  | 4.56 (1.37) | 32 core E5-2686 v4; 4 M60 GPU x (2048 cores, 8 GiB video memory) |
|        | g3s.xl   | 0.75 (.23) |  2 core E5-2686 v4; 1 M60 GPU x (2048 cores, 8 GiB video memory) |
| Azure | NC6      | 0.90 | 6 core 1 K80 GPU |
|        | NC12     | 1.80 | 12 core 2 K80 GPU |
|        | NC24     | 3.60 | 24 core 4 K80 GPU |
|        | NC24r    | 3.96 | 24 core 4 K80 GPU with low latency high throughput network interface |
|        | NC6 v3   | 3.06 | 6 core 1 V100 GPU |
|        | NC12 v3  | 6.12 | 12 core 2 V100 GPU |
|        | NC24 v3  |12.24 | 24 core 4 V100 GPU |
|        | NC24r v3 |13.47 | 24 core 4 V100 GPU with low latency high throughput network interface |
| Google | 1 GPU    |2.76 (.80)| 4 core, 1 GPU V100 | 
|        | 2 GPU    |5.52 (1.60)| 8 core, 2 GPU V100 | 
|        | 4 GPU    |11.03 (3.20)| 16 core, 4 GPU V100 | 
|        | 8 GPU    |22.07 (6.40)| 32 core, 8 GPU V100 | 


#### Microsoft Azure notes


- Azure has preemptible instances called 'Low-Priority VM' available through Azure 
Batch Service; but I did get cost estimates here. It is safe to assume they are comparable to AWS. 
- More information needed on memory / RAM / CPU make and model


#### Google Cloud Platform notes


- Cost in parentheses is the preemptible rate
- GCP instances have a base cost and you then pay a premium ($2.48 ($0.74)) per GPU attached, up to 8
- vCPUs as AWS; see note below
- More information needed on memory / RAM / CPU make and model


#### AWS notes


- AWS uses 'virtual CPUs' or vCPU as a metric = 2 x number of cores
- Rates shown are for the Linux operating system. Windows OS typically costs more.
- Parenthetic costs are preemptible instance Spot pricing: Oregon, Nov 1 2018
- p3 instances use V100 GPUs and Xeon E5-2686 v4 (Broadwell) processors; NVLink for GPU-GPU communication
- p2 instances (not listed in the table above) use K80 GPUs and Xeon E5-2686 v4s; GPUDirect for GPU-GPU communication
- g3 instances use NVIDIA Tesla M60 GPUS and Xeon E5-2686 v4 (Broadwell) processors


## Topics for further elaboration


- Threads, vCPUs, hyperthreading, blades...
- Machine characteristics 
- Distinction between metal and various VM configurations
- Testing guidelines
- Overview of types and categories by vendor


{% include links.html %}
