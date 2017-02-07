---
title: Jupyter on AWS
keywords: jupyter
last_updated: January 26, 2017
tags: [AWS]
summary: "Jupyter Notebook on AWS"
sidebar: mydoc_sidebar
permalink: aws_jupyter.html
folder: aws
---

## Introduction

The purpose of this page is to overview AWS-based (EC2) approaches to creating and using Jupyter notebooks, 
We describe a *standard* server-based approach with some shareability features and a *personal* approach
which makes use of an ssh tunnel. The latter is also described on [this technical page](cc_technical.html).
Aside from AWS you can also create a static Jupyter notebook on GitHub, you can clone a Jupyter repo from
GitHub and you can also explore the option described [here](az_Jupyter.html).

## Links

- [Jupyter notebooks](https://jupyter.org/)
- [AWS Jupyter Server instructions](http://chrisalbon.com/jupyter/run_project_jupyter_on_amazon_ec2.html)
- [Our middle-school math club demo notebook](https://notebooks.azure.com/library/89FHPIGSGMs)

## Warnings

***We outline two EC2-based approaches here, shared and non-shared. The shared form is a nice 
collaboration tool but has two drawbacks: First you share **write** access with anyone you give
the password to and second (in early 2017 anyway) there is some browser security complaining 
that you must push past. This seems a bit sketchy.*** 

## Before starting 
In the introduction above we mention five approaches to using Jupyter notebooks.  Here we 
concentrate on the first two of these, both on EC2 instances.

### Approach one: Personal Jupyter notebook, ssh tunnel

Suppose you need a Jupyter notebook for your own research; you do not need to share it with 
anyone. You create an EC2 instance, get the *.pem* key pair file, install Jupyter on the instance
and that's it, you are ready to go... except that you don't have an obvious way of getting the 
Jupyter notebook to appear in a browser (because it the Jupyter server is running remotely). 
The solution: **ssh tunneling** as described [here](cc_technical). 

### Approach two: A shared Jupyter notebook

Suppose that you would like to share access to a Jupyter notebook on an EC2 instance with a few colleagues
via a URL and a simple password. Follow the directions given 

- [here](http://chrisalbon.com/jupyter/run_project_jupyter_on_amazon_ec2.html)
- [or here](http://jupyter-notebook.readthedocs.io/en/latest/public_server.html)

Approach two has two differences from Approach one: First your colleagues can edit the 
notebook files. (It may be wise to periodically back them up.) Second as of 2017 the connection
seems to be non-secure and a bit sketchy. 

## Our notes on Approach Two

The links we give above or a quick internet search are quite possibly better resources than our
notes given here.

- Spin up an AWS instance with Ubuntu AMI and install [Anaconda](https://docs.continuum.io/anaconda/install)
- Install Jupyter Notebook 

```
% sudo apt-get install jupyter-notebook
```

Once you've installed Jupyter Notebook, follow the steps below:

```
% jupyter notebook --generate-config 
```

Then launch ipython and generate a hashed password to add to the configuration file you generated:

```
% ipython

In [1]: from notebook.auth import passwd
In [2]: passwd()
Enter password:
Verify password:
Out[2]: 'sha1:--long_string_of_characters--'
```

The "sha1:--string--" is a hashed password. It is used below in a configuration file.

Generate a self-signed certificate using openssl so that your hashed password is encrypted

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

```
# Set options for certfile, ip, password, and toggle off
# browser auto-opening
c.NotebookApp.certfile = u'/absolute/path/to/your/certificate/mycert.pem'
c.NotebookApp.keyfile = u'/absolute/path/to/your/certificate/mykey.key'
# Set ip to '*' to bind on all interfaces (ips) for the public server
c.NotebookApp.ip = '*'
c.NotebookApp.password = u'sha1:--long_string_of_characters--'
c.NotebookApp.open_browser = False

# It is a good idea to set a known, fixed port for server access
c.NotebookApp.port = 9999
```

Note: You must open port 9999 on the EC2 instance. You can do this from the AWS console using the 
Security Groups and Inbound rules.

Note: If http://ipaddress:9999 doesn't work, use https://ipaddress:9999.  

## Creating Alarms for Jupyter Notebook Service

kilroy this part is not in place yet; see source nbk

## Jupyter notebook auto-restart

This is how you manually start / stop a Jupyter server:

```bash
% sudo service jupyter start
% sudo service jupyter stop
```

You may also want to delve into the difference between these two commands: 

```bash
% jupyter notebook
% nohup jupyter notebook
``` 

The first will halt when you log off the machine; the second uses 'nohup' to make the process 
persist in the background so you can log out. ('nohup' is short for no hang-up; a holdover from
phone modem days.)

This manual starting and stopping can get tedious (tm Isabella Boom); so this section describes how to 
set your Jupyter notebook server to start automatically on reboot.  As noted your EC2 instance may
restart as often as every couple days or so.  The notes below assume the Jupyter 
notebook server is installed through Anaconda.  It assumes that you have an 
EC2 instance running Ubuntu. 

Download [this script](https://gist.github.com/Doowon/38910829898a6624ce4ed554f082c4dd) and save it 
on your EC2 instance as /etc/init.d/jupyter.  Edit this file to make this modification:

```
> DAEMON=/home/ubuntu/anaconda3/bin/jupyter-notebook
```

Make sure there is a /var/log/jupyter/ folder. If necessary create one using **sudo mkdir**.

Issue the following sequence from the command line: Respectively these make the init.d file executable, 
generate a Jupyter config file, and update the rc process to include your Jupyter service.
Once this is done you can reboot the instance and make sure the Jupyter service starts properly.

```bash
% sudo chmod +x /etc/init.d/jupyter
% sudo jupyter --generate-config -f /etc/jupyter/jupyter_config.py
% sudo update-rc.d jupyter defaults
```



{% include links.html %}
