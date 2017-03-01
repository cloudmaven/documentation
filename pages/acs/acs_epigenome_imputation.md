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


end part 1


middle bit

- This imputes hypothetical results in silico in place of wet lab experiments.

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

Fourth when you went up to running 1% of the genome it still took 1 hour.

This might be true for some version of the model and for some cluster configuration, but unfortunately I can't 
tell you exactly which one. Lately my models take longer to train than an hour; they are more on the order of 
10 hours, and some of my attempts for things I was trying this fall took more like 12-24 hours to train.

Fifth when you do the entire genome it will take... wait for it... 1 hour. (these are wall clock times)

I think you'd be hard-pressed to get the run time down to an hour, at least with my current implementation. 
The run time is highly dependent on model settings and the size of the cluster you're willing to allocate, 
so I'm sure you could make the run time pretty reasonable, but the whole genome has proven problematic (see above).


{% include links.html %}
