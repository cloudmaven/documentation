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

The purpose of this page is to walk through the installation of JupyterHub on a remote server: e.g. on an AWS instance. JupyterHub helps to create a multi-user hub to serve Jupyter Notebooks. 

The procedures here mostly follow the recipe outlined in the links provided below with minor notes and changes. 

## Links
[JupyterHub](https://jupyterhub.readthedocs.io/en/latest/)
[Installation of Jupyterhub on remote server](https://github.com/jupyterhub/jupyterhub/wiki/Installation-of-Jupyterhub-on-remote-server)

## Warnings
None. Installation is fairly easy

## Installation of Jupyterhub on remote server

** I have spun up an micro AWS EC2 Instance with the root user of ubuntu **


1. Linux Anaconda Installation
(Anaconda conveniently installs Python, the Jupyter Notebook, and other commonly used packages for scientific computing and data science. )

    * Go to : [Continuum Analytics - Anaconda Downloads](https://www.continuum.io/downloads)

    * Under Linux Anaconda Installation (copy link of 64 bit):
    On Terminal

        `$ wget https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda2-4.0.0-Linux-x86_64.sh`

        It will download Anaconda*.sh file

    * Installing by using following command:

        `$ bash Anaconda2-4.0.0-Linux-x86_64.sh`

        Enter(many times) >> yes >> give directory or keep it as Default

** Note: You may also have to type source ~/.bashrc to load your default bash profile
 
2. Installing Python3 (dependency of jupyterhub is on python3)

    `$ sudo apt-get install python3-pip`

3. Install nodejs/npm

    `$ sudo apt-get install npm nodejs-legacy`

4. Install proxy with npm

    `$ sudo npm install -g configurable-http-proxy`

5. Install Jupyterhub

    `$ sudo pip3 install jupyterhub`
 
6. Install Jupyter notebook (/upgrade)

    `$ sudo pip3 install --upgrade notebook`

7. Test Jupyterhub default configuration

    `$ jupyterhub --no-ssl`

    This will start session in localhost:8000
    

    * Go to [http://your_ip_address:8000](http://www.example.com)

    ** Make sure that port isn't protected under Firewall of your system. Since I am installing this on an EC2 instance, the IP address will be the public IP address of the instance **

8. It is recommended to use secure SSL certificate file for the public facing
   interface of the proxy.
    To produce personal security certificates commands are as follows:

    `$ openssl req ­-x509 ­-nodes ­-days 365 ­-newkey rsa:1024 ­-keyout mykey.key ­-out mycert.pem`
    
    **Fill in the credentials.(even if you dont..It's ok!)


9. Create Jupyterhub configuration file

    `$ jupyterhub --generate-config`

10. We will use Github OAuthentication as our Authenticator.
 so steps are as follows:

  1. On the top left hand corner of Github.com, Go to your Github profile (click on profile icon) > Settings > Oauth application (under Developer Settings)

  * it is more convenient to not use capital letters in GitHub username

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



{% include links.html %}
