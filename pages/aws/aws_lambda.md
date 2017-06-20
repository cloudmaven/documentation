---
title: AWS Console
keywords: aws
last_updated: January 26, 2017
tags: [AWS, account_management]
summary: "AWS Console"
sidebar: mydoc_sidebar
permalink: aws_console.html
folder: aws
---

## Introduction


This page describes the use of the AWS *lightweight* **Lambda** service. It includes a case study 
from a circa-2016 student capstone project involving the management of a fleet of vehicles. 


## Links


## Warnings


## Lambda is...


## Capstone case study

The case study involves GPS-capable devices that are first configured in the office and then deployed
in a fleet of vehicles. They are able to log data via the cellular phone network to a location maintained
by Sprint (the company) where they can be retrieved using a REST API. This in turn can be called programmatically
for example using the Python urllib2 Library. 


Lambda supports Python code; so the objective here was to automate the REST API calls in a Lambda function; 
and to place the recovered data into an RDS database on AWS. 


![capstone concept](/documentation/images/aws/aws_lambda0001.png)


Student participants are some subset of these names: Anya, Anagha, Yuzhou (Sissi), Mingxin.


AWS Solutions Architect solutions to problems are given in quote blocks.


Technology: Interoperable NAT Gateway, Lambda, RDS, VPC.


NAT Gateway: See [this link](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html).


Problem: The solution requires a database (RDS) and this should be isolated from the internet via a VPC.
The Lambda function associated with it must be proximal (inside the VPC) but the students could not then
access that Lambda function. See Lambda role **lambda_basic_vpc_execution**.


> The NAT Gateway allows access to the internet without exposing the systems in the VPC directly.
> Systems in your VPC subnets do not need an internet-routable IP address. Traffic outbound (to the internet)
> goes from the subnet to the NAT Gateway and thence out. 
>
> Lambda inside a VPC requires this because Lambda does not provide a public IP address to a function when it is 
> running. In contrast Lambda running *outside* of a VPC does provide a function with a public IP address 
> for its duration.


New problem: Since Lambda connects to the RDS requiring credentials: Is there anything in Lambda that can *hide*
those credentials? The students would prefer not to embed their password in Python code. 


> Store the password file in S3. Using IAM configure permissions so that only Lambda has access to the S3 bucket
> and hence the passowrd. This is simple and secure. 


New problem: Applications like Tableau want access to data held in the RDS, i.e. within the VPC. How to access?


> Create a VPN connection from the User's network to the VPC hosting the RDS database. RDS remains 
> isolated from the internet. It is also feasible to install Tableau on an EC2 within the VPC and restrict
> access to that EC2 using *Security Groups*. A final option (for running Tableau locally against the 
> RDS) would be to put the RDS on a *public* subnet and use *Security Group* rules to restrict access
> based on the source ip address. (CIDR block specification.)


{% include links.html %}
