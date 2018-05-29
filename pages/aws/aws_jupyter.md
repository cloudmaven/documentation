---
title: Jupyter on AWS
keywords: jupyter
last_updated: January 26, 2017
tags: [AWS, Jupyter, cloud_service, reproducibility, visualization, github, research_computing, data_science, collaboration, python]
summary: "Jupyter Notebook on AWS"
sidebar: mydoc_sidebar
permalink: aws_jupyter.html
folder: aws
---


# Introduction


This page covers AWS-based (EC2) Jupyter notebooks. We describe a 
a *personal* approach using an ssh tunnel and 
*standard* server-based approach with some shareability features.
The ssh tunnel business is also described on [this technical page](cc_technical.html).
Aside from AWS or other public cloud VMs there are many other facets to Jupyter notebooks. 
You can make use of hosting services like Azure Notebooks or Google CoLab, you can create static 
views of Jupyter notebooks on GitHub, you can clone Jupyter notebook repositories from GitHub, 
you can explore other options e.g. as described [here](az_Jupyter.html), you can integrate
Jupyter notebooks with containers... it is in short a popular technology (for good reason)
with some attendant complexity.  As always the ability to find help online (Stack Overflow, 
GitHub, etcetera) will be invaluable.


## Links


- [Jupyter notebooks](https://jupyter.org/)
- [AWS Jupyter Server instructions](http://chrisalbon.com/jupyter/run_project_jupyter_on_amazon_ec2.html)
- [Our middle-school math club demo notebook](https://notebooks.azure.com/library/89FHPIGSGMs)


## Warnings


***We outline two EC2-based approaches here, shared and non-shared. The shared form is a nice 
collaboration tool but has two drawbacks: First you share **write** access with anyone you give
the password to and second (in early 2017 anyway) there is some browser security complaining 
that you must push past. This seems a bit sketchy.*** 



## Approach one: Personal Jupyter notebook, ssh tunnel


### Overview


You would like a Jupyter notebook for (say) some research; and sharing is not high on the priority list 
at the moment.  This section runs through this in moderate detail.  The crucial idea here is that the EC2
instance has Jupyter installed; and you run this without a browser connection. Rather you direct the jupyter
process to pay attention to a particular *port* on the machine. Then you securely connect to that port 
from your own machine using ssh and then finally connect from your local browser. This is an alternative 
to remote desktop ideas which of course would also work. 


The method of connecting machines via ssh we refer to as **ssh tunneling**. 


In what follows we work from a Windows machine with the bash shell installed. That is, bash commands
like ssh are run in a bash terminal window.  This is how the port configuration is done. One can check 
port status on a local machine using:  


```bash

sudo lsof -i :port number

``` 

Open ports must be closed before they can be re-used. 


### Starting up an EC2 instance to host the Jupyter notebook server


- Log into the AWS console as an IAM User with (say) admin privilieges
- Use the EC2 wizard to Start and EC2 instance
  - See [this page](https://cloudmaven.github.io/documentation/aws_ec2.html) for more on configuring EC2 instances. 
  - Choose AWS Linux 
    - Notice that the login name for this version of Linux is ec2-user
  - The ip address will not be fixed unless you grant this machine one of your elastic ip addresses
    - You will need to be aware that it changes as you stop and re-start the instance
  - An m5.large instance has a modest amount of processing power and costs 11 cents per hour
    - It is good practice to attach a data drive based on the needs of the work
    - Both the EC2 instance and the attached data drive (EBS) should be tagged with a Name that clearly indicates what the instance is being used for
    - Enable logging and encryption on the data drive if you are interested in keeping the data secure
    - A 100 GB data drive costs 10 cents per GB-month; so that comes to $10 per month
  - To access this EC2 instance we use a key-pair file with file extention **.pem**
    - If using PuTTY you must use the PuTTYGen sister-application to convert the file to a **.ppk** file. Instructions are easy to find online. 
    - You download this file in the process of using the AWS console to start the EC2 instance
    - Save it some place safe and far away from any GitHub repositories you may have 
    - The sftp and ssh switch to point to the key-pair file is the same: **'-i keypair_file.pem'**
  - In preparation for operating your EC2 instance you should consider the cost of leaving it running versus the cost of stopping it
    - In the case of 11 cents per hour keeping the machine on over the weekend will cost about six dollars
    - Over the course of a month this machine will cost about $90
    - If you diligently Stop this machine at the end of each day and use it 32 hours per week it will cost you $15 per month
    - Your personal time to Stop an instance is about 2 seconds plus the time required to log in to the AWS console (maybe 30 seconds)
    - Your personal time to Stop an instance if you use the AWS command line with an alias for the command is 2 seconds
      - This would be nice to write up here (kilroy) and that should be combined with some means of tracking the shifting ip address 


Let's assume your EC2 is now running with ip address 123.12.123.12.  Certain steps such as this one require you to confirm with 'yes' etcetera
so that is assumed. Also I will differentiate your local machine with the prompt L$ and the EC2 instance with the shell prompt EC2$.
Again your user login is 'ec2-user'. Log in to your AWS EC2 instance using bash from your machine; and then update it:


```bash
L$ ssh ec2-user@34.211.12.186 -i rob_HPRC_poc_key_pair.pem


(various messages)


EC2$ sudo yum update
```


Determine that the EC2 operating system volume (by default 8 GB) is mounted but the data drive is not.
Then use lsblk to find the designation for the data drive. 


```bash
EC2$ df


EC2$ lsblk 


NAME     MAJ:MIN   RM   SIZE   RO   TYPE    MOUNTPOINT
nvme1n1  259:0      0   100G        disk
(etc)
```


Notice that the size 100G matches the selected EBS volume (from the configuration Wizard above).
Mount the data drive on your EC2 operating system. This will make the 100 GB of storage available.
In this example the data drive is designated **/dev/nvme1n1**.



```bash
EC2$ sudo mkdir /data


EC2$ sudo mount /dev/nvme1n1 /data


EC2$ mount -l


EC2$ cd /data


EC2$ df .
```


### Locations and a security note


The data drive should be present and empty.  Your home directory **/home/ec2-user** is located on the root drive. This is not encrypted. 
The /data drive was configured as encrypted.


### Remaining goals


With an EC2 instance running with attached 100 GB EBS drive we are ready to install the Jupyter notebook server with both **Python 3**
and **R** kernels available.  


>> **A Few Notes:** Logging in as 'ec2-user' with ssh (and the key pair file) is independent of any AWS IAM User identity. 
>> You do not need the latter to log in to the EC2 instance. Furthermore when you are logged in as ec2-user you can run **sudo**.
>> If you attempt to connect to the EC2 and it fails to respond: Its ip address may have changed or it may simply be *stopped*.
>> Re-starting it can be done from the console or using the AWS command line interface (cli).  The EC2 instance has the cli
>> pre-installed but not configured; this topic is discussed further elsewhere as it is not directly relevant here.
>> Uploading data to this EC2 instance can be done using secure ftp **sftp**. In doing so the data should as a matter of 
>> best practice be saved on **/data**, the added EBS volume.


### Install Anaconda and hence Jupyter


[Jupyter notebook server nstallation website](http://jupyter.readthedocs.io/en/latest/install.html)


...first step is to [install Anaconda](https://www.anaconda.com/download/) but in fact using **wget**
so I found a stack overflow search result: 


```bash
EC2$ wget http://repo.continuum.io/archive/Anaconda3-4.3.0-Linux-x86_64.sh
EC2$ bash Anaconda3-4.3.0-Linux-x86_64.sh
```


It is fine to install this in the ec2-user home directory. Again this is a single machine - single user 
configuration.  I did accept the option to prepend the path onto PATH so **conda** will run properly. 
I find I must log out and log in again for this to take effect (or perhaps just run .bashrc...) 
Jupyter comes with Anaconda so no more installation is required until we get to **R**.  The command


```bash
EC2$ jupyter notebook
```


will now run but won't do anything useful since there is no available browser.


### Install **R**


The install of **R** is a single line. We also indicate starting and quitting the R command console.


```bash
EC2$ conda install -c r r-essentials


EC2$ R


R version 3.4.1 (2017-06-30) -- "Single Candle"
etcetera


> q()
```


### Connect (tunnel) from your local machine to the EC2 Jupyter notebook server


[This page](https://cloudmaven.github.io/documentation/cc_technical) discusses the tunneling
process. Again the local command prompt is **L$ ** and the EC2 command prompt is **EC2$ **.


```bash
EC2$ jupyter notebook --no-browser --port=8889 
```

This command will produce a very long token string such as *a377a0a7b23bf9bfed9d48347c7cbaf338e0b8fd29aedbc6*.
Retain this token string for your first time connecting with the Jupyter server. 


Note that this jupyter notebook server is now a running process on the EC2 instance. If you halt that
process there will be no service. You have a couple of options for keeping it going. First: Don't do anything; 
just minimize the terminal window and leave it alone. This has the advantage that if the server halts you 
can easily restart it (provided you are still logged in to the EC2 instance). If you like you can run the 
process in the background, for example through ctrl-z and 


```bash
EC2$ bg
```

You can also start it as a background process using


```bash
EC2$ (jupyter notebook --no-browser --port=8889) &
```


However this is accomplished the main idea is to leave the EC2 instance in a state of *'watching'* port 8889
for activity. This is what your local machine's browser will connect to.


On the local machine issue: 


```bash
L$ ssh -N -f -i keypair_file.pem -L localhost:7005:localhost:8889 ec2-user@123.12.123.12
```


Now localhost port 7005 will be connected to port 8889 on the EC2 instance by means of the authentication keypair file.
The ip address will as noted change upon stopping and re-starting the EC2 instance. The user name **ec2-user** is fixed.
Naturally one could configure multiple users on the EC2 instance in the normal fashion; but that is not covered here.


Next open a browser tab and type in the address window:


```bash
http://localhost:7005
```


Upon hitting Enter this should connect to the Jupyter notebook server, giving you a listing of any existing notebooks
and the option to start new ones, either with the Python 3 kernel or the R kernel. It may be necessary to enter the
token string you recorded above.  


If your subsequent work is important
we strongly encourage binding your notebook folder to a GitHub repository, again taking care not to include any keypair files. 
Doing regular synchs with GitHub will protect your work from accidental loss. 
Notice that the keypair.pem file is never imported onto the EC2 instance; it resides only on your local computer. 


We also reiterate that stopping and re-starting the EC2 instance is a matter of a few seconds action at the console.
The start time is typically 2 minutes, possibly enough time to get some coffee. The trick in stopping and re-starting
is to adapt easily to the new ip address of the EC2 instance.  The simplest way to do this is by means of an elastic 
ip address, an AWS feature that keeps an EC2 at a single ip address regardless of start/stop state.


The EC2 instance must be running
the Jupyter notebook server -- possibly in the background -- with the **--no_browser** and **--port=8889** arguments.
There is nothing particularly magical about port 8889 or 7005 as far as we know. Some ports are 'spoken for' and 
should be avoided but these work fine in our experience. 


If you decide that your software is running too slowly on the EC2 instance you do have the option of **stopping**
the instance and then **re-starting** it on a more powerful machine. This can be done for example in the console
very easily. A more powerful machine costs more per hour but should complete the task in less time, meaning that
the cost to you is roughly equivalent... you simply have a shorter wait. But benchmark to be sure this is the case.


### Preserving the EC2 instance as an Amazon Machine Image


Stopping the running instance places it 'on hold' so that you do not pay the hourly rate. You can also choose
to create an Amazon Machine Image (AMI) from your stopped instance. This acts as a template that you can use
to spawn more instances. This might be useful in a collaboration context for example.  It also means that if
you want to pick up where you left off at some point down the line you do not have to go through all of these
configuration steps again. 


## Approach Two: A shared Jupyter notebook


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

```bash
% sudo apt-get install jupyter-notebook
```

Once you've installed Jupyter Notebook, follow the steps below:

```bash
% jupyter notebook --generate-config 
```

Then launch ipython and generate a hashed password to add to the configuration file you generated:

```bash
% ipython

In [1]: from notebook.auth import passwd
In [2]: passwd()
Enter password:
Verify password:
Out[2]: 'sha1:--long_string_of_characters--'
```

The "sha1:--string--" is a hashed password. It is used below in a configuration file.

Generate a self-signed certificate using openssl so that your hashed password is encrypted

```bash
$ openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mykey.key -out mycert.pem
```

Set Jupyter Notebook to use the certificate when it starts: 

```bash
$ jupyter notebook --certfile=mycert.pem --keyfile mykey.key
```

You can also set the Jupyter Notebook to use the certificate when it starts by editing the configuration file:

```bash
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
