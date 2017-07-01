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
