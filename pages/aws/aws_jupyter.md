---
title: AWS Procedural
keywords: jupyter
last_updated: January 26, 2017
tags: [AWS]
summary: "Jupyter Notebook on AWS"
sidebar: mydoc_sidebar
permalink: aws_jupyter.html
folder: aws
---

## Introduction

The purpose of this page is to overview AWS-based (EC2) approaches to creating and using Jupyter notebooks, 
We describe a *standard* server-based approach with some shareability features and a *personal* approach
which makes use of an ssh tunnel. The latter is also described on [this technical page](cc_technical.html).
Aside from AWS you can also create a static Jupyter notebook on GitHub, you can clone a Jupyter repo from
GitHub and you can also explore the option described [here](az_Jupyter.html).

## Links

- [Jupyter notebooks](https://jupyter.org/)
- [AWS Jupyter Server instructions](http://chrisalbon.com/jupyter/run_project_jupyter_on_amazon_ec2.html)
- [Our middle-school math club demo notebook](https://notebooks.azure.com/library/89FHPIGSGMs)

## Warnings

***We outline two EC2-based approaches here, shared and non-shared. The shared form is a nice 
collaboration tool but has two drawbacks: First you share **write** access with anyone you give
the password to and second (in early 2017 anyway) there is some browser security complaining 
that you must push past. This seems a bit sketchy.*** 

## Before starting 
In the introduction above we mention five approaches to using Jupyter notebooks.  Here we 
concentrate on the first two of these, both on EC2 instances.

### Approach one: Personal Jupyter notebook, ssh tunnel

Suppose you need a Jupyter notebook for your own research; you do not need to share it with 
anyone. You create an EC2 instance, get the *.pem* key pair file, install Jupyter on the instance
and that's it, you are ready to go... except that you don't have an obvious way of getting the 
Jupyter notebook to appear in a browser (because it the Jupyter server is running remotely). 
The solution: **ssh tunneling** as described [here](cc_technical). 

### Approach two: A shared Jupyter notebook

Suppose that you would like to share access to a Jupyter notebook on an EC2 instance with a few colleagues
via a URL and a simple password. Follow the directions given 

end part 0

{% include links.html %}
