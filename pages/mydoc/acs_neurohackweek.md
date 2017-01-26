---
title: Research Computing Neurohackweek
keywords: research,computing,case,study,neuron,neurohack,hack,hackweek
last_updated: January 25, 2017
tags: [research,computing,case,study,neuron,neurohack,hack,hackweek]
summary: "Neurohackweek at the eScience Institute using AWS"
sidebar: mydoc_sidebar
permalink: acs_neurohackweek.html
folder: mydoc
---

# AWS at Neurohackweek 2016 

### University of Washington eScience Institute

### By Ariel Rokem and Rob Fatland

## Summary
Neurohackweek ran September 5--9 2016 at the UW eScience Institute with 40+ attendees; with a strong emphasis on team projects built into the agenda. 
Four of these team projects made use of cloud computing resources provided by UW IT to great effect as described below. UW IT Research Computing will 
continue to work with the event organizer Ariel Rokem and with this community to expand and solidify the contribution of cloud computing to this 
important research. This continuation will include provision of compute resources, hosting training sessions and supporting consultation with AWS solution 
architects. 

## Background
Neurohackweek is an annual 5-day workshop held at the University of Washington eScience Institute held this year on September 5th-9th (2016). 
The workshop convened more than 40 participants: graduate students, post-docs, faculty and research staff from all over the US and from the 
UK and the Netherlands, from Psychology, Neuroscience, Computer Science and other fields. The workshop was structured as part conference, 
part summer school, and part hackathon. During the week, participants took part in workshops and tutorials, presented their work in talks, 
and worked in small teams on projects or *hacks*, with results presented at the end of the week. 

Video recordings of some of the presentations, including presentations of the final projects are available in 
[this YouTube channel](https://www.youtube.com/playlist?list=PLEdFhTRBFLObkatJOX9wp3BCueH4wNSl7)

On the second day of the workshop Cameron Craddock (Child Mind Institute, NY) presented a morning tutorial on using AWS for cloud computing 
for neuroimaging applications. The materials used for this tutorial are available on the 
[Neurohackweek GitHub account](https://github.com/neurohackweek/NI_cloud_computing) .

For this tutorial we provided participants with AWS credentials. They were thereby able to explore several options of neuroimaging compute 
pipelines with AWS, primarily built on EC2 and S3 technologies. 

## Project outcomes
Four of the team projects conducted during the week used AWS: 

1. Developing a system for running BIDS apps -- docker containers of neuroimaging pipelines -- in the cloud. 
Preprocessed data from the ABIDE initiative was used. When fully developed, this will greatly simplify user 
access to high powered neuroimaging pipelines available through BIDS-Apps and cloud computing. 

2. An implementation of the NPAIRS framework: Using a pre-configured AMI from Cameron, this project added 
nodes, installed python modules to the nodes, and ran machine learning scripts on the nodes. They found that it 
was easy to use a pre-built AMI but a little bit tricky to install modules to nodes. AWS or other cloud computing 
would be good for running time-consuming and parallel jobs that do not need lots of intermediate human interaction.

3. Collaborative Jupyter on AWS EC2: providing easy access to and storage of the ABIDE data and serial processing of 
scripts overnight. The scripts for this project were then run in parallel on AWS, making it easy to then deploy them 
on local clusters at the University of Oregon and at MIT when participants returned home. Notably, this team had 
some difficulty with credentials when trying to create new nodes. Quickly debugging these kinds of issues 
in the context of a hackathon is a challenge for the organizers.

4. Preprocess the [CoRR dataset](https://s3.amazonaws.com/fcp-indi/data/Projects/CORR): An AMI with the newest 
version (v0.4.0) of the C-PAC pipeline software was created, and Starcluster was used to launch and manage 
20 EC2 instances with the goal of preprocessing all of CoRR's datasets. Since CoRR  is so large (1629 subjects; 
3357 anatomical scans 5093 resting state functional scans), the instances didn't finish running before the end 
of Neurohackweek, but the setup during the week will allow the team to continue the work.


{% include links.html %}
