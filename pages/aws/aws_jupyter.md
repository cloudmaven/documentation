---
title: AWS Procedural
keywords: jupyter
last_updated: January 26, 2017
tags: [AWS]
summary: "Jupyter Notebook on AWS"
sidebar: mydoc_sidebar
permalink: aws_jupyter.html
folder: aws
---

## Introduction

The purpose of this page is to overview AWS-oriented approaches to creating and using Jupyter notebooks, 
specifically by getting them running on EC2 instances. 
We describe both a *standard* server-based approach with some shareability features and a *personal* approach
which makes use of an ssh tunnel. The latter is also described on [this technical page](cc_technical.html).
A third approach is to create a static instance on GitHub and a fourth approach is to clone such a GitHub 
repo (but these are not AWS-oriented approaches).  For completeness: We also mention the option 
described [here](az_Jupyter.html).


## Links

- [Jupyter notebooks](https://jupyter.org/)
- [AWS Jupyter Server instructions](http://chrisalbon.com/jupyter/run_project_jupyter_on_amazon_ec2.html)
- [Our middle-school math club demo notebook](https://notebooks.azure.com/library/89FHPIGSGMs)

## Warnings
***We outline two approaches here, one for a non-shared notebook and one for shared. The shared form
is a nice collaborative tool but has two drawbacks: First you give **write** access to anyone with whom
you share the password and second (in early 2017) your browser balks at the non-secure connection so
it seems a bit sketchy. A third option would be to place the notebook files on GitHub and share them 
through the standard cloning mechanism.***

## Before getting started
In the introduction above we mention no less than five approaches to operating Jupyter notebooks.
Here we concentrate on the first two, both on AWS EC2 instances, so let's begin by describing these
at a high level.

### Approach one: A personal Jupyter notebook with ssh tunnel

Suppose that you just need a Jupyter notebook for your own research; you do not need to share the 
contents or the development process with anyone. To do this on an EC2 instance you would first 
create that instance; then install Jupyter; and then... you are ready to go but you don't have an
obvious way of getting the Jupyter notebook to appear in your browser. Enter **ssh tunneling**
which we [here](cc_technical). 

### Approach two: A shared Jupyter notebook

Suppose instead that you would like to share access to a Jupyter notebook on an EC2 instance with
a few colleagues. You can follow the directions given at the website provided above; and these are
supplemented in the notes that follow below. Here you will not be using your key pair credentials
to connect to the EC2 instance. Rather you will configure it to run on the internet at some URL 
where access will be controlled by means of a password. 

This latter approach has the disadvantage that your colleagues can edit your notebook files. 
If this is your intent then great; but it might be wise to back up the Notebook collection 
some place from time to time. The other down-side is that there is some sort of security issue
flagged by your browser as you connect to the Jupyter server. So this solution is not yet 
perfect; but as this is an active area of community work it may already be much improved by
the time you read this. 

### In either case

Sometimes EC2 instances reboot; and when they do they stop running the Jupyter server. It is 
generally re-started manually. However the rc startup file structure can be configured to 
re-launch Jupyter when your EC2 instance reboots. (kilroy is this documented here yet?)

## Procedural 

As noted above [this link](http://chrisalbon.com/jupyter/run_project_jupyter_on_amazon_ec2.html) is the
latest we have found for instructions on setting up an EC2 instance as a Jupyter notebook.  You may also
find useful help 
[here](http://jupyter-notebook.readthedocs.io/en/latest/public_server.html).
The instructions we give below may *also* be of use; but we consider them deprecated. 

### Setting up a public Jupyter Notebook server

- Spin up an AWS instance with Ubuntu AMI and install [Anaconda](https://docs.continuum.io/anaconda/install)
- Install Jupyter Notebook 

```
% sudo apt-get install jupyter-notebook
```

- Once you've installed Jupyter Notebook, follow the steps below:

```
% bash
% jupyter notebook --generate-config 
```

Then launch ipython and generate a hashed password to add to the configuration file you generated:

```
% bash
% ipython

In [1]: from notebook.auth import passwd
In [2]: passwd()
Enter password:
Verify password:
Out[2]: 'sha1:----very_long_string_of_characters-------------------'
```

The "sha1:---etcetera" string will be used below in a configuration file.

Next: Generate a self-signed certificate using openssl so that your hashed password is encrypted

```
$ openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mykey.key -out mycert.pem
```

Set Jupyter Notebook to use the certificate when it starts: 

```
$ jupyter notebook --certfile=mycert.pem --keyfile mykey.key
```

You can also set the Jupyter Notebook to use the certificate when it starts by editing the configuration file:


```
$ vi ~/.jupyter/jupyter_notebook_config.py
```

You will want to add the following lines to the config file (or uncomment those lines -- remove the hashes): 

```bash
# Set options for certfile, ip, password, and toggle off
# browser auto-opening
c.NotebookApp.certfile = u'/absolute/path/to/your/certificate/mycert.pem'
c.NotebookApp.keyfile = u'/absolute/path/to/your/certificate/mykey.key'
# Set ip to '*' to bind on all interfaces (ips) for the public server
c.NotebookApp.ip = '*'
c.NotebookApp.password = u'sha1:bcd259ccf...<your hashed password here>'
c.NotebookApp.open_browser = False

# It is a good idea to set a known, fixed port for server access
c.NotebookApp.port = 9999
```

Note: You will also want to open the port on your AWS Portal (using the Security Groups and Inbound rules)

Note: If http://ipaddress:9999 doesn't work, use https://ipaddress:9999.  

### Creating Alarms for Jupyter Notebook Service

kilroy this part is not in place yet

## Jupyter notebook auto-restart

This section describes how to set your Jupyter notebook server to start automatically on reboot so you do not 
have to log in to your EC2 instance and type "jupyter notebook" whenever it restarts -- which might be once 
every couple days or so.

The example below assumes the Jupyter notebook server is installed through Anaconda. 
It also assumes that you have an EC2 instance running Ubuntu. 

Download this [init.d script](https://gist.github.com/Doowon/38910829898a6624ce4ed554f082c4dd) and save 
it on your EC2 instance as /etc/init.d/jupyter

Edit the file and change this line:

> DAEMON=/home/ubuntu/anaconda3/bin/jupyter-notebook

Make sure there is a /var/log/jupyter/ folder; if necessary create one using **mkdir**. You may need to use **sudo**.

The folowing commands are issued from the command line. Respectively they make the init.d file executable, 
generate a Jupyter config file, start the jupyter service, update the rc process, and stop the jupyter service. 

kilroy the above text does not adequately explain what the user is doing.

```
% sudo chmod +x /etc/init.d/jupyter
% sudo jupyter --generate-config -f /etc/jupyter/jupyter_config.py
% sudo service jupyter start
% sudo update-rc.d jupyter defaults
% sudo service jupyterhub stop
```



{% include links.html %}
