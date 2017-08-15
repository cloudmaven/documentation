---
title: Relational Database Service on AWS
keywords: aws, spotmarket, procedures
last_updated: January 26, 2017
tags: [AWS, database, cloud_service, storage, data_api, research_computing, data_science, scale]
summary: "The RDS (Relational Database Service) on AWS"
sidebar: mydoc_sidebar
permalink: aws_database.html
folder: aws
---

## Introduction

This page describes creating and using a database on the AWS public cloud: As a service, not as 
software installed on a Virtual Machine. Our example study captures a near-real-time data stream 
from a university campus power consumption monitoring system. We begin by describing the distinction 
between the traditional approach to SQL database management and the AWS **Relational Database 
Service**.

## Links
- AWS link
- AWS RDS link
- [What is my ip address?](http://whatsmyip.org)

## Warnings 

- ***DynamoDB and Redshift and so forth need to be called out here in addition
to RDS flavors and what may be missing***

## RDS on AWS

To create a MySQL database on a Linux machine typically requires some administrative access and a 
command line; plus a browser to identify resources, search for procedures and get questions answered. 
In the course of installing and maintaining the database you will also typically be concerned
with patching the underlying operating system periodically. This requires time and thought if you
are diligent and exposes your system to risk if you are not. 

In contrast if you have an AWS cloud account you can create the database without the underlying
Virtual Machine through the three typical approaches to 'talking with the cloud'. These are,
in order of sophistication: Using the AWS console 

{% include links.html %}
