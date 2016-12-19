---
title: Research Computing Case Studies
keywords: research_computing
last_updated: November 2, 2016
tags: [research_computing,geospatial,case_studies]
summary: "Use of Geospatial Tools for Research - Case Studies "
sidebar: mydoc_sidebar
permalink: rc_geoserver.html
folder: mydoc
---

## Installing Geoserver on Ubuntu 14.04 with Tomcat 7
** Note: This is also available as an [Amazon Machine Image (AMI)](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) if you don't want to go through the entire installation process - please contact us if you would like to access the AMI.

1. Spin-up an instance or virtual machine with Ubuntu 16.04 as the operating system. 
  * Make sure to open port 8080 when configuring your security settings during the VM setup
2. Update the OS and install Tomcat 7

```bash
  $ sudo apt-get update
  $ sudo apt-get upgrade
  $ sudo apt-get install tomcat7
  $sudo apt-get install tomcat7-docs tomcat7-admin tomcat7-examples
  $ sudo apt-get install default-jdk
```
  
3. Change permissions for tomcat user roles. Remember to put these in between the <tomcat-users></tomcat-users> tag. 

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

4. Increase java heap memory to improve startup speed. Modify the first instance of JAVA_OPTS to read as belo. 

```bash
$sudo vi /etc/default/tomcat7

JAVA_OPTS="-Djava.security.egd=file:/dev/./urandom -Djava.awt.headless=true -Xmx1024m -XX:MaxPermSize=512m -XX:+UseConcMarkSweepGC"

```

5. Restart Tomcat

```bash
sudo service tomcat7 restart
```

{% include links.html %}
