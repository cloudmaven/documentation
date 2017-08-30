---
title: NicaDIF on AWS
keywords: research_computing
last_updated: January 26, 2017
tags: [research_computing, collaboration, AWS, data_api, visualization]
summary: "Nicaragua DIF implementation on AWS"
sidebar: mydoc_sidebar
permalink: acs_nicadif.html
folder: acs
---

## Introduction
The purpose of this page is to describe the implementation of the Dynamic Information Framework (DIF) in Nicaragua.


## CC*IIE Remarks

### Objective and Approach
The country of Nicaragua is set in a climatic zone subjected to extreme storm events that cause land slides
and flooding. This work is highly motivated by the need to improve coherence in addressing the development of Nicaragua's
rural landscape and exploring the important linkages between agriculture, water, land and food security An overarching goal here is to provide advanced warning systems and explore different avenues of adaptation to possible climate change outcomes..
There exists various possibilities for tackling resource problems and arriving at actionable infomation through multi-sectoral partnerships. 

This project aims to promote data sharing and collaboration by deploying a base hydrologic model on a virtual machine in the cloud, storing the data on cloud-backed storage, providing analytical tools and scripts via Jupyter notebooks and developing a cloud-based web framework.  


### Solution
The project consists of interrelated analytical pieces: (i) An evaluation of available geospatial information resources (b) Merging and data collection of information into dataframes for hydrologic modeling and watershed analysis (c) deploying modeling platform and associated information in the cloud to encourage data sharing and collaboration (d) visualization tools for actionable information and decision making. Together, these pieces form the backbone of a "[dynamic information framework](ccs/ccs_dif.html)". 

### Results
We have provisioned AWS resources as part of the cloud deployment of the framework. The hydrologic model and associated datasets are stored on an AWS virtual machine (EC2) that is has been made accessible to stakeholders. Technical collaborators can essentially run the complex hydrological model "out of the box". We have also developed Jupyter Notebooks to help with analysis. We are currently working on developing the web framework and refining the training/stakeholder input objectives.  

## Links
[Overarching DIF concept](/ccs/ccs_dif.html)
 
## Warnings
***Stakeholder inputs and participation necessary***



{% include links.html %}
