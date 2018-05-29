---
title: JupyterHub for Research Computing
keywords: research, computing
last_updated: July 13, 2017
tags: [research_computing, reproducibility, Jupyter, data_science, cloud_basics, web_framework]
summary: "Installing and Using JupyterHub for research computing"
sidebar: mydoc_sidebar
permalink: rc_jupyterhub.html
folder: rc
---

## Introduction

- Jupyter Notebooks are -- briefly -- powerful interactive data science laboratories. 
- Jupyter Hubs are centers that disperse and support Jupyter Notebooks to a User community: Scientists, students, 
research teams and the like. 


This page describes the operation of a JupyterHub instance on the public cloud. We provide a walk-through
and conceptual framework for both installation and operation. The cloudmaven.org working instance is 
not public.  However a Jupyter Notebook service is provided at no cost by the Microsoft Azure team; 
see [this link](http://notebooks.azure.com).


Our first implementation is built on the AWS public cloud.  We address cost management, 
provision of fully functional working environments for the User pool, software versioning, 
data access, ingress and egress. We rely heavily on Anaconda here; but a future revision 
will include kubernetes/docker-based scaling. That is: By scaling up the Jupyter Hub can
serve larger groups of people. 


## Facets of the JupyterHub framework


- Set up a machine instance (or instances: to manage *many* users)
- Create options for pre-built collections of Jupyter Notebooks. We will call these Libraries
- Build a computation environment that includes Python and necessary Python packages 
- Establish a User pool with authentication by each User; we use OAuth with GitHub for this
  - Cascade of User groups
    - root: propagate User-built environments as notebook kernels (as dropdown menu choice) 
      - From the User perspective: I customize a working environment and it is easy for anyone to use
    - admin: can ssh into VMs to modify groups and owners; and can sudo install packages
      - this avoids collisions and other uncomfortable outcomes from power users = admin
    - power users: can configure their own conda environment
    - student users
- Create a disk volume appropriate for datasets in common use by the User pool
- Ensure that each User has a PATH environment variable appropriate to the work they are doing
- Establish a cost management plan that minimizes operational cost without creating User inconvenience
- Establish an upload mechanism where a User can push files to their environment
- Establish a download mechanism where results (e.g. result files) can be pulled onto a local machine
- Establish a GitHub repository connection whereby the User can synchronize their progress
- Further manage costs through images and object storage when hot environments are not needed is not needed
- Support an Integrated Development Environment (IDE) called JupyterLab
- Support static (render/display) visualization (%pylab inline etc)
- Support dynamic visualization
  - Note that javascript / Python interoperability has led to excellent advances


## Use Cases


This document and the JupyterHub implementation at 
https://jupyterhub.cloudmaven.org are driven by the following use cases.


- **Course**
  - Professor X is teaching a course with 50 students
  - Uses Python and R 
  - Connects to external (astronomy) data sources
- **NeuroHackweek**
  - One-week 'hackathon' with lots of domain-specific (neuro-imaging) work involved
- **GeoHackweek**
  - One-week 'hackathon' with lots of domain-specific (geospatial) work involved
- **research team**
- **Jupyterhub demonstration**
  - Show Jupyterhub in action, particularly in talks
- **IOT study**
  - University HVAC/power-consumption study 
  - Includes access to a SQL Server RDS instance
- **Hyrdology study**
  - Intent: Involve DASC cluster scheduler
- **High Mountain Asia study**
  - Collateral to a highly secured NASA system to help illustrate practical advantages of an open data approach


## Imperatives from Use Cases


This section calls out certain features and details are called out and briefly defined.
- Installing and working with Anaconda 
- Scaling machine size
- Scaling number of machines
- Kubernetes/Docker approach
- GCP autoscaling
- DASK and cluster computing
- GitHub connectivity
- Reproducible configurations (kernels)


## Links


- [JupyterHub](https://jupyterhub.readthedocs.io/en/latest/)
- [Install Jupyterhub remotely](https://github.com/jupyterhub/jupyterhub/wiki/Installation-of-Jupyterhub-on-remote-server)
- [Interactive data visualization in Jupyter](https://www.youtube.com/watch?v=p7Hr54VhOp0)


## Admonitions and warnings


- The basic installation is not too challenging
- The customization of environments is challenging ('Hey why doesn't PIL display my image?')
- User account security is managed via a whitelist of GitHub usernames and Linux permissions


## Terms


- Jupyterhub: A multi-user server that manages and proxies multiple instances of the single-user Jupyter notebook server
- [Jupyterlab](https://www.youtube.com/watch?v=p7Hr54VhOp0): A contextual support/development environment for Jupyter notebooks
- Jupyter notebook: a web app for creating and sharing data science workspaces that include live code, equations, visualizations and narrative text
- nodejs/node.js: A lightweight, efficient javascript runtime (execution engine)
- npm: node package manager associated with nodejs


## Procedural 


Procedures here follow the recipes in the links provided with minor notes and changes. 


1. Spin up (start) an AWS EC2 Ubuntu instance (root username is 'ubuntu')
  - Suggest first time use a small ('micro') instance for practice
  - The following steps presume you are logged on to this machine e.g. using ssh or PuTTY


2. Install Linux Anaconda 
  - Anaconda conveniently installs Python, Jupyter Notebook, other commonly used scientific computing packages
  - Go to [Continuum Analytics - Anaconda Downloads](https://www.continuum.io/downloads)
  - Under Linux Anaconda Installation (copy link of 64 bit):
  - On Terminal


    `$ wget https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda2-4.0.0-Linux-x86_64.sh`


  - This gets the Anaconda*.sh file
  - Install it with


    `bash Anaconda2-4.0.0-Linux-x86_64.sh`


  - Enter yes (many times) >> provide directory or keep default
  - You may have to load your default bash profile


    `type source ~/.bashrc to load your default bash profile`

 
3. Installing Python3 (dependency of jupyterhub is on python3) and nodejs/npm (node package manager)


    `$ sudo apt-get install python3-pip`
    `$ sudo apt-get install npm nodejs-legacy`


4. Install proxy with npm


    `$ sudo npm install -g configurable-http-proxy`


5. Install Jupyterhub


    `$ sudo pip3 install jupyterhub`

 
6. Install Jupyter notebook (/upgrade)


    `$ sudo pip3 install --upgrade notebook`


7. Test Jupyterhub default configuration


    `$ jupyterhub --no-ssl`


    - This starts the session in localhost:8000 (i.e. on port 8000)
    - Connect from a browser on your local machine to http://server_ip_address:8000
    - Ensure this port is not protected / firewalled

8. Recommended: Use a secure SSL certificate file for the public facing interface of the proxy
    - Produce personal security certificates as follows:

    `$ openssl req ­-x509 ­-nodes ­-days 365 ­-newkey rsa:1024 ­-keyout mykey.key ­-out mycert.pem`
    
    - Fill in credentials
      - kilroy would like clarification on this cryptic remark: 'Even if you dont..It's ok!'


9. Create Jupyterhub configuration file


    `$ jupyterhub --generate-config`


10. We use Github OAuthentication as our Authenticator,  as follows:

  1. On the top left hand corner of Github.com, Go to your Github profile (click on profile icon) > Settings > Oauth application (under Developer Settings)

    - it is more convenient to not use capital letters in GitHub usernames

  2. Register new application

  3. Under callback URL is: [https://your_host/hub/oauth_callback](http://www.example.com)

    Where **your­host** is where your server will be running. For example, mine is at: https://52.35.105.145/hub/oauth_callback

  4. click on Register application.

   You will see Client id and secret key generated above:

        ```
        Github client_id = '---­­­­­­­Some cryptic string----­­­­­'
        Github client_secret = '­­­­­­­---­­­­­­­Some cryptic string----­­'
        ```

11. Install OAuthenticator:

    `$ sudo pip3 install oauthenticator`

12. Create **userlist** file

    `$ sudo nano userlist`

    Enter the Github username and role of the user. For example:

    ```
    amandalehr admin
    robfatland admin
    aaarendt 
    ```

13. Create these users in your server machine:

    For ubuntu:
    
    `$ sudo adduser amandalehr`

    fill in credentials. & repeat same for other users.

14. Create Default Directory for your Jupyter Notebooks:

    `$ sudo mkdir /home/amandalehr/notebooks`

    So now all users notebooks will be under `~/notebooks` directory

    * Make sure to give full access to notebooks folder to your user (read/write/execute). You can check current access with:
    
    `$ ls -la notebooks`


15. Now Edit `jupyterhub_config.py` as follows:

    `$ sudo nano jupyterhub_config.py`

    ```python
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    # Application configuration
    #-----------------------------------------------------------------------------------------------------------------------------------------------------

    # This is an application.
    c.JupyterHub.authenticator_class = 'oauthenticator.GitHubOAuthenticator'
    c.GitHubOAuthenticator.oauth_callback_url = 'https://your_ip_addrees/hub/oauth_callback'
    c.GitHubOAuthenticator.client_id = '---­­­­­­­Some cryptic string----­­­­­'
    c.GitHubOAuthenticator.client_secret = '---­­­­­­­Some cryptic string----­­­­­'
    # This is an application.
    # create system users that don't exist yet
    c.LocalAuthenticator.create_system_users = True
    c.Authenticator.whitelist = {'amandalehr', 'robfatland', 'aaarendt'}
    c.Authenticator.admin_users = {'amandalehr', 'robfatland'}
    c.Spawner.notebook_dir = '~/notebooks'
    c.JupyterHub.ssl_cert = 'mycert.pem'
    c.JupyterHub.ssl_key = 'mykey.key'
    c.JupyterHub.cookie_secret_file = '/home/ubuntu/jupyterhub_cookie_secret'
    c.JupyterHub.proxy_cmd = ['/usr/local/bin/configurable-http-proxy']

    # Let the Systemctl aware of all the environment path
    import os
    for var in os.environ:
        c.Spawner.env_keep.append(var)
    ```
    
    Ctrl + X and press 'Y' for yes to save this file.

17. Now starting jupyterhub with above configuration
    
    `$ jupyterhub`

    Go to https://your_ip_address:8000

    Your browser will raise "Untrusted certificates". 
    click on "Proceed anyways"

    * It will show "Sign-in with Github"
    * After clicking on it, It will redirect the page to **Github login page**
    * Then if you are Admin then screen will have control panel

    Enjoy start server and enjoy Jupyter Notebook.

18. If you want to install Python2 kernel in Jupyter Notebook.
    These are steps to follow : 

    * Check already existing kernels

        `$ sudo jupyter kernelspec list`

    * Install ipykernel package

        1.`$ sudo python -m pip install ipykernel`

        if you dont have pip (of python2)

            1.`$ sudo apt-get install python-pip`

            if you get compilation error as :

                ```
            --------------------------------------------------------------
                #include "Python.h"
                                ^
            compilation terminated.
            error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
            --------------------------------------------------------------
                ```

            2.Then use following command:

            `$ sudo apt-get -y install python-zmq`

            Again do step 1) of 'ipykernel' and see whether it installs or not.

        2. Installing python2 kernel with `ipykernel`

            `$ python2 -m ipykernel install`

            instead of python you can add address of python2 directory also.

            1. Another hack would be 

                1) Inside  - `/usr/local/share/jupyter/kernels/python2/kernel.json`

                2) Edit - "argv" address : `/home/ubuntu/anaconda2/bin/python2.7`

                    ```
                            {
                             "display_name": "Python 2",
                             "language": "python",
                             "argv": [
                              "/opt/anaconda2/bin/python2.7",
                              "-m",
                              "ipykernel",
                              "-f",
                              "{connection_file}"
                             ]
                            }
                    ```
                    ** Make sure that addreess is accessible to all otherwise it will raise `permissionError: [Errno 13] Permission denied failed to start kernel`


## Run jupyterhub as a system service

1. edit `/lib/systemd/system/jupyterhub.service` and `/etc/systemd/system/jupyterhub.service` as follows:

   ```bash
   [Unit]
   Description=Jupyterhub

   [Service]
   User=root
   Environment="PATH=/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/opt/anaconda3/bin"
   ExecStart=/usr/local/bin/jupyterhub -f /home/ubuntu/jupyterhub_config.py

   [Install]
   WantedBy=multi-user.target
   ```

2. `sudo systemctl daemon-reload` to load the config

3. Now you can manage it using `sudo systemctl <start|stop|status> jupyterhub`

4. To ensure it runs at startup `systemctl enable jupyterhub.service`

 Refer <https://github.com/jupyter/jupyterhub/wiki/Run-jupyterhub-as-a-system-service>

 ** Make sure all file link given in `jupyter_config.py` are proper.


## Configure a custom environment

- Get your kilroy sysadmin to give you correct permissions
- Log in to Jupyterhub
- Open a terminal
- Insert a new path into your PATH variable


```
prompt> export PATH=/opt/anaconda/bin:$PATH
```

- create a new kernel named **awesome** (notice the prompt changes when you activate):


```
prompt> conda create -n awesome anaconda
prompt> source activate awesome

(awesome) prompt>
```

- In your activated kernel install some custom software
  - Some packages are part of Anaconda: pyodbc, scikit-learn, JSAnimate, ipywidgets, dask
  - Other packages may be outside the ken of conda install: azure-sdk-for-python and so on. 


```
(awesome) prompt> conda install networkx
(awesome) prompt> conda install boto3
(awesome) prompt> conda install xarray
```


- De-activate the kernel. 

```
(awesome) prompt> source deactivate

prompt>
```


{% include links.html %}
