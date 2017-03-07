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
- ***You can use cloud-provider support for Apache Spark: e.g. Elastic Map Reduce on AWS. However AmpLab 
(the originators of Spark) also provide more direct solutions that can save you some money but require a 
bit of additional effort to configure.***



## ***PREDICTD*** 
- Parallel Epigenomics Data Imputation with Cloud-based Tensor Decomposition. 
- Epigenome = all of the machinery associated with the genome: Protein manufacture, gene regulation, etc
- Stochastic Gradient Descent Optimization 


- A prior study used for comparatives is called CHROMIMPUTE. 
  - The paper for this was published by Ernst and Kellis in 2015 in Nature Biotechnology.


- The researcher for this study is Tim Durham, a graduate student in Bill Noble's genomics lab at the University of Washington.
  - The results improve over the CHROMIMPUTE study for global mean squared error.
  - CHROMIMPUTE does better by comparison on the other metrics; but the methods are still close. 
  - The computation is a form of machine learning (modeling) and is built on the Apache Spark engine
  - The data volume is a three-dimensional tensor with axes: Human cell types, human proteins, and the human genome
    - The cell type axis is 120 or so cell types
    - The protein axis is similarly 150 or so proteins
    - The genome axis is three billion nucleotides
  - The model is trained and one important result is that two of the model components can be locally optimized using only 1% of the genome
  - The entire genome would take some time... 24-48 hours depending on the cluster size
  - Today 1% of the genome requires five hours on 64 cores: That is an X1.16xlarge 
    - More memory than needed; but still cheap per core
    - optimized data structures to use compressed-format matrices
    - cell type and assay matrix training used 1% of 1% of the data; so that all fit on one machine
    - 500GB required; 1.4TB available

## Next steps

- Write the paper
- publish the software and tutorial on GitHub and cloudmaven will point to this
  - Add some interpretability to the code
  - HDInsight or EMR on AWS: Is fine.
  - Tim ran Spark EC2 which bootstraps an EC2 cluster... but you need to be root
    - Spark EC2 is from AmpLab on GitHub.com/amplab/spark-ec2
    - AWS makes it hard for you to log in as root...
  - EMR now permits some spot market access (although the X1.16xlarge may or may not be part of that)
- Entire genome
  - Publish the results "whole genome imputed tracks through the Encyclopedia of DNA Elements 'ENCODE'
    - Hopefully by start of summer
    - There are three obstacles in the way of imputing the whole genome right now. 
      - The first (and much bigger) issue is that this will take more time and money than I currently have
      - It's proving harder than I thought it would to get Spark to swallow the full data set, so I will have to do 
some additional software engineering to process the full genome in batches. 
      - The third reason that we have de-prioritized training on the whole genome is that we've found that the model performs 
essentially as well on 0.01% of the data as it does on 1% of the data, so we don't expect to get much of a performance 
boost by training on everything. 

- Tim will turn next to some wet lab work: Studying tissue development in a nematode C.elegans

## Speed up for cloud implementation

- From weeks to order of hours 
  - ChromImpute led to training the model on 127 cell types and 24 assays for comparison purposes 
- This imputes hypothetical results in silico in place of wet lab experiments.


## Computation and cost details
- How much does one such physical wet lab experiment cost (i.e. one cell type, one protein assay, 3 billion base pairs)?

A typical run that I'm doing now takes about 8 hrs with 1 x m4.xlarge instance (4 cores, 16 GB memory) 
and 1 x x1.16xlarge instance (64 cores, 976 GB memory). The head node (m4.xlarge) is a normal EC2 
instance, while the worker (x1.16xlarge) is a spot instance, so the price isn't consistent, but it 
stays at around $1.22/hr. So a single training run costs ~$10; we tend to do a cross-validation 
scheme with 4-8 folds, so the total cost of processing a model runs about $80 and takes two to three 
days. Data storage is the other big component of the cost. With the subset of the experiments and 
genomic positions that I am working with the output of one of these cross-validation runs is about 
750 GB stored on S3. Loading the entire genome into memory for all training examples takes about 
1.5 TB, so training on the whole genome will produce at least 4.5 TB considering that the 1.5 TB 
does not include 2/3 of the data. My total S3 usage right now is significantly higher even than that 
because I have been keeping results from all the preliminary experiments I've done over the past 
year trying to tune the model, but I'll clean those up soon once the paper comes together. 


Anyway, storage costs for a single imputation run (as I'm currently running it) are on the order of 
$20/month, so I guess the total imputation cost is about $100. This compares pretty favorably to the 
cost of collecting the data in the lab -- a quick search for services that will perform these assays 
show prices as high as $1000/sample, but I'm not sure how much it would cost a lab equipped to do 
the assay in-house.

Model training at the 1% scale takes ten to 24 hours wall clock time.

You could make the run time pretty reasonable but the whole genome has proven problematic for other
reasons; see above.

### Tim details on cost

- $300 EMR with no spot instances
- $88 EMR with spot
- $1.25 for X1.16xlarge when Tim last checked but this instance may not work
- ... so we go to another (allowed) 2 x R3.8xlarge instance and that gives us the above costs
  - (EMR does not permit R4 as far as we know at the moment)
- 1% of the genome, requiring 48 hours
- 100% of genome scales linearly and this (with a bit of coding) should scale sideways
  - so the entire genome would require some testing: Spin up 100 3-node clusters? Bigger dataset? 
- Without EMR: $90 becomes $60
  - large instances are $.27 / hour / instance


## Full genome 

- Pending
- Train cell type and assay parameters (the smaller dimensions) on a small subset of genomic positions
  - Then apply those across the genome in batches
- ...to publish imputed results plus code plus tutorial for use by others
- Of 127 cell types x 24 assays there are 1014 (33%) experimental datasets 
- The full project with additional cell types and protein assays has only 2% of the possible data

{% include links.html %}
