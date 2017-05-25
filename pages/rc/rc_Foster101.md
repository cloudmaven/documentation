---
title: Foster 101 Cloud Overview Course
keywords: research, computing
last_updated: May 9, 2017
tags: [research_computing]
summary: "Cloud computing basics with some hands-on for Foster School Of Business"
sidebar: mydoc_sidebar
permalink: rc_Foster101.html
folder: rc
---

**Date:** Thursday May 25, 2017 

**Location:** Paccar 390

**Time:** 4:00 to 6:00 pm 


---


![picture cloud bridge](/documentation/images/rc/foster101_001.jpg)


## Objective


This two hour overview will introduce participants to the public cloud computing environment.
Participants will learn about cloud pillars, cost management, data security, web frameworks,
collaborative tools and cloud-related elements of project management. 


---


## Pre-requisites 

 
- Optional for hands-on activities: Bring a laptop or tablet
- Attendees are encouraged to investigate the cloud in advance, bring questions
- [Our Cloud Maven technical website is at this link](http://cloudmaven.org)
  - Use the left sidebar drop-down for site navigation 
- [Google Android Studio](https://cloud.google.com/android-studio/)
- [Microsoft Azure Machine Learning Studio](https://studio.azureml.net/)
- [Amazon Web Services Lambda serverless computing](https://aws.amazon.com/lambda/)
- [World bank via F# type provider](http://www.tryfsharp.org/Learn/data-science)


---

## Course Outline 

- Welcome and logistics: You may wish to use a browser

- Under cloud cover we are really here to advocate for the broader field of data science

- Introduction to cloud computing
  - Why does the cloud matter to you (as a person in a business)?
    - You are NOT guessing capacity
    - You are NOT waiting for infrastructure arrival / config 
    - Faster time to market
    - Experiment with different solutions; scrap / keep (A/B at Amazon.com example)
    - You have an instantaneous global presence without buying data centers around the world 
    - Start-up? You have the same access to resources that Netflix has
  - What are some strategies for thinking about the cloud?
    - Once there was a PC. Once there was a search engine. Once there was cloud computing.
    - "Culture Eats Strategy"...  
    - The more you know technically the more your perspective will matter 
      - Jargon makes you crazier but also saner... 
      - Developers are *interesting* and may present language bridging challenges
    - The flip side: It can be helpful to describe end results rather than *How* solutions
    - Be ready to learn about and evaluate trends
      - Agile, Test-Driven Development, the 12 Factor App, etc etc etc etc etc
    - Implementing organizational structure (like EA) can make you a hero
      - Fine art of learning to insist and persist without being a threat
      - [Enterprise Architecture video...](https://www.youtube.com/watch?v=qDI2oF1bASk)

![hairball architecture](/documentation/images/rc/foster101_002.png)

  - What is the pbulic cloud?
    - What are the alternatives?
    - Who are the cloud providers?
    - Similarities/differences: Cloud in research versus cloud in the commercial sector?
      - Cattle not pets
      - Storage is not memory
      - In research: sharing, collaboration, repro, student access, scale, security, IOT, cost management, institutional policy, ...
      - In commercial: scale, security, IOT, cost management


- From UW research a case study

![HMA](/documentation/images/rc/foster101_003.png)

![remote sensing example](/documentation/images/rc/foster101_004.png)

![planning hydropower](/documentation/images/rc/foster101_005.png)


- Cloud security: What is it? How does it fail?


![VPC](/documentation/images/rc/foster101_006.png)


- Cost of the cloud: How does one generate a budget? 
  - Logging, Alarms, segue to Amanda


- Amanda on databases, cost, AralDIF, API


- Pillars of cloud
  - Compute
    - Instances, scale, clusters, HPC/HTC, 
  - Storage
    - Buckets and Drives
  - Data management
  - Web applications
    - Web frameworks and the 99% principle
    - Hands on: Using an API to access openly available data
  - Services
    - AWS Lambda
    - Azure Machine Learning Studio
    - Google Android Studio
      - Digression: Why is IOT a cloud story?


- Portability and cloud hopping


- Costing II: The dollar-time tradeoff
<<<<<<< HEAD


=======
- Other cloud services to make your life easier: Managed databases, logging/billing management
>>>>>>> bd02e359b9accb7d305fcc4a5eb28e9464d08c6f
- Closing remarks
  - Collaboration 
  - Hands on: Using a Jupyter notebook to collaborate
    - https://notebooks.azure.com/library/89FHPIGSGMs/dashboard
  - The only constant is change
  - How technology succeeds by vanishing
  - Data science: How eScience uses Jupyter, GitHub and CS skills to impact research at UW


{% include links.html %}
