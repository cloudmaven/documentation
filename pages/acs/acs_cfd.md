---
title: Computational fluid dynamics on AWS
keywords: research_computing
last_updated: October 6, 2016
tags: [research_computing, scale]
summary: "Computational fluid dynamics on the AWS cloud"
sidebar: mydoc_sidebar
permalink: acs_cfd.html
folder: acs
---

## Introduction 

## Links

## Warnings

## Start


- Create a cfncluster with a placement group

- disable hyperthreading if desired (not critical). 
  - This requires a config file and a post_install_script. (sent but may need to re-create)

- There is a cfncluster tutorial that can be helpful. (see email chain for links). 
 
- Install starccm+ on the shared volume and set up the license

- Create a snapshot of the volume (for the next cluster).
 
- create a qsub file and launch. 
  - The qsub file is created from starccm+ documentation. 
  - AWS does not generally know best practices for the individual software packages. 
  - Guessable but best to get from siemmens.
 
- number of processes requested (and hence the number of instances requested) depends on the number of gridcells in the CFD calculation. 
  - LH targets about 50,000 cells per process. 
 
- Recollection: A's cases were small so only about 72 processes are required 
  - two c4.8xlarges, with hyperthreading turned on --- four if its turned off
 
- when we went to launch the case the cluster was not working correctly. 
  - In fact, it was quite bad 
  - I checked the config file and it didn’t have placement groups so I suggested that a new cfncluster was going to be needed.
 
- Also running starccm+ with a batch or qsub file is documented in Steve’s portal (the starccm+ website). 
  - AWS does not generally have access to steve’s portal so we don’t have recommended practices for each of the software packages. 
 
- AB can walk through most of this. 

{% include links.html %}
