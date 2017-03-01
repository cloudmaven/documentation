---
title: Preemptible Instances - Google Compute Engine
keywords: google, compute, engine, preemptible, instances, vm, vms
last_updated: March 1, 2017
tags: [research_computing, Google, GCP]
summary: "Preemptible Instances - Google Compute Engine"
sidebar: mydoc_sidebar
permalink: g_preemptible_instances.html
folder: g
---

# Preemptible Instances - Google Compute Engine

Use preemptible instances to control costs for workloads which are not sensitive
to individual machine failures, such as batch jobs.

## Links

- [Preemptible VM Instances](https://cloud.google.com/compute/docs/instances/preemptible)
- [GCP Pricing Calculator ](https://cloud.google.com/products/calculator/#id=053c962c-3c94-41b1-b717-df7b85eda239)
- [Compute Engine Pricing](https://cloud.google.com/compute/pricing#predefined_machine_types)

## Overview

A preemptible instance is a lower-cost [Google Compute
Engine](./g_compute_engine.html) virtual machine. For example (as of March 1,
2017), a single CPU machine costs $0.05/hour but a the same machine costs
$0.01/hour as a preemptible instance. This lower costs comes with some caveats:

- Preemptible Instances run for a maximum of 24 hours.
- Preemptible Instances may be "preempted" (shutdown) by Google at any time.
  You get about 30 seconds to run a shutdown script.
- Preemptible Instances may not be available if Compute Engine does not have
  excess capacity.

## Examples

- Google doubled the capacity of the global [CMS
  Experiment](http://cms.web.cern.ch/) computing resources for the week of the
  [SC16 Supercomputing Conference](http://sc16.supercomputing.org/) using
  preemptible VMs. See [blog
  post](https://cloudplatform.googleblog.com/2016/11/Google-Cloud-HEPCloud-and-probing-the-nature-of-Nature.html).

{% include links.html %}
