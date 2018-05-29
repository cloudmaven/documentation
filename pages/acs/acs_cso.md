---
title: Community Snow Observations on AWS
keywords: research,case,study,citizen_science,webapp
last_updated: May 29, 2018
tags: [research_computing, case_studies, visualization, data_api, AWS, collaboration, cloud_service, storage, database]
summary: "Community Snow Observations on AWS: A Web Application case study"
sidebar: mydoc_sidebar
permalink: acs_cso.html
folder: acs
---

The [community snow observations](http://communitysnowobs.org) project aims to achieve a better understanding of snow depth variability in mountainous regions. We are recruiting community-based observers (citizen scientists), including backcountry professionals and recreationists, to help gather snow observations.

The project has partnered with [Mountain Hub](http://about.mountainhub.com/) (Crowd Sourced information App for all outdoor activities) for collecting snow observations data. The snow observations collected are displayed in our [web application](http://app.communitysnowobs.org/).

This document outlines how the system has been setup within Amazon Web Services (AWS)

[System Architecture](#system-architecture)
[System Setup](#setup)

---
## System Architecture

The system uses the following technologies within AWS to host both the website and web application.

- [EBS (Elastic Beanstalk)](https://aws.amazon.com/elasticbeanstalk/)
- [RDS (Relational Database Service)](https://aws.amazon.com/rds/)
- [Route 53](https://aws.amazon.com/route53/)
- [S3 (Simple Storage Service)](https://aws.amazon.com/s3/)

### EBS

Elastic Beanstalk is being used to manage the architecture of the website and web application, providing auto scaling capabilities and automatic updating of core ecosystem for the application.

#### Wordpress
[Wordpress.org](https://wordpress.org/) is hosted within Elasticbeanstalk. This application is used to manage the content of the website.
![ebs wordress](/documentation/images/acs/acs_cso_ebs_wordpress.png "Wordpress on EBS")

#### Django
[Django](https://www.djangoproject.com/) is hosted within Elasticbeanstalk. This application is used to develop the web application.
![ebs django](/documentation/images/acs/acs_cso_ebs_django.png "Django on EBS")


### RDS

Relational Database Service is used to manage the MySQL relational database for Wordpress. EBS with RDS completes the classic Linux, Apache, MySQL, PHP (LAMP) setup for Wordpress.

[MySQL Database](https://www.mysql.com/) is hosted within RDS.
![rds mysql](/documentation/images/acs/acs_cso_rds_mysql.png "MySQL on RDS")

### Route 53

Route 53 service is used to manage DNS (Domain Name System) for our website and web application

### AWS S3 Bucket

S3 Bucket is used as storage for the images, videos, and files within the website. A plugin is used to push content from wordpress to an s3 bucket.

![s3 cso](/documentation/images/acs/acs_cso_s3_cso.png "CSO Wordpress Content on S3")

---
## Setup

1. [Setting up wordpress in AWS with Elastic Beanstalk and RDS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-hawordpress-tutorial.html)
2. [Setting up Django Application in AWS with Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)
