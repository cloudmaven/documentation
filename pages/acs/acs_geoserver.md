---
title: Geoserver on AWS
keywords: research_computing
last_updated: January 26, 2017
tags: [research_computing, case_studies, visualization, data_api, AWS, collaboration, cloud_service, storage, database]
summary: "Geospatial tools on AWS: A GeoServer case study"
sidebar: mydoc_sidebar
permalink: acs_geoserver.html
folder: acs
---

## Introduction
This page describes an example Geoserver deployment for hosting and visualizing Lidar (satellite) data. This prototype was developed for the University of Washington Library Data Services. 

 
## Links
[Webmap created using Leaflet.js](http://lidarwebmap.cloudmaven.org)

[Geoserver backend with hosted Lidar data](http://geoserver.cloudmaven.org)

## Warnings

## Installing Geoserver on Ubuntu 16.04 with Tomcat 7

** Note: This is also available as an [Amazon Machine Image (AMI)](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) 
if you don't want to go through the entire installation process - please contact us if you would like to access the AMI.

Spin-up an instance or virtual machine with Ubuntu 16.04 as the operating system. 
* Make sure to also open port 8080 when configuring your security group settings during the VM setup

Update the OS and install Tomcat 7

```
bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install tomcat7
$ sudo apt-get install tomcat7-docs tomcat7-admin tomcat7-examples
$ sudo apt-get install default-jdk
```

Change permissions for tomcat user roles. Remember to put these in between the <tomcat-users></tomcat-users> tag. 

```bash
$ sudo vi /etc/tomcat7/tomcat-users.xml

<tomcat-users>
  <role rolename="tomcat"/>
  <role rolename="role1"/>
  <role rolename="manager-gui"/>
  <role rolename="admin-gui"/>
  <user username="admin" password="password" roles="manager-gui,admin-gui"/>
  <user username="tomcat" password="tomcat" roles="tomcat"/>
  <user username="both" password="tomcat" roles="tomcat,role1"/>
  <user username="role1" password="tomcat" roles="role1"/>
</tomcat-users>
```

> Note there are security issues related to Tomcat and AWS instances -- please change the passwords above as soon as possible before following the next steps.  

Increase java heap memory to improve startup speed. Modify the first instance of JAVA_OPTS to read as below. 

```bash
$ sudo vi /etc/default/tomcat7

JAVA_OPTS="-Djava.security.egd=file:/dev/./urandom -Djava.awt.headless=true -Xmx1024m -XX:MaxPermSize=512m -XX:+UseConcMarkSweepGC"

```

Restart Tomcat

```bash
sudo service tomcat7 restart
```

Download the latest release of geoserver web archive on this page: http://geoserver.org/release/stable/
At this time, the latest release is 2.10.

```bash
$ wget 'http://sourceforge.net/projects/geoserver/files/GeoServer/2.10.0/geoserver-2.10.0-war.zip'
$ sudo mv geoserver-2.10.0-war.zip /var/lib/tomcat7/webapp/
$ sudo unzip /var/lib/tomcat7/webapps/
$ sudo service tomcat7 restart
```

That's it. You may be prompted to install unzip in that case, just `sudo apt install unzip` and proceed accordingly. 

## Loading data into Geoserver

It is good practice to keep your data stored separately from your service deployment instance. Instructions to mount an additional EBS drive to your EC2 instance can be found [here](https://cloudmaven.github.io/documentation/aws_ec2.html#mounting-the-attached-volume).

In the previous step, Tomcat and Geoserver were deployed. Now you're ready to load your data into Geoserver. For the development of the Lidar portal, I used Lidar data obtained from the Puget Sound Lidar Consortium which were then generated into GeoTIFF mosaics by Harvey Greenberg at the UW Earth and Space Sciences Department. 

![](/documentation/images/acs/acs_geoserver_img0001.png)
You will need to log in to Geoserver. The default username and password is admin:geoserver. 

> Remember to change your password as soon as possible for security reasons!!! 

Select Stores > Add New Store > GeoTIFF and enter the na

![](/documentation/images/acs/acs_geoserver_img0002.png)  

![](/documentation/images/acs/acs_geoserver_img0003.png)

## Creating a Webmap 
The webmap was created using Leaflet.js.  
{% include links.html %}
