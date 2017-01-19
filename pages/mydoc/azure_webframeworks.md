---
title: Azure Procedural
keywords: azure, procedural
last_updated: October 6, 2016
tags: [Azure]
summary: "Web Frameworks on Azure"
sidebar: mydoc_sidebar
permalink: azure_webframeworks.html
folder: mydoc
---

## Python Web Frameworks 
Download PDF [here](/documentation/pdf/Doc01_PythonWebFrameworkBasics.pdf) 

## Adding PDF buttons
Download PDF [here](/documentation/pdf/Doc02_Djargon_on_Azure_Add_PDF_Button.pdf)

## Introduction
The purpose of this page is to introduce you to the integration of three common Python web frameworks
--Django, Bottle and Flask--with the Azure cloud technology stack. The principle idea is that Microsoft 
has a powerful IDE called Visual Studio that you can configure to publish content to Azure; and it 
allows you to quickly configure and publish one of these web frameworks. We particularly endorse this
route because the web frameworks in turn support APIs (Application Program Interfaces) that serve out 
data in response to RESTful queries. 

## Example REST API Client in Python

Here is a typical scenario: You have some stream gauge data that you would like to make publicly available 
through a programmatic interface. By this we mean that a computer program can talk to your system and obtain
data without involving human beings, web browsers, clicking on <Download> buttons, and so forth. 


You begin by following this recipe: 

1. Get an Azure account
2. Install Visual Studio and link it to your Azure account
3. Create a new Django solution in Visual Studio - here it's called DjangoWebProject1 
![](/documentation/images/azure_webframeworks_pic1.png)
4. You will be asked where you want to install your external packages - choose Add A Virtual Environment (since you're publishing this)
![](/documentation/images/azure_webframeworks_pic2.png)
![](/documentation/images/azure_webframeworks_pic3.png)
5. In order to use the API we have written - you will need to change your version of Django to Django1.9.2. To do this, right click on the name of your virtual environment and click 'Install Python Package', select install using pip and type django==1.9.2. 
![](/documentation/images/azure_webframeworks_pic4.png)
![](/documentation/images/azure_webframeworks_pic5.png)
6. Include an API in your solution and publish this to Azure. You can download the API from [Github](https://github.com/amandalehr/araldif)  

This might be a website called geohack.azurewebsites.net

![](/documentation/images/azure_webframeworks_pic7.png)
![](/documentation/images/azure_webframeworks_pic8.png)
![](/documentation/images/azure_webframeworks_pic9.png)
![](/documentation/images/azure_webframeworks_pic10.png)

7. Test your API; let us imagine that it works great
8. Write a Python Client that automatically gets stream data from the website

"Write a Python Client" might sound intimidating but it is quite straightforward. 

```python
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
