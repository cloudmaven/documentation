---
title: Parallel Epigenomics Data Imputation with Cloud-based Tensor Decomposition
keywords: research_computing, genomics, spark
last_updated: October 6, 2016
tags: [research_computing, genomics, spark, case_studies, AWS, Azure, organic_chemistry, data_science, scale]
summary: "Parallel Epigenomics Data Imputation with Cloud-based Tensor Decomposition (PREDICTD)"
sidebar: mydoc_sidebar
permalink: acs_epigenome_imputation.html
folder: acs
---

## Introduction
This page describes a methodology study in genomics to impute (computationally infer) information linking 
cell types, proteins and locations along the human genome. The study is currently in preparation as a 
research paper. The computation is done on the public cloud (both AWS and Azure platforms) using the 
Apache Spark computation framework.

## Links

- Link to the code

## Warnings
- ***You can use cloud-provider support such as EMR but AmpLab also provides more direct solutions that can save
you some money.***

## Overview

This project is called 'PREDICTD': Parallel Epigenomics Data Imputation with Cloud-based Tensor Decomposition. 

- Epigenome Imputation: Epigenome is all of the machinery associated with the genome: Protein manufacture, gene regulation, and so on.
- The method used here is called Stochastic Gradient Descent Optimization.
- A prior study used for comparatives is called CHROMIMPUTE. The paper for this was published by Ernst and Kellis in 2015 in Nature Biotechnology.
- The researcher for this study is Tim Durham, a graduate student in Bill Noble's genomics lab at the University of Washington.
  - The results improve over the CHROMIMPUTE study for global mean squared error.
  - CHROMIMPUTE does better by comparison on the other metrics; but the methods are still close. 
  - The computation is a form of machine learning (modeling) and is built on the Apache Spark engine
  - The data volume is a three-dimensional tensor with axes: Human cell types, human proteins, and the human genome
    - The cell type axis is 120 or so cell types
    - The protein axis is similarly 150 or so proteins
    - The genome axis is three billion nucleotides
  - The model is trained and one important result is that two of the model components can be locally optimized using only 1% of the genome
  - Therefore the entire genome would take some time... would take 24-48 hours depending on the cluster size
  - Today 1% of the genome requires five hours on 64 cores: That is an X1.16xlarge (more memory than needed; but still cheap per core)
    - optimized data structures to use compressed-format matrices
    - cell type and assay matrix training used 1% of 1% of the data; so that all fit on one machine
    - 500GB required; 1.4TB available
- First write the paper
- Second publish the software and tutorial on GitHub which we will reference
  - Add some interpretability to the code
  - HDInsight or EMR on AWS: Is fine.
  - Tim ran Spark EC2 which bootstraps an EC2 cluster... but you need to be root
    - Spark EC2 is from AmpLab on GitHub.com/amplab/spark-ec2
    - AWS makes it hard for you to log in as root...
  - EMR now permits some spot market access (although the X1.16xlarge may or may not be part of that)
- Third do the entire genome
  - Publish the results "whole genome imputed tracks through the Encyclopedia of DNA Elements 'ENCODE': Hopefully be start of summer
- Tim will turn next to some wet lab work: Studying tissue development in a nematode C.elegans
- The plan is to impute and publish the data tensor for the complete genome-axis. 
  - There are three obstacles in the way of imputing the whole genome right now. 
    - The first (and much bigger) issue is that this will take more time and money than I currently have
    - It's proving harder than I thought it would to get Spark to swallow the full data set, so I will have to do 
      some additional software engineering to process the full genome in batches. 
    - The third reason that we have de-prioritized training on the whole genome is that we've found that the model performs 
      essentially as well on 0.01% of the data as it does on 1% of the data, so we don't expect to get much of a performance 
      boost by training on everything. 
  - Priorities: get a paper out, write up the cloud (tutorial), final coding and show that the code works to impute some whole genome

## More material

- The original iterative testing took about two weeks to sorta converge whereas you sped that up to...
  - ...on the order of hours. It depends on model parameter settings and how much of the genome you are trying to impute. 

- That was operating on 0.06% of the genome and order 100 proteins and order 100 cell types.
  - ChromImpute led to training the model on 127 cell types and 24 assays for comparison purposes 


{% include links.html %}
