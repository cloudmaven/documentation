---
title: Organic chemistry case study on Azure
keywords: GDS
last_updated: October 6, 2016
tags: [research_computing]
summary: "Geo Data System "
sidebar: mydoc_sidebar
permalink: azcs_organic_chemistry.html
folder: azcs
---

## Introduction

The purpose of this page is to describe a data system for organic chemistry research, specifically 
for physical and spectral analysis of dissolved organic matter (DOM) obtained from samples of the 
earth's hydrosphere.  

## Links

## Warnings

## Overview

In 2010 one of us (RF) began working with a group of geochemists (AS, RS, TD, JN, RS, HM) to build a system
on the Microsoft technology stack that would advance the state of the art of research in the earth's global carbon 
cycle.  Specifically the scientists recognized that there were two important functions that a centralized, 
standardized data system could potentially provide: Perfunctory data processing and a large collective pool 
of queryable samples.  

To provide a sense of the research we present a brief scientific digression. 

The earth's hydrosphere is *all of the water on earth in its many locations* from the bottom of the Antarctic ice 
sheet to water vapor suspended in the upper reaches of the atmosphere to the oceans to the permafrost of Siberia 
to the mud on the banks of the Great Grey Greasy Limpopo River (all set about with fever trees) to the glaciers of 
the Himalayas to the damp soil of the Hoh rainforest... and on and on. All of this water bears the fingerprints of 
its history in the form of dissolved carbon-bearing molecules. These molecules generally reflect metabolic processes 
of life on earth at all scales from microbial to macroscopic as well as physical effects such as degredation due 
to the sun's ultraviolet rays. The common denominator in this picture is the storage and transport of carbon in 
what is called the global carbon cycle.  Carbon is stored in the earth system in reservoirs that include soil, 
oceans, sediment, rock, atmosphere, surface water and ice. It is transported and transformed between reservoirs by 
physical, chemical and biological processes at various rates. The aggregate of medium-to-small carbon molecules 
with life-based or organic structure are referred to as DOM for Dissolved Organic Carbon. 

The current state-of-the-art in analysis of DOM found in water samples involves spectral methods, three in particular
in the work described here. By 'spectral analysis method' we mean a procedure that generates from one water sample a
series of values associated with one or more spectral parameters such as wavelength. As an example if one were 
studying rain rather than DOM one might measure the intensity of a rainbow across all of its colors; by wavelength.

Let's consider spectral DOM data generated in the course of a single research project.  If a particular field campaign 
produced one thousand water samples and each of these sampels yielded 400,000 data values across three spectral methods 
then the project will have produced 400 million data values that must be stored and analyzed. Typical reduction methods 
applied to these data might be applied iteratively many times over the course of two or three years resulting in 
three or four research papers; where the conclusions therein would emerge from patterns and structures discovered in 
that data.

The problem is this: The scientists are extremely adept at imagining forms of data analysis that have not yet been 
implemented. They are able to see how other scientists in related field could make use of this data. They would
like those scientists to have direct, unfettered access to the spectral DOM data without any human intervention
being necessary.  And finally our scientists are able to envision the power of combining datasets from multiple 
sampling projects to create a deeper body of data to analyze. But none of these imagined pathways can be implemented 
because the data are simply too complex and unwieldy in their traditional form to support these advances in DOM-driven
research. 

The task therefore falls to technologists (including these same scientists) to build a data management system that 
makes all of these imagined advances a reality. This, simply put, is the objective of our DOM data system project. 

## User Interface

Download PDF [here](/documentation/pdf/Doc07_BDSUserInterfaceBasics.pdf) 

## API

## Query

Download PDF [here](/documentation/pdf/Doc08_BDSQueryBasics.pdf)

## Data Egress

Download PDF [here](/documentation/pdf/Doc12_BDSDataEgress.pdf)

## Metadata

Download PDF [here](/documentation/pdf/Doc09_BDSMetadataBasics.pdf)

## MATLAB Functions

Download PDF [here](/documentation/pdf/Doc10_BDSMATLABFunctionsInMETemplates.pdf)

## EEMs

Download PDF [here](/documentation/pdf/Doc11_BDSEEMPARAFAC.pdf)

{% include links.html %}
