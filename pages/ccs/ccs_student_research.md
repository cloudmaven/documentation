---
title: Student Research
keywords: NASA
last_updated: January 30, 2017
tags: [research_computing]
summary: "Student-led research computing on the public cloud"
sidebar: mydoc_sidebar
permalink: ccs_student_research.html
folder: ccs
---

## Introduction 


The purpose of this page is to describe student research on the public cloud as implemented at the University of Washington.
The project was initiated from the High Performance Computing Club with initial support from the Student Technology Fee Committee
and with a generous research credit grant from Amazon Web Services.


## Links


- [Configuring the account to allow IAM Users to track billing](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_billing.html?icmpid=docs_iam_console#tutorial-billing-step2)


## Status

- $10k in credits spends down *before* the $10k initial grant
- Status on grant at end of initial period June 30 2017?
- Spend to date is light (under $1k as of July 1)
- Leadership transfer in progress
- 1-2 part-time supporting roles
  - Address governance and account management 
  - Largely self-driven in terms of deliverables
  - Can extend to cloud-based data science work provided documentation 
- Second grant disbursal is the big open question at this point.
  - Further research credit grant process would follow upon resolving this


## For Administrators

- Someone has requested an increase in p2.xlarge quota which was granted
  - "We've approved and processed your EC2 Instances p2.xlarge limit increase request for the US East region; your new limit is 10."
- NetID authentication is presenting IAM challenges and we have resorted to granting IAM User admin access
  - This should be reviewed with the AWS SA soonest opportunity


### Adding a new user


UW-specific instructions...


- Go to https://groups.uw.edu/
- At the top click on My Groups
- Click on hpccloud_student_group
- Click on Membership
- In the appropriate box add the new NetID (no at extension)
- Click Do It
- Invite them to log in at [this link](https://idp.u.washington.edu/idp/profile/SAML2/Unsolicited/SSO?providerId=urn:amazon:webservices)


## Account management guidelines


- Tag all of your resources with these tags:
  - (key, value) = (Project, your UW NetID) 
    - **Do not include the email extension '@uw.edu'.**
    - **Do not include anything else in the Value part of the tag.**
  - (key, value) = (End_date, your expected finished-by date) 
  - (key, value) = (Name, netid_short_description) 
    - Suppose my email address is kilroy@etc.edu. I might give my EC2 instance the name *kilroy_heavycompute_A*.
- Once per month (or more!) email the student administrator a two sentence summary of your status. More frequent is fine.
  - Include your projected cost estimate so we can see how good we are at that!
- Contact the student administrator and/or the cloud computing staff with any questions.
- Stop your instances and other services when you are not using them. 
- Write up a synopsis of your research, results and blockers as you go. 
  - This is your primary deliverable for participating and we will use these to further promote the program.
- Have fun, do incredible work.


## IAM User additions

- Until we figure out Roles etc the NetID authentication can fall short necessitating an additional login
- This IAM User can be an admin... with attendant risk
- We like to hand over creds using a thumb drive
- Kilroy when this is not possible we need to write up PGP encryption for transferring creds via email securely 


## Tracking spending


IAM Users are given admin access as well as IAM access via Role/Policy actions on the console. There are two more
steps needed. 

First [enable access to billing data](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_billing.html#tutorial-billing-step1).


Second: Create and assign a Policy to IAM admin Users granting them billing access. 
[Here](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_billing.html?icmpid=docs_iam_console#tutorial-billing-step2)
is the link for how to do this; it is a little involved. 


kilroy here is the segment on how to use the cost tool


{% include links.html %}

## Getting Started with AWS Cloud

If you are a student like me who would like to use the cloud for research purposes, then you are at the right place. The following steps will walk you through how to get a cloud account and and how to use the cloud.

1. Create an AWS account through us. This is as simple as emailing .... to get an AWS account set up.

Once we have set up an account for you, you will receive an Account number, User Name, and Password. This is a private account, so please do not share this information with anyone.

2. Choose the solution that you would like to build.

3. Click on Launch a virtual machine in Build a Solution.

  1. In the AWS console https://console.aws.amazon.com, click on Launch a virtual machine. For information about EC2 instance pricing, visit https://aws.amazon.com/ec2/pricing/on-demand/ where you can find out about the cost to run EC2 Instance on different operating systems.
  
  2. Click on Get Started. Type in a name for your EC2 Instance. Example: MyFirstInstance

  3. Select an Operating System. Example: Amazon Linux AMI

  4. Select an Instance Type. Example: t2.micro (You can check for the price of this Instance Type by going to https://aws.amazon.com/ec2/pricing/on-demand/)

  5. Create a Key Pair and download and save it in a safe place on your computer.

  Congratualtions! You have successfully launched your own EC2 Instance.

#### Where do I find the EC2 Dashboard?

Click on the Services tab in the AWS console. Under Compute, click on EC2. OR Type EC2 in the search bar.

#### Connecting to your Linux Instance Using SSH from Terminal or Command Prompt

1. Go to the Folder where you saved your key pair file in Terminal. 

2. Type ssh ec2-user@12.123.56.110 -i KeypairName.pem 

If this WARNING: UNPROTECTED PRIVATE KEY FILE! appears, type ls -al Fir* in the terminal to check the permissions. This will be in a format like this: -r--rw-r--
Then, type chmod 400 FirstInstance.pem in the terminal to change the permissions to -r--------
Hit enter and then press the up arrow key to return to ssh ec2-user@12.123.56.110 -i KeypairName.pem

3. When you have successfully accessed your Linux Instance, you will see an EC2 symbol in your Terminal/Command Prompt screen.
If you are asked to run sudo yum update, type this in to apply all updates. Complete! will show when the updating is done.
For a more detailed instruction, visit http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html




Congratualtions! You have successfully connected to your linux instance.

#### Autotagging EC2 instances

For instructions on "How to Automatically Tag Amazon EC2 Resources in Response to API Events", please visit https://aws.amazon.com/blogs/security/how-to-automatically-tag-amazon-ec2-resources-in-response-to-api-events/


#### AWS CloudWatch

For instructions on how to "Create Alarms to Stop, Terminate, Reboot, or Recover an Instance", please visit http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingAlarmActions.html

## Anaconda 
Before you download Anaconda, check which version of Python your computer is running on. You can do this by typing 'python -v' into the command line.

To download and install Anaconda, follow the instructions on the following website.
https://www.continuum.io/downloads Note: If you choose to download the command-line installer, please make sure that you go to the folder where you downloaded your command-line installer in your command line. This can be typing cd FolderName (usually the folder is Downloads). Then, in your command line window, type one of the bash commands as shown in the instructions on website.

##### Packages included in Anaconda 4+ (The following information is obtained from Acaconda's Cheat Sheet):

1. NumPy | https://numpy.org N-dimensional array for numerical computation
2. SciPy | https://scipy.org Collection of numerical algorithms and toolboxes, including signal processing and optimization
3. MatPlotLib | https://matplotlib.org Plotting library for Python
4. Pandas | https://pandas.pydata.org Powerful Python data analysis toolkit
5. Seaborn | https://stanford.edu/~mwaskom/software/seaborn/ Statistical data visualization
6. Bokeh | https://bokeh.pydata.org Interactive web visualization library
7. SciKit-Learn | https://scikit-learn.org/stable Python modules for machine learning and data mining
8. NLTK | https://nltk.org Natural language toolkit
9. Notebook | https://jupyter.org Web-based interactive computational environment combines code execution, rich text, mathematics, plots and rich media
10. R essentials | https://conda.pydata.org/docs/r-with-conda.html R with 80+ of the most used R packages for data science
"conda install -c r r-essentials"

## Jupyter Noteboook

Once you have installed Anaconda on your computer, type 'jupyter notebook' (without the quotes) into your command line to run the notebook.
