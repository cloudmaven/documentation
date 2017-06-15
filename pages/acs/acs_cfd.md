---
title: Computational fluid dynamics on AWS
keywords: research_computing
last_updated: June 7, 2017
tags: [research_computing, scale]
summary: "Computational fluid dynamics on the AWS cloud"
sidebar: mydoc_sidebar
permalink: acs_cfd.html
folder: acs
---

## Introduction 

## Links

## Warnings

## Procedure

- Resource tagging per HPC Club policy
  - [Link](https://cloudmaven.github.io/documentation/ccs_student_research.html)
  - **Project** tag key; value = NetID (without '@uw.edu')
  - **End_date** tag key; value = when you expect to be done with the resource
  - **Name** tag key; value = NetID_descriptive_phrase


- Central idea: Use the Spot market, do the first calculation, make sure it works, get cost


- AB can assist with getting the technical details right


- Authenticate with NetID possible but we will use IAM User for now


- Procedural
  - Create cfn cluster with placement group
    - See email chain for links
  - optional: disable hyperthreading (config file and post_install_script required)
  - install starccm+ on the shared volume, set up the license
    - A making progress on the execution issue; please send Rob confirmation this is fixed
  - create a snapshot of the volume for next cluster
  - create a qsub file and launch
    - created from starccm+ documentation; get file from Siemmens, cf email chain; pls send to Rob


- Number of processes / instance depends on number of gridcells in the CFD calc
  - LH: 50k cells per process
  - LH: 72 processes implies qty 2 c4.8xlarge with hyperthreading on; qty 4 if off
  - A revises: 9e6 cells 180 processors = 4-5 c4.8xl
  - 'existing config does not have a placement group' implies new cfncluster needed


- Obstacle
  - Insufficient space on the shared EFS drive... solution pending

- The Steve's Portal
  - This is the starccm+ website
  - batch/qsub documentation available


{% include links.html %}
