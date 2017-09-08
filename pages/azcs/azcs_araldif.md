---
title: AralDIF on Azure
keywords: Azure
last_updated: January 30, 2017
tags: [Azure]
summary: "Azure-based Geospatial API for the Aral Sea DIF project"
sidebar: mydoc_sidebar
permalink: azcs_araldif.html
folder: azcs
---

## Introduction


This page provides an overview of the 
AralDIF project as implemented on the Microsoft Azure public cloud platform.
'Aral' refers to the Aral Sea in central Asia, and DIF abbreviates 'Dynamic Information System'. This is one of several
related, regionally focused projects that implement hydrological models in concert with data from local stakeholders. 
The ultimate objective is to provide actionable public data concerning water resources in regions that are subject
to water stress.


## CC*IIE


The NSF-sponsored work under the CC*IIE initiative is focused here on cloud adoption in research. Our perspective is
researcher-centric and cloud-agnostic. It is therefore worth noting that this cloud implementation success story is
based on the Microsoft Azure public cloud and built in part from the Microsoft Visual Studio integrated development environment. 


### Objective and Approach


The AralDIF program is an extension of the DIF (ccs/ccs_dif.html) framework for Central Asia. The primary focus domain is the Aral basin. 
The core project is a collaboration between the World Bank and stakeholders from seven different countries with drainage basins flowing into 
the Aral sea from the east.


Our task has been to implement a hydrologic model to understand changes in the regional water balance, quantify the effects of climate 
change on water resources and agricultural production, and translate these linkages into actionable information through a decision support 
system.  In the process, we are also looking to build a system to encourage data sharing and collaboration in a geo-politically sensitive region.  


### Solution


In order to facilitate the data sharing process, we have developed APIs that allow users to subset data from cloud-based storage. 
We have also developed a website to help stakeholders visualize model input and outputs as well as perform minor analysis. Further, 
all data layers, model setup and parameters are stored on a virtual machine on a public cloud platform (MS Azure), thus negating 
the ability of a single country/stakeholder to dominate or manipulate the data. We have used publicly-available datasets for our 
analysis and data layers and used open-source tools for our cyberinfrastructure.   


### Results


The AralDIF website is available at: [AralDIF](http://araldif.azurewebsites.net). 
Publications are pending. 



### Links
- [ICIMOD](http://www.icimod.org)
- [NASA SERVIR](https://www.nasa.gov/mission_pages/servir/index.html)



{% include links.html %}
