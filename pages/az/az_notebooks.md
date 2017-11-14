---
title: Azure Notebooks (Jupyter) 
keywords: azure, best, practices
last_updated: November 14, 2017
tags: [Azure, coding, notebooks, jupyter]
summary: "Introduction to Microsoft Azure Notebooks (aka Jupyter)." 
sidebar: mydoc_sidebar
permalink: az_notebooks.html
folder: az
---

# Azure Notebooks
## Introduction 
### What is Azure Notebooks?
Azure Notebooks is a free service for anyone to develop and run code in their browser using Jupyter.  Jupyter is an open source project that enables combing markdown prose, executable code, and graphics onto a single canvas: 
![Notebook Image](/documentation/images/az/az_notebook_intro_01.png)
**A Jupyter notebook showing Python code, markdown and interactive graphics**

Azure Notebooks currently supports Python 2, Python 3, R and F# and their popular packages. For example, for Python the Anaconda distro is preinstalled.   All your code and data is persisted. 

## Usage Scenarios
Since Azure notebooks is a general code authoring, execution and sharing platform, you can use it for many diverse scenarios: 
- Learn a new programming language – try one of the [frontpage tutorials](https://notebooks.azure.com/Microsoft/libraries/samples/html/Introduction%20to%20Python.ipynb)
- Learn Data Science – try [Jake VanderPlas' book](https://notebooks.azure.com/jakevdp/libraries/PythonDataScienceHandbook)
- [Teach a course](https://notebooks.azure.com/garth-wells/libraries/CUED-IA-Computing-Michaelmas) for hundreds of students 
- Give a webinar online or at a conference without spending time on installation 
- Enable GitHub users to directly load and run notebooks by [creating a GitHub launch badge](https://notebooks.azure.com/help/libraries/sharing/create-a-github-badge)
- Give PowerPoint like [slideshows](https://notebooks.azure.com/help/jupyter-notebooks/slides) where code in slides is executable! 

You also get Terminal/Shell access to your own Linux environment which you can use for git, file, etc. operations.

### Current Service limitations
The service is free but there are network limitations to prevent abuse.  We have white-listed lots of data sources and services and regularly add more per user requests. 
There is a 4G memory limit per user and a 1G data limit. 

### Next steps
- Check out some of the frontpage samples and tutorials.   You can view any pubic notebook on without logging in. 
- If you want to run a notebook, simply login any Microsoft, Gmail, etc. email address “Clone” the Library of notebooks so you have your own copy, and click “Cell/Run-All” ! 

If you’re looking for even more notebooks to try check out these two resources:  
- [https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks)
- [http://nbviewer.jupyter.org](http://nbviewer.jupyter.org)

### Questions? 
Visit us on our [GitHub](https://www.github.com/Microsoft/AzureNotebooks) page or check out the [Help](https://notebooks.azure.com/help) section.   
Twitter: @AzureNotebooks  

Email: (please file issues on github) nbhelp@microsoft.com

## Discovering Notebooks
There's a large collection of existing notebooks that you can discover and use on Azure Notebooks. 
Here's a list of interesting notebooks that you can save locally & upload:
- Check out some of the frontpage samples and tutorials. You can view any public notebook without logging in.
- [https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks)
- Check out [http://nbviewer.jupyter.org](http://nbviewer.jupyter.org) for a gallery of notebooks as well.

*NOTE: Some notebooks may require prerequisites which you will need to install using !pip install (for Python) or install.packages (for R). Also, some packages may not yet be available in Azure Notebooks.*

## Signing Up
Azure Notebooks supports signing in with either a Microsoft account (formerly Windows Live ID) or with a "Work or School account". 

**Microsoft Accounts**
These are typically @outlook.com/@hotmail.com e-mail account. 

**Work or School Account**
Other accounts used to login to services such as Office 365. 
  
The full write up on Azure Notebooks is located (here)[https://notebooks.azure.com/help]

## Request Form
Please use this [form](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbRxLOqWUi_fJItLLsEfSA7I9UQzk5TVNQMThJRUJQMk00Wk1BWE9CMENCMC4u) to provide feedback, request more documentation, request someone to contact you for help, etc.


{% include links.html %}




