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


To go further: [**D3**](https://d3js.org) is highly favored at this time (elegant plotting/visualization; plus open source). D3 was developed by 
[Mike Bostock](https://bost.ocks.org/mike/path/)
who formerly worked in Jeff Heer's lab, now at UW.  See also this [idl link](https://idl.cs.washington.edu). 
To continue in this vein we mention 
further that D3 data interpolation examples can be tied to smart data decimation; 
see [this link associated with Simen Brekken](http://bl.ocks.org/simenbrekken/6634070).


Another item: The FK et al paper on OOI HD video data. This work illustrates derived scientific data products and automated QA/QC
(Quality Assurance / Quality Control) methods. This QA/QC code would ideally be run on the cloud; and would have the ability to
work through the entire video archive. See [this pdf](https://www.dropbox.com/s/grky08o1hxgs8u9/PID4900623.pdf?dl=0).


Another item: [A beautifully illustrated data story written in D3](http://ww.r2d3.us/visual-intro-to-machine-learning-part-1/).


{% include links.html %}
