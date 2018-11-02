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

A comparison of $/GPU/hour on V100s gives preemptible rates of .93/.61/.84 dollars per GPU per hour
for AWS, Azure and Google respectively. The on-demand rates are respectively 3.06/3.06/2.95 dollars per GPU per hour.
These feature the current generation: NVIDIA Tesla V100 GPUs.  Prior-generation GPUs (P100, P4, K80, M60) are also available
at commensurately lower rates.  These data are subject to change. 


Note that data for Tensorflow Processing Units (TPUs) are still pending; available only 


### Summary for high-end instances, 3 cloud providers


|Vendor|Instance|$/GPU/hr preemptible|$/GPU/hr on-demand|Description|
|:----|:---|:---:|:---:|:---|
|AWS|p3.16xlg|0.93|3.06|32 core, V100 GPUs x 8|
|Azure|NC24 v3|0.61|3.06|24 core, V100 GPUs x 4|
|Google|n1-highmem-64|0.84|2.95|32 core, V100 GPUs x 8|


### Cost per hour (notice these prices are **not** scaled by number of GPUs)


|Vendor|Instance|$/hr preemptible|$/hr on-demand|Description|
|:---|:---|:---:|:---:|:-----------------|
| AWS | p3.2xl   | 1.36 | 3.06| 4 core E5-2686 v4; 1 V100 GPU x (5120 CUDA + 640 Tensor cores) |
|     | p3.8xl   | 3.77 |12.24| 16 core E5-2686 v4; 4 V100 GPU x (5120 CUDA + 640 Tensor cores) |
|     | p3.16xl  | 7.47 |24.48| 32 core E5-2686 v4; 8 V100 GPU x (5120 CUDA + 640 Tensor cores) |
|     | g3.4xl   | 0.35 | 1.14| 8 core E5-2686 v4; 1 M60 GPU x (2048 cores, 8 GiB video memory) |
|     | g3.8xl   | 0.68 | 2.28| 16 core E5-2686 v4; 2 M60 GPU x (2048 cores, 8 GiB video memory) |
|     | g3.16xl  | 1.37 | 4.56| 32 core E5-2686 v4; 4 M60 GPU x (2048 cores, 8 GiB video memory) |
|     | g3s.xl   | 0.23 | 0.75|  2 core E5-2686 v4; 1 M60 GPU x (2048 cores, 8 GiB video memory) |
| Azure | NC6      |0.18|  0.90 | 6 core 1 K80 GPU  |
|       | NC12     |0.36|  1.80 | 12 core 2 K80 GPU |
|       | NC24     |0.72|  3.60 | 24 core 4 K80 GPU |
|       | NC24r    |0.79|  3.96 | 24 core 4 K80 GPU with low latency high throughput network interface |
|       | NC6 v3   |0.61|  3.06 | 6 core 1 V100 GPU  |
|       | NC12 v3  |1.22|  6.12 | 12 core 2 V100 GPU |
|       | NC24 v3  |2.45| 12.24 | 24 core 4 V100 GPU |
|       | NC24r v3 |2.63| 13.47 | 24 core 4 V100 GPU with low latency high throughput network interface |
| Google |n1-highmem-8 |0.84| 2.95|  4 core, 1 GPU V100 | 
|        |n1-highmem-16|1.68| 5.91|  8 core, 2 GPU V100 | 
|        |n1-highmem-32|3.36|11.81| 16 core, 4 GPU V100 | 
|        |n1-highmem-64|6.72|23.63| 32 core, 8 GPU V100 | 


#### General notes


- Rates shown are for Linux. Windows users might find Azure pricing advantageous.


#### Microsoft Azure notes


- Azure preemptible instances are 'Low-Priority VMs' available through Azure Batch Service


#### Google Cloud Platform notes


- Add: Instance base rate (e.g. $0.10 / hr preemptible) plus per-GPU rate (e.g. $0.74 per Tesla V100 per hour preemptible)
- vCPUs are counted as with AWS: Number of cores x 2 hyperthreads each


#### AWS notes


- AWS uses 'virtual CPUs' or vCPU as a metric = 2 x number of cores via hyperthread
- Preemptible prices (AWS Spot instances) subject to variability 
- p3 instances use V100 GPUs and Xeon E5-2686 v4 (Broadwell) processors; NVLink for GPU-GPU communication
- p2 instances (not listed in the table above) use K80 GPUs and Xeon E5-2686 v4s; GPUDirect for GPU-GPU communication
- g3 instances use NVIDIA Tesla M60 GPUS and Xeon E5-2686 v4 (Broadwell) processors


## Topics for further elaboration


- TPUs available from Google: How much do they run, performance comparison, development platform comparison
- Threads, vCPUs, hyperthreading, blades...
- Machine characteristics 
- Distinction between metal and various VM configurations
- Testing guidelines
- Overview of types and categories by vendor


{% include links.html %}
