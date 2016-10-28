---
title: AWS Procedural
keywords: documentation theme, jekyll, technical writers, help authoring tools, hat replacements
last_updated: July 3, 2016
tags: [AWS]
summary: "Guides related to AWS EC2 instances"
sidebar: mydoc_sidebar
permalink: aws_ec2resources.html
folder: mydoc
---

## FTP Setup and EC2 Instance
Overview: Create a virtual machine, install the ftp server and setup user accounts. Bonus: Bind your EC2 instance to an Elastic IP so you can reuse the same public IP even if your instance changes!

1.  Sign up for a free AWS account [here](https://aws.amazon.com/free). Usage and free tier information available [here](https://aws.amazon.com/free/?sc_ichannel=ha&amp;sc_ipage=signin&amp;sc_iplace=body_link_text&amp;sc_icampaigntype=free_tier&amp;sc_icampaign=ha_en_free_tier_signin_2014_03). You will need to provide credit card information, but won't be billed unless you exceed the free tier usage limits. Don't worry, you can set up alarms to alert you when you're near the limit! More on that later. 

2.  [This recipe](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) from AWS is straightforward. Print it out and don't skip a step. An EC2 (elastic compute cloud) is your virtual computing environment i.e. your virtual machine. This video by Microwave Sam expands on the EC2 setup.   

    <iframe style="display: block; margin-left: auto; margin-right: auto;" src="//www.youtube.com/embed/wNr7YqjjzOY" width="425" height="350"></iframe>  

3.  Once your virtual machine is setup, you can access your "computer in the cloud" by securely tunneling in via the Terminal on your macbook, ssh on your Unix machines and Putty or other Unix environment emulator on Windows. 

4.  You can now set up an FTP server on your virtual machine. 

5.  The first solution [here on Stackoverflow](http://stackoverflow.com/questions/7052875/setting-up-ftp-on-amazon-cloud-server) is non-tortuous and really easy to follow. Thanks, clone45!

6.  You should now be able to use an FTP client to connect to your ftpserver. 

7.  If you can't connect, check your directory permissions on your virtual machine! 

8.  Again, follow instructions and don't skip a step!

## Elastic IPs

The annoying thing I've experienced with AWS is that every time you stop and restart an instance, you get assigned a new public DNS for your instance (e.g. public DNS = ec2-52-41-144-22.us-west-2.compute.amazonaws.com). You can get around this by associating ypur instance with an Elastic IP. Steps are outlined [here](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html). Once you've associated the Elastic IP with a running instance, you can ssh into the VM with the Elastic IP but using the previous public key generated for the instance. Don't forget to update the vsftpd.conf with your new Elastic IP address which is now your public address.

```
    > sudo vi /etc/vsftpd/vsftpd.conf
    pasv_address=<Elastic IP address>
    > sudo /etc/init.d/vsftpd restart
```
MS Azure on the other hand, let's you choose your on public DNS hostname which reduces the need for this workaround.

## DNS Hostnames

If you have your own registered domain, you can set your A-Record to point to the Elastic IP address of your instance. That gets rid of the unsightly public DNS that AWS assigns to you. Here's the example for cloudmaven.org (our domain registrar is Namecheap.com): ![](https://raw.githubusercontent.com/amandalehr/cloudmaven/master/dns-eg.tiff)

An A-record points the hostname (here "compute") to the AWS instance Elastic IP (here "52.41.144.22"). I can then ssh into my compute instance using ec2-user@compute.cloudmaven.org. You can also set up similarly an A record called ftp that points to the elastic IP of your ftp server instance to allow ftp access into say ftp.cloudmaven org 


## EC2 instance background
Download PDF [here](/documentation/pdf/Doc46_EC2_Resources_on_AWS.pdf)

{% include links.html %}
