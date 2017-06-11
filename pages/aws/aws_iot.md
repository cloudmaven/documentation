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


This page provides a template for registering and operating embedded IOT devices -- specifically 
an Arduino Yun -- on the university WiFi network in relation to the AWS public cloud. Operation 
includes both sensing and actuation using simple hardware (a light and a light sensor). 


## Links


- [The AWS Command Line Interface (CLI)](http://aws.amazon.com/cli)


## Glossary


- IOT: Internet of Things, embedded devices from smart phones to Arduino constructions to FitBits
and beyond -- limitless -- that create an information framework in some environment. 
  - IOT emphasis is first placed on devices 
  - Here we are more interested here in a backing or supportive data system 
  - This system is implemented on the public cloud
- Diaspora: Informally the distribution / dispersion of IOT devices into some environment
  - Devices locations may change over time; a common IOT theme
- CLI: Command Line Interface, here specifically the one for AWS 
  - The CLI exists in the abstract as a means of communicating with the cloud
  - To use it: It must be installed on an EC2 instance 
  - To use it from off the cloud (e.g. from your laptop) it must also be installed there
  - For IOT work we use the CLI to poll or query the supporting data system
- IDS: IOT Data System, an acronym of convenience
  - Implies that we build devices, build the IDS, and then connect them together
- REST API Endpoint: A URL where http messages will be POSTed by the IOT device
- Shadow: An AWS cloud construct 
    - Behaves as a shadow / proxy / image / representation of an IOT device
    - Persists on the cloud regardless of whether the IOT device is connected
    - As such it acts as the "latest known state record" of the device
- MQTT
- MQTT topic: A message tag that enables a message stream to be sorted (by that tag)


## Admonitions


- ***IOT devices are vulnerable to multiple failure modes***
  - ***Operational failure: Fragile, not ruggedized***
  - ***Malicious interference***
  - ***Spurious signals often assumed to be accurate***
- ***To all three such ends we emphasize here on the backing data system: In the public cloud***


## Scenario 1


### A game of ping pong 


Two Arduino Yun devices are powered up, are sitting adjacent to one another on a desktop. 
Each has a light sensor and a laser diode. The laser diodes of one Yun is pointed at the
light sensor of the other Yun.  The objective is to set up a sort of ping pong: 


- Yun 1 laser diode ON
- Yun 2 senses increased signal at light sensor
- Yun 2 transmit Sensor High to the IDS
- IDS publishes Yun 2 Sensor High 
- Yun 1 polls IDS, notices Yun 2 Sensor High state, in response turns laser diode OFF
- Yun 2 senses low signal at light sensor
- Yun 2 transmit Sensor Low to the IDS, turn laser diode ON
- IDS publishes Yun 1 Sensor Low
- Yun 1 senses increased signal at *its* light sensor
- Yun 1 transmit Sensor High to the IDS
- IDS publishes Yun 1 Sensor High
- Yun 2 polls IDS, notices Yun 1 Sensor High state, etcetera


### Ping pong procedural


- Purchase at least 2 Arduino Yun boards (supported for IOT by AWS)
  - Cost is around USD 60 circa 2016
  - These devices have not one but two distinct processors
    - The Arduino microcontroller 'Atmega' (technically ATmega32u4)
    - A LINUX processor 'Atheros' (technically AR9331)
    - Note that we are implicitly dealing with three complexities from the outset
      - Programming an Arduino microcontroller
      - Creating execution logic on a LINUX system
      - Coordinating communication between the two


- Install the Arduino IDE on your laptop
  - IDE = Integrated Development Environment
  - In the work shown here the installation is on a PC running Windows 10
  - The IDE connects with the Arduino Yun by means of a USB cable
    - The Arduino can receive its operating power through this cable
    - The Arduino will ultimately run autonomously off a separate power source 


- Install the [AWS CLI](http://aws.amazon.com/cli) on a laptop


- Set up a REST API endpoint on AWS; our example is called 'quack' 


![quack REST API Endpoint status card](/documentation/images/aws/aws_iot_001_quack_endpoint_synopsis.png)





{% include links.html %}
