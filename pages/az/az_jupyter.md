---
title: Jupyter on Azure
keywords: azure, procedural
last_updated: January 26, 2017
tags: [Jupyter]
summary: "Jupyter Notebooks on Azure"
sidebar: mydoc_sidebar
permalink: az_jupyter.html
folder: az
---

# Jupyter notebooks on Microsoft Azure


## Introduction


This page presents the Microsoft Azure Jupyter notebook hosting service as an extremely 
valuable (and currently free (2017)) tool for research.  We use it to support a middle-school
math club called the **Other Math Club** located 
[here](https://notebooks.azure.com/library/89FHPIGSGMs/dashboard).
If you are interested in jumping in: Go to this link and Sign In using your Windows Live ID. 
Your copy of the notebook spins on the Azure Cloud. Some content -- files referenced 
by the notebook pages -- may be ephemeral meaning they can go away when the notebook is closed.
To make them easy to reload we back them up on an open GitHub repo. See the comment below for 
more on this; the point being that the Jupyter environment combined with a little GitHub finesse 
allows you to safely share an interesting research environment with other folks. 


In general we advocate using Jupyter notebooks to create research sandboxes, to develop paper content, 
to share reproducible results, and to communicate on a technical level. Jupyter notebooks support 
Python, R, F Sharp, Julia and other programming languages. They also support markdown including LaTeX mathematical formatting.


Microsoft to their immense credit has created a Jupyter notebook hosting service on their Azure cloud platform. This has two 
advantages over hosting a Jupyter notebook on a machine that you manage: First Azure takes care of the basics of managing the 
notebook and its host machine; so you don't.  Second the Azure Jupyter notebook is connected to other useful technogies;
so it is already built into a broader technical context or ecosystem. These extensions include Azure Machine Learning Studio 
and GitHub, just to begin with. We believe this service has a great future and is well worth your time exploring.


## Links


- [Example notebook](https://notebooks.azure.com/library/89FHPIGSGMs/dashboard) for a middle school math club. 
- [Microsoft Azure Jupyter notebook hosting site](http://notebooks.azure.com)
- [The Azure Notebook FAQ](http://notebooks.azure.com/faq) is an excellent overview.
- [Gallery of interesting notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-and-IPython-Notebooks)
- [Data loading > Jupyter instructions](https://notebooks.azure.com/run/Microsoft/samples?dest=/notebooks/Getting%20to%20your%20Data%20in%20Azure%20Notebooks.ipynb)


## Warnings

- *** Azure hosting of Jupyter is under development so be prepared to shoot them a 'help!' email. The other important
thing to realize is that from a Python cell you can issue a Linux command using '!command'. In particular the
link above on data loading tells you how to use !curl to load data from GitHub; and you may also want to
avail yourself of '!conda install' at the top of a particular notebook to make sure your added libraries are in place.  ***
- *** When your notebook shuts down any data you have uploaded will evaporate. It does not persist. We have an entire
section below called 'Rehydration' on how to deal with this by parking the necessary files on GitHub. Please note: 
GitHub does have file size restrictions so you may need to resort to other means.***


## Rehydration

As of spring 2017 Azure Jupyter notebooks do not persist data that you upload when the Notebook shuts down. 
This means that you have to "rehydrate" your data supply when you re-start; but this can be done with an 
initialization cell running Python as follows: 

An Azure Jupyter notebook cell executing Python can run Linux commands by prefacing them with
an exclamation mark '!'. In particular you can use the Linux curl command to inhale files (particularly 
in our case: Smallish data files and important figures, say .png files)  
to the current Notebook session from GitHub. The GitHub URL to use is not necessarily easy to find; 
so let's place it right here.

The key information is as follows: 

``` 
My github account is 'my_username'
My repository is called 'my_reponame'
My branch is 'my_branchname'
My file is 'my_filename.png'
```

The curl command to retrieve this to /nbuser/home (where it will be called file0001.png) is: 

```
!curl https://raw.githubusercontent.com/my_username/my_reponame/my_branchname/my_filename.png -o file0001.png
```


{% include links.html %}
