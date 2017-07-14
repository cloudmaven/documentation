---
title: Light sheet microscope
keywords: research_computing, data_science
last_updated: June 28, 2017
tags: [scale, research_computing, AWS, case_studies]
summary: "Light sheet microscope for fast-turnaround tumor biopsy"
sidebar: mydoc_sidebar
permalink: acs_light_sheet_microscope.html
folder: acs
---

## Introduction

This page presents a case study on rapid throughput in microscopy.


## Links


- [Feature story](http://www.washington.edu/urology/2017/06/27/tumor-scanning-microscope/)
- [Second feature story](http://www.washington.edu/news/2017/06/26/microscope-can-scan-tumors-during-surgery-and-examine-cancer-biopsies-in-3-d/)

- [Networking notes for AWS](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)
- [aws s3 cp multithreading](https://aws.amazon.com/blogs/apn/getting-the-most-out-of-the-amazon-s3-cli/)


## Overview


![acs_light_sheet_microscope0001.png](/documentation/images/acs/acs_light_sheet_microscope0001.png)
![acs_light_sheet_microscope0002.png](/documentation/images/acs/acs_light_sheet_microscope0002.png)



## Cloud 


- Increase output rate on the computer connected to the microscope camera
- Increase the bandwidth in the telco closet to the vertical pipe to the basement
- Increase the bandwidth on the basement switch to the campus backbone
- Test the link
- Test the link from Health Sciences (relocate the microscope)
- Supposing the microscope-to-AWS-S3 link is working: Get the processing running quickly


## Benchmarks

- With Ian Cote
  - [Networking notes for AWS](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)
  - Notice in the AWS Console EC2 Launch Instance choice table includes a Network Performance column
    - Using a lightweight machine (t2micro) we get MB per second as expected 
    - Using a c4.8xlarge with '10GBit' connection: (1.91, 0.65, 1.14 Gbps, quite ow
      - Via the NON-IPS path over 2 x 10G campus inet pipe: (1.47, 2.53, 2.44 Gbps)
  - To S3...


{% include links.html %}
