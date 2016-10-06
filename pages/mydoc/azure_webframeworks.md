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

## Web Frameworks 
Download PDF [here](/pdf/Doc43_Jupyter_on_AWS.pdf) 

## Jupyter Notebook As A Service
This document describes how to set your Jupyter Notebook (JpyNb) server to boot on startup so you do not have to type "jupyter notebook" at the command line every time. Also, if your EC2 instance fails and re-boots, JpyNb restarts automatically. 

I'm assuming you have knowledge of basic linux commands e.g. wget, cp, mv and chmod. I also recommend installing JpyNb from Anaconda. The example below assumes that JpyNb is installed through Anaconda. It also assumes that you have an EC2 instance with Ubuntu. 

Download this [init.d script] (https://gist.github.com/Doowon/38910829898a6624ce4ed554f082c4dd) and save as /etc/init.d/jupyter

Edit the file and change this line:

> DAEMON=/home/ubuntu/anaconda3/bin/jupyter-notebook

Also make sure there's a /var/log/jupyter/ folder, or you can create one using mkdir. You may need sudo privileges. 

Then do the following:
```
    sudo chmod +x /etc/init.d/jupyter
    
    # generate a config file
    
    sudo jupyter --generate-config -f /etc/jupyter/jupyter_config.py
    
    # start service
    
    sudo service jupyter start
    
    # start jupyter on boot
    
    sudo update-rc.d jupyterhub defaults
    
    # stop service
    
    sudo service jupyterhub stop
```

Voila! 


{% include links.html %}
