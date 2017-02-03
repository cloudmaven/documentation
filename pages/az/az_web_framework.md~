---
title: Azure Web Frameworks
keywords: azure, procedural
last_updated: October 6, 2016
tags: [Azure]
summary: "Web Frameworks on Azure"
sidebar: mydoc_sidebar
permalink: az_web_framework.html
folder: az
---

## Introduction

The purpose of this page is to introduce you to web frameworks supported on the Microsoft Azure stack. 
We particularly emphasize three that use Python: Django, Bottle and Flask. The basic idea is that 
common web-based tasks share the same basic structure and these frameworks accelerate building those
features by providing most of the necessary structure; you just fill in the details. 

Microsoft has a powerful Integrated Development Environment (IDE) called Visual Studio that you can configure 
to publish content to the Azure cloud.  Visual Studio in particular provides Django, Bottle and Flask 
solution templates that deploy in minutes.  We endorse web frameworks particularly because they make it
easy to share data through an Application Program Interface (API).

## Links
- VS
- Azure
- API

## Warnings

## please integrate this: on adding PDF buttons
Download PDF [here](/documentation/pdf/Doc02_Djargon_on_Azure_Add_PDF_Button.pdf)

## Example REST API Client in Python

Here is a typical scenario: You have some stream gauge data that you would like to make publicly available 
through a programmatic interface: Someone else's computer program can talk to your system and obtain
data without involving human beings, without web browsers, without clicking on a <Download> button, 
without going to an ftp server... it just happens. As it should. 

You begin by following this recipe: 

- Get an Azure account
- Install Visual Studio and link it to your Azure account
- Create a new Django solution in Visual Studio - here it's called DjangoWebProject1 

![awf01](/documentation/images/az/az_web_framework0001.png)

- You will be asked where you want to install your external packages - choose Add A Virtual Environment (since you're publishing this)

![awf01](/documentation/images/az/az_web_framework0002.png)

![awf01](/documentation/images/az/az_web_framework0003.png)

- In order to use the API we have written - you will need to change your version of Django to Django1.9.2. To do this, 
right click on the name of your virtual environment and click 'Install Python Package', select install using pip and type django==1.9.2. 

![awf02](/documentation/images/az/az_web_framework0004.png)

![awf03](/documentation/images/az/az_web_framework0005.png)

- Include an API in your solution and publish this to Azure. You can download the API from [Github](https://github.com/amandalehr/araldif)  

This might be a website called geohack.azurewebsites.net

![awf04](/documentation/images/az/az_web_framework0006.png)

![awf05](/documentation/images/az/az_web_framework0007.png)

![awf06](/documentation/images/az/az_web_framework0008.png)

![awf07](/documentation/images/az/az_web_framework0009.png)

![awf08](/documentation/images/az/az_web_framework0010.png)

- Test your API; let us imagine that it works great

- Write a Python Client that automatically gets stream data from the website

The phrase "Write a Python Client" may sound intimidating but it is quite straightforward. 
Here in about 20 lines of code:

```
python
import urllib2
import time

def dif(calltype, date1, date2, station):
    baseurl = 'https://streamdata.azurewebsites.net/'
    apiqual = 'api/'
    typequal = calltype + '?'
    sdatequal = 'start=' + date1 + '&'
    edatequal = 'end=' + date2 + '&'
    stationqual = 'station=' + station + '&'
    api_call = baseurl + apiqual + typequal + sdatequal + edatequal + stationqual
    t1 = time.time()
    u = urllib2.urlopen(api_call)
    t2 = time.time()
    data = u.read()
    t3 = time.time()
    print 'urlopen required', t2 - t1, 'seconds; read() required', t3 - t2, 'seconds'
    return data

data = dif('gethydrograph', '1995-01-01', '2000-12-31', 'UCHKU')
print data[0:94]
```

You would run this program on your laptop (say) or some other computer where you want to look
at the data. It will reach out to the Azure site and come back with the data if all goes well.


{% include links.html %}
