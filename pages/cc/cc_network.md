---
title: Network 
keywords: cloud, introduction
last_updated: October 6, 2016
tags: [research_computing]
summary: "Cloud computing network connection"
sidebar: mydoc_sidebar
permalink: cc_network.html
folder: cc
---


## Introduction


This page documents network connection process, speed, details and benchmarks between our parent organization 
and public cloud vendors. That is: If you are a Researcher at UW and you need speed to connect to the cloud:
Start here. 


## Links
- [cloudmaven](http://cloudmaven.org)
- [self-reference](cc_network.html)


## Warnings


- ***We estabilsh both standard and accelerated network connection options here; the latter will probably
require installing some hardware and we indicate cost on the order of magnitude scale.***


## Glossary


- 10gig
- D528
- IDF
- fiber
- Cat6A copper


## AWS Case Study


This case study supports multiple light-sheet microscopes that generate a lot of data in a short
amount of time. Currently in fact 1GB/sec but the new generation will be 8GB/sec or about 5TB in
10 minutes.  We need to get that data onto the AWS cloud in near-real-time. 


We have two light sheet microscope locations: UW Health Sciences D-Wing (HSD) and the Aeronautical Engineering 
Building AER. Our objective is to support up to 10 Gigabits per second transfer rate, herein '10Gig'. 


Health Sciences D Wing (HSD) is ready to support 10gig: D528 is cabled to the telco closet / IDF in 
that area. Needed: Station cabling to D528 (longest lead-time item); and will this be copper or fiber?
With this information the Communications Infrastructure team works up an estimate and timeline. With
the cable in place the hardware follows quickly.  AER is more complex: A site visit is necessary to
determine whether there is room for the necessary hardware; again in an IDF / telco closet. 


The cable path is as follows, total cost being O($10k). For items that must be purchased by the
research team we pre-pend a dollar sign $.


- $ 10G network card for the controlling computer in the lab
  - Choice is Fiber or Cat6A 
  - If fiber: make sure 'single mode' LRSFP+ 1310nm and identify connector type: LC is the current industry standard
- Cable run to the nearby telco closet on the same floor to a switch
- $ LIU Switch in telco closet (high-ticket item) 
- Cable is already run vertically ('riser') to aggregation units in the basement
- $ Aggregation units include two modules that must be upgraded to 10Gig
- Signal goes to the campus backbone 40Gig network; and thence ... to AWS


#### Scientist preparation remarks


```
Ethernet cables connect to a port above the the lab table.
There are copper ports in the lab desktops; but the research team will need to upgrade Ethernet network cards 
to 10 gigabit capable. They will purchase 4 SATA3 SSDs to capture data from the microscope camera. 
The Hamamatsu camera writes in parallel to all 4 hard drives; so theoretical speed to the hard drives should be 
24 gigabits/sec. From these drives the goal is a 10 gigabit/s connection to the cloud.
```


## Ports, sockets and tunneling


This topic is related but does not belong on this page: It refers to access to instances inside the cloud; 
i.e. at a much higher level than basic network connectivity. For more on this please see [this page](cc_technical.html).


## Network poster


![cc_network_image_1](/documentation/images/cc/cc_network001.png)

![cc_network_image_2](/documentation/images/cc/cc_network002.png)


{% include links.html %}
