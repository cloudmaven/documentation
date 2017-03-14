---
title: Cloud Computing Cost Management
keywords: cloud, introduction
last_updated: October 6, 2016
tags: [account_management, cost, proposals, cloud_basics, research_computing]
summary: "Cost of moving research computing to the cloud"
sidebar: mydoc_sidebar
permalink: cc_cost_management.html
folder: cc
---

## Introduction
This page describes the cost of putting research computing on the public cloud. In the **Proposals** section of 
[cloudmaven](http://cloudmaven.org) we have [a more tactical page](p_costing.html) which may also be of interest.

## Links
- [The cloudmaven page on cost estimation for research proposal writing](p_costing.html)

## Warnings
- ***It is commonly asserted that the cloud does not compare in cost to purchasing your own hardware. We make the case here that this assertion is false.***
 
## How much does the cloud cost?

A quick answer is "3 cents per GB-month of storage, 3 cents for an hour of CPU time". This is something we will qualify and expand upon here;
but for the sake of getting started those are useful numbers to keep in mind.  

### Qualifiers 
- A powerful multi-core machine costs between 30 cents to one dollar per hour (with further qualifiers)
- The storage cost for archival is currently 0.4 cents per GB-month at AWS.

### Total cost of ownership (TCO)

If you purchase a computer you are done paying for the hardware; so we present three tiers of effective cost that factor in your time. 

- You bought it; you (or someone) maintains the system by installing patches and upgrades. You (or someone) provides space, power and does back-ups. 
- You pay for it on the cloud: The cloud provider does the care and maintenance. You just use the system.
- You pay for a service on the cloud: You don't even use the system; you just use the service.

To elaborate further: A VM on the cloud is not something you ... kilroy left off here




 and you can use it until it fails; hopefully for 2 or more years. Then you need to purchase 
another computer. This is the traditional computing model and it makes sense if your machines are adequate to your computing needs provided that someone can 
pay for the electricity and cooling and someone has the time to maintain the operating system; and provided you have a good back-up strategy in case something 
bad happens. Cloud computing costs money but eliminates a lot of these ongoing maintenance tasks. Cloud computing resources are billed using a utility model: You pay for what you use.

Cost is managed by turning off resources when they are not in use; and by carefully managing how many machines are in use when running jobs. Both of these tasks 
can be associated with automatic alarms that can prevent cloud usage from getting out of control and expensive.

See also the section below on cloud research credits, a way to mitigate the cost of learning if the cloud works for you.

## Cloud Research Credits
There are at least four approaches open to you:

- Cloud novice approach: Get a $100 free credit account on AWS or a $200 free credit account on Microsoft Azure. Both require you to enter credit 
card info. This is like giving your hotel your credit card in case you break the TV.

- You need some substantial compute power Today: Contact us by email. We may be able to quickly (within a few hours) set you up with a temporary 
User account. You will need to coordinate your usage with us; we will need to make sure you are proficient at managing resources; and we will 
ask that you do some reporting on your experience. This can be a short-term stop-gap.

- You need some serious compute power for a year at no cost (requires 2 months to set up): Fill out the one-page application here for AWS 
or the one-page application here for Microsoft Azure. On approval you can receive up to $20k in research credits for a year. Both public 
clouds are excellent so we do not recommend one over the other. Come visit our office hours if you would like to disucss relative merits further.

- You need some serious compute power and you have a budget: Contact UW IT to set up a purchase order. This will take a couple of days.

{% include links.html %}
