---
title: Ocean Observing Initiative
keywords: NSF
last_updated: January 30, 2017
tags: [research_computing]
summary: "Ocean Observing Initiative"
sidebar: mydoc_sidebar
permalink: ccs_OOI.html
folder: ccs
---

## Introduction 


This page describes a case study of cloud computing applied to the Ocean Observing Intiative (OOI). 


## Starting material provided by Friedrich Knuth


### HD Video Data

Tim Crone at LDEO is working with Aaron Marburg at APL. Tim has set up a [platform](https://chiron.ldeo.columbia.edu) 
to provide co-located processing and storage of HD video data.  Transfer to cloud would require a cost evaluation; 
and likewise with broadband hydrophone data. 

### OOI M2M with real-time data visualization


[IPython notebook](https://github.com/friedrichknuth/m2m_demo), documentation pending. The notebooks gets at the basic data
and the metadata request functionality. Bear in mind that real-time requests are called 'synchronous' and come back as JSON 
with a maximum of 1000 data values; whereas 'asynchronous' requests produce .nc files off a THREDDS server. In both cases 
we are seeing raw data processed on-request to a data product.

The [real-time plotting function](https://github.com/ooi-data-review/ooi-realtime-plotting) is built on top of the above notebook. 


```
from concurrent.futures import ThreadPoolExecutor
```

is the key to sending continuous requests that re-initiate after each prior request is completed.  For more on this see 
the [OOI Data Team portal](http://ooi.visualocean.net). 


To go further: [**D3**](https://d3js.org) is highly favored at this time (elegant plotting/visualization; plus open source). D3 was developed by Mike
Bostock who came from Jeff Heer's lab, now at UW.  See also this [idl link](https://idl.cs.washington.edu). 



{% include links.html %}
