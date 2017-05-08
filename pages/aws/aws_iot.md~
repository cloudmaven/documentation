---
title: IoT on AWS
keywords: aws, iot, procedures
last_updated: January 26, 2017
tags: [AWS, IOT, case_studies]
summary: "IoT on AWS"
sidebar: mydoc_sidebar
permalink: aws_iot.html
folder: aws
---

## Introduction


This page provides a template for registering and operating an IOT device -- specifically an
Arduino Yun -- on a university WiFi network in relation to the AWS public cloud. Operation 
includes both recording sensor data and actuation of a small light. The operational scenario 
is described in more detail below.  We are implementing our example at the University of 
Washington in Seattle. If you are working elsewhere you may benefit by getting in touch
with your local IT management organization.


## Links


- [The AWS CLI](http://aws.amazon.com/cli)


## Glossary


- Diaspora: A term adopted informally here to indicate a distribution and/or dispersion of 
IOT devices. 'Where all the devices are located' often changes over time since transportation 
is a common IOT theme.
- IOT: Internet of Things, the realm of embedded devices (including smart phones) that interact
in some way with a larger ensemble of electronics, people and the environment. While IOT emphasis
is easily placed on the devices we are interested here primarily in the cloud aspect of the story; 
specifically how to place intelligent data management in the cloud in support of an IOT diaspora.
- CLI: The Command Line Interface for AWS, typically installed on an AWS EC2 instance and/or
your computer depending on where you need to work. The CLI operates remotely to effect 
changes and read states on the AWS cloud.


## Admonitions


- ***IOT devices are vulnerable to failure in three senses. First they are susceptible to operational
failure owing to the difficulties in getting bespoke ('one-off') prototype hardware to work reliably
outside of the lab. Second they are susceptible to being undermined by people with malicious intent.
Third they can produce spurious signals that are mistakenly interpreted as accurate.*** 


## Part 1. Scenario


Two Arduino Yun devices are powered up, sitting adjacent to one another on a desktop. 
Each has a light sensor and a laser diode. The laser diodes are aimed at the other Yun's 
light sensor. The objective is to set up a game of ping pong between the two Yuns. 


- First Yun turns on its laser diode
- Second Yun measures an increase in its light sensor
- Second Yun sends a *BRIGHT* signal to an AWS IOT Endpoint
- AWS notifies First Yun that Second Yun is in state BRIGHT
- First Yun turns off its laser diode
- Second Yun measures a decrease in its light sensor
- Second Yun turns on *its* laser diode
- First Yun registers this in *its* sensor and sends a *BRIGHT* signal to AWS
- AWS notifies Second Yun
- Second Yun turns off its laser diode
- ...and so on...


## Part 2. Procedural

- Install the AWS CLI per the instructions at http://aws.amazon.com/cli
- Set up a REST API endpoint on AWS for the IOT devices to use
  - Need a little more detail here Kilroy
- Visit YouTube and search on AWS IOT to identify instructional material suited to your project.
  - You can certainly continue with this tutorial but we suggest checking online



{% include links.html %}
