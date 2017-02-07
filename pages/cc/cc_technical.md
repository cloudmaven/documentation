---
title: Cloud technical notes
keywords: cloud, introduction
last_updated: October 6, 2016
tags: [research_computing]
summary: "Cloud computing technical notes"
sidebar: mydoc_sidebar
permalink: cc_technical.html
folder: cc
---

## Introduction
This purpose of this page is to present you with important technical details of cloud computing. 

## Links
- [Example ssh usage/help](http://support.suso.com/supki/SSH_Tutorial_for_Linux)
- [Computer networking port](https://en.wikipedia.org/wiki/Port_(computer_networking))
- [Linux cURL command](http://www.computerhope.com/unix/curl.htm)
- [Access to Jupyter notebooks via ssh](https://coderwall.com/p/ohk6cg/remote-access-to-ipython-notebooks-via-ssh)
- [PuTTY on Wikipedia](https://en.wikipedia.org/wiki/PuTTY)

## Warnings
- ***The material on this page can be incredibly useful but out of context may appear a bit 'so what?'; 
we suggest skimming through here to help build your cloud context web if these topics are new to you.***
- ***Our [glossary](cc_glossary.html) may help with unfamiliar terms.***

## Ports, sockets and tunneling

Following a URL such as 123.213.101.102 you may see a colon followed by a number, as in: 123.213.101.102:8001. 
This following number is a ***port***, per wikipedia 'a networking endpoint in an operating system'. A port in 
this context means a dedicated signal wire. By directing applications to a port you build a 
dedicated send/receive connection. This is particularly useful in getting two computers to talk to one another.

For completeness there is a related concept called a [socket](https://en.wikipedia.org/wiki/Network_socket) 
which we do not need in this discussion. 

We proceed with a particularly important cloud-oriented use of ports. Suppose you have a cloud VM instance 
You wish to run some software that uses a Graphical User Interface (GUI). In this case let's consider the
common example of a [Jupyter notebook](az_jupyter.html). Here a remote Jupyter notebook server is accustomed to
talking to your machine via your local browser. 
The commands below follow [this reference](https://coderwall.com/p/ohk6cg/remote-access-to-ipython-notebooks-via-ssh).

Let's assume you log in to the cloud VM at ip address 123.213.101.102 using ssh.  
There you issue 

```
% jupyter notebook --no-browser --port=8889
```

This is directing the jupyter application to pay attention to port 8889.
Next, on your local machine, say a laptop for example, you would issue: 

```
% ssh -N -f -i ~/.ssh/credential_filename.pem -L localhost:7005:localhost:8889 username@123.213.101.102
```

This uses the ssh command. If you are using a Windows PC it is common to connect using PuTTY (see below).
The point of the command is to create a tunnel from port 7005 on your local machine to port 8889 on the 
cloud VM. 

The **-i** switch specifies an identity file (key pair access to the cloud VM). 

The **-L** switch in the command stands for **Local**.  As another example concerning 
MySQL database connections: Here is a paraphrased quote from an online ssh tutorial
[http://support.suso.com/supki/SSH_Tutorial_for_Linux](http://support.suso.com/supki/SSH_Tutorial_for_Linux):

> SSH can forward communication across an SSH session that you establish.  For example, you can 
> set up a port forward for your connection from your home machine to xyz.org such that connections to localhost 
> port 3306 forward to the remote machine's port 3306. Port 3306 is the port that the MySQL server listens on, 
> so this would allow you to bypass the normal host checks that the MySQL server would make and allow you to 
> run GUI MySQL programs on your local computer while using the database on your remote machine. Here is the 
> command to accomplish this: 
>
> ssh -L 3306:mysql.xyz.org:3306 username@kilroy.xyz.org
>
> The -L (which means Local port) takes one colon-delimeted argument. 
>
>   local-host:local-port:connect-to-host:connect-to-port 
>
> You specify what host and port the connection will go to on the other side of the SSH 
> connection.  When you make a connection to the local-host:local-port port it sends the 
> data through the SSH connection to the connect-to-host:connect-to-port port. From 
> the point of view of connect-to-host it is as if the connection 
> came from that machine.

In our example the **ssh** command for the Jupyter notebook connection stipulated port 7005 on 
localhost. Hence on your local machine you can now open a browser and enter in the address bar: 

```
localhost:7005
```

If all is well you will see the Jupyter notebook (from the cloud VM) on your browser. 

Jupyter notebooks have associated passwords; and in the case above our colleague had to set this password 
to an empty string in the Jupyter config file due to Jupyter permission default settings.  

The main point here is that the ssh protocol can be used to create tunnels into cloud VMs and 
that this particularly applies when you want to see GUI content on your local machine. 

## PuTTY

The Windows PC environment does not yet support the **ssh** command and consequently cloud VM connections typically
use the PuTTY application. (There are also 
[alternative options](http://web.archive.org/web/20130806071308/http://huddledmasses.org/scriptable-ssh-from-powershell/) ). 
PuTTY is a slightly circuitous but perfectly reliable means of connecting with a cloud VM, supporting as it does several
communication protocols including ssh. 

The main point here is that a VM credential file with a *.pem* extension does not work with PuTTY. You can use the companion
application PuTTYgen to convert this file to an equivalent file with a .ppk file extension.  The PuTTY program can then use 
this credential file to connect to a cloud VM. 

kilroy need screencap of PuTTYgen in operation and the menu location for specifying a .ppk file.

kilroy need text and screencap showing use of PuTTY to accomplish the Jupyter tunnel given above; and copy to the all Jupyter pages as well. 

## Python connections

Python has a Library to help simplify connecting to a URL. The following code is a simple program that demonstrates
an API call to one of our projects ([AralDIF](AralDIF)):

```
import urllib2
import time

def dif(calltype, date1, date2, station):
    baseAPI = 'https://araldif.azurewebsites.net/api/'
    apiExtension = calltype + '?' + 'start=' + date1 + '&' + 'end=' + date2 + '&' + 'station=' + station + '&'
    api_call = baseAPI + apiExtension
    print api_call
    t1 = time.time()
    u = urllib2.urlopen(api_call)
    t2 = time.time()
    data = u.read()
    t3 = time.time()
    print 'URL open required', t2 - t1, 'seconds; read() required', t3 - t2, 'seconds'
    return data

data = dif('gethydrograph', '1995-01-01', '2000-12-31', 'UCHKU')
print data[0:198]
```

The output of this program (the first 198 characters returned) is as follows: 

```
https://araldif.azurewebsites.net/api/gethydrograph?start=1995-01-01&end=2000-12-31&station=UCHKU&
URL open required 9.09429216385 seconds; read() required 0.0734670162201 seconds
DATE,FLOW
1995-01-01,93.787209
1995-01-02,90.740631
1995-01-03,87.948059
1995-01-04,85.219681
1995-01-05,82.500687
1995-01-06,79.934334
1995-01-07,77.52166
1995-01-08,75.218941
1995-01-09,73.028778
```

Note that establishing the connection required about 9 seconds and the data transfer less than one tenth of a second.

The importance of being able to write this code is high and can be understood as follows: 

If your research requires you to regularly go to an external data resource to make new data queries 
(updates, new ideas for looking at existing data and so on) then you traditionally carry this out by manual 
methods: Lots of clicking and dragging and waiting. The above Web Client demonstrates that this process can be 
automated; provided that the person maintaining the data service (in our example 'araldif.azurewebsites.net') 
has built and maintained their side of the automation contract. 

## Exclam

This section describes using exclam in front of a Linux command from a Jupyter frame.

## Linux connections

This section describes ssh / ftp stuff and may be kilroy redundant

## curl 

Per Wikipedia, [**curl**](https://en.wikipedia.org/wiki/CURL) is a command line tool for getting or sending files 
using [URL](https://en.wikipedia.org/wiki/Uniform_Resource_Locator) syntax. 
[See this link for Curl usage](http://www.computerhope.com/unix/curl.htm).

curl can be used in the context of an Azure-hosted Jupyter notebook to load a particular data resource (e.g. from GitHub) 
as an initialization step every time the notebook is restarted. 

{% include links.html %}
