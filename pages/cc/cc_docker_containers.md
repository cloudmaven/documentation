---
title: Docker containers on the public cloud
keywords: cloud, docker
last_updated: October 6, 2016
tags: [research_computing, Jupyter, containers, reproducibility, account_management, data_science, cloud_basics]
summary: "Using Docker containers on the public cloud"
sidebar: mydoc_sidebar
permalink: cc_docker_containers.html
folder: cc
---

## Introduction

This document -- available [here](http://cloudmaven.org "A cloud computing technical website") -- is 
an introduction to the use of Docker containers. These are software constructs that 'contain' an entire
computing environment that can be bundled as a file called a Docker image. This image can be transported to 
another physical computer and reconstituted there. 
We recommend reading the [Wikipedia Docker(software)](https://en.wikipedia.org/wiki/Docker_(software)) 
entry as a first step in understanding the Docker project / phenomenon. Docker containers provide you 
with intrinsic portability for your computing environment and reproducibility of execution results. 

## Links

- [Wikipedia description of Docker containers / project](https://en.wikipedia.org/wiki/Docker_(software)) 
- [Docker official website](https://www.docker.com/what-docker)
- [Geohackweek wiki entry](https://github.com/geohackweek/geohackweek.github.io/wiki/Docker-steps-to-run-containers)
- [Geohackweek docker tutorial](https://geohackweek.github.io/Introductory/01-docker-tutorial/)

## Warnings

*** Please let us know if you have a 'vendor lock-in' horror story; we are looking for evidence that this as more than 
an urban myth. In any event: Docker containers are often presented as an antidote to vendor lock-in; so this remark is
just a bit of (dubious!) folk wisdom.***

## Additional remarks

The [configuration](https://github.com/geohackweek/geohackweek.github.io/wiki/Docker-steps-to-run-containers) 
and [tutorial](https://geohackweek.github.io/Introductory/01-docker-tutorial/) entries 
at the Geohackweek web pages are together a tutorial for getting
started with Docker containers. It is tailored to the event (November 2016); an update would be appreciated to
generalize the solution away from geohackweek. 

The above material also indicates how Docker containers can be integrated with Jupyter notebooks. 

{% include links.html %}
