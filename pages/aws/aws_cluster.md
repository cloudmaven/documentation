---
title: AWS Cluster
keywords: aws, cfncluster, procedures
last_updated: January 26, 2017
tags: [AWS, scale, research_computing, containers, research_credits]
summary: "Clusters on AWS"
sidebar: mydoc_sidebar
permalink: aws_cluster.html
folder: aws
---

## Introduction

This page runs through a build of a compute cluster on the AWS public cloud. 

## Links

## Warnings

- ***Some content here presumes use of other pages, e.g. [EC2 instances on AWS](aws_ec2.html)***
- ***Assumed: You have a properly sanitized AWS account***
- ***Assumed: You have an IAM User credential file giving both your public and private ID
placed in a secure location (*never* on an open repo like GitHub!) ***

## Let's Begin

### important vocabulary

- PIT: Project Identifier Tag, a unique string you designate like 'himat'
- queue: A stack of jobs
- Master: A VM charged with managing a cluster
- Worker: A VM charged with executing sub-processes
- Scheduler: Software that starts sub-processes within a compute task
  - Includes SLURM, Torque, OpenLava and SGE (which we use here)
- qsub: (Linux) submit a job to a processing queue
- qstat: (Linux) get queue status
- qdel: (Linux) delete a job from the queue
- host: List Worker nodes
- IAM User Keys: AWS Access Key ID, AWS Secret Access Key ID


### Strategy

These steps depend upon some pre-configuration, already done for you prior to the class. 
Specifically we created a Virtual Private Cloud with a public subnet for this exercise. 
We created an associated Internet Gateway and a Security Group. The latter permits ssh 
in from *any* location on the internet, so in passing this is not best practice because 
your work is visible from anywhere. 

In what follows you will want to have a Project Identifer Tag or PIT handy. This is just 
a short ID string that you will use to tag everything you create. Mine for example might 
be 'Basie' because I like the music of Count Basie. In what follows when you see either 
'PIT' or possibly 'Basie' you should substitute your own string. In this way everyone 
can proceed on parallel tracks.

Our strategy is fairly simple here:

1. Start up a manager machine on AWS 
2. Log in to this machine as 'ec2-user' using ssh
3. Update this machine, install cfncluster software and create a cluster called PIT0
4. Turn to the CloudFormation service on the AWS console to monitor your progress
5. 

- Autoscale group
- Cloud Formation service
- Cloud Watch service
- Simple Notification Service
- EC2 instance: Launcher with *cfncluster* installed
- cfncluster creates a cluster that includes...
  - An EC2 Master instance
    - Recognizes Worker EC2 instances as they are *added* to the resource pool
    - Has some memory
    - Includes task software
    - Shell script to launch multiple jobs to the SGE processing queue


### Create an EC2 instance cfncluster Launcher

- Refer to the [EC2 page here](aws_ec2.html)
- It will be the 'base of operations' for the compute task
  - Give it a PIT name like 'rob101_Launcher'
  - It can be small and cheap to operate, for example a **T2.micro**.
- Choose the Amazon Linux AMI 
  - This has AWS tools already installed; but we will update and install cfncluster
- The default EBS volume is fine but could be expanded as needed per data 
- We will place everything in a single Region/AZ/etceter
    - Region = us-west-2 (Oregon)
    - AZ = Zone C
    - VPC = Virtual Private Cloud cloud101_vpc
    - Subnet = cloud101_public_subnet
    - Internet Gateway = ... kilroy
    - Route Table entries ... kilroy
    - Security Group = cloud101_securitygroup (ssh allowed from anywhere: 'hi risk')
- Review and launch
  - Download a new key pair
  - You can use an existing key pair as well; be sure you have it on hand
    - This will be a '.pem' file extension. 
      - If you are Windows using PuTTY you will need to convert to a .ppk file format
      - This is done using the PuTTYGen application
- Once it spins up (green dot, ip address present) ssh to this EC2 as ec2-user

Notice that the VPC and so on already exist: Preliminary spadework we are sparing you in this
course. 

### Log in and configure the Launcher

You should now be able to log in to your cfncluster Launcher using ssh (or PuTTY on Windows)
where your login name is 'ec2-user'. You do not enter a password as you are using your .pem
(or .ppk) file to authenticate. 

Once logged in you will update your machine, install the cfncluster tools, configure 
cfncluster and create a new named cluster. This in turn will lead to the last steps to 
run a large-scale compute task.

On your EC2 Launcher:

```
sudo yum update
sudo pip install cfncluster
sudo pip install --upgrade cfncluster
cfncluster configure
```

Running *configure* will produce a config file within the .cfncluster directory in your home
directory. (Use 'ls -al' to see that this exists.) A good way to get the configure steps 
correct is to follow the details at 
a web page like [this one](http://cfncluster.readthedocs.io/en/latest/getting_started.html).

```
cfncluster create PIT0
```

The cluster you create includes a head node. By default this will be a small EC2 instance (T2). 
On the AWS console in your browser you can monitor your progress 



#### A Worker program

This C code performs part of a Fourier transform on a simple dataset. In ensemble 

```
// fourier.c performs a simple Fourier transform of a small data vector
//   This is intended as a fast but non-trivial compute task.
//     Signal = a Gaussian envelope x sine wave with about 10 cycles
//     FT: i is the i'th term of the FT; a_i is the coefficient, complex 
//     a_i = Sum over n running 0 to N-1 of x_n * CE
//     CE is a complex exponential e^{ -2 * pi * i * k * n / N }
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX_N 32768
void main(int argc, char **argv)
{
    if (argc < 3) { printf("\nfourier N i: i'th coeff of an N-element signal\n\n\n"); exit(0); }
    int N = atoi(argv[1]); 
    int i = atoi(argv[2]);          printf("\nSignal length %d, term %d.\n\n", N, i);
    if (N < 0 || N > MAX_N || i < 0 || i >= N) { exit(0); }
    double s[MAX_N], ar = 0.0, ai = 0.0, pi = acos(-1.0), dN = (double)N, di = (double)i;
    double dShft = (double)(N/2), dScl = (2.0*pi*5.0)/dShft, dGScl = 2.0/dShft;
    for (int n = 0; n < N; n++) {             // signal generator block
        double dn = (double)n;                  // convert index to a floating point value
	double x = (dn - dShft) * dScl;         // ... to a number on [-5 * 2pi, 5 * 2pi]
	double xg = (dn - dShft) * dGScl;       // ... also to a number on [-2, 2]
	double g = exp(-xg*xg);                 // ... and get the Gaussian of the latter
	double m = sin(x);                      // ... and the sine of the former
	s[n] = g*m;                             // ... and compile their product into the signal vector s[]
	// printf ("%d,%lf\n"n, s[n]);
    }
    for (int n = 0; n < N; n++) {             // FT block
        double dn = (double)n;                //   dn is the sum index
        double exp_arg = -2.0*pi*(dn/dN)*di;  //   argument of the exponential
	double real_n = cos(exp_arg);         //   real component of the exponential
	double imag_n = sin(exp_arg);         //   imag component of the exponential
        ar += s[n]*real_n;                    //   accumulate
	ai += s[n]*imag_n;                    //      "
    }
    printf ("\n\ncoefficient %d = (%lf, %lf).\n\n\n"), i, ar, ai); exit(0);
}
```
  

{% include links.html %}
