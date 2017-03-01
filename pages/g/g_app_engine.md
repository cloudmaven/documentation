---
title: Google App Engine
keywords: google, app, engine
last_updated: March 1, 2017
tags: [research_computing, Google, GCP]
summary: "Google App Engine"
sidebar: mydoc_sidebar
permalink: g_app_engine.html
folder: g
---

# Google App Engine

Google App Engine is a platform as a service offering. It dynamically scales
the number of computing resources based on the request load.

## Links

- [Google App Engine Documentation](https://cloud.google.com/appengine/docs/)
- [App Engine Standard Environment](https://cloud.google.com/appengine/docs/standard/)
- [App Engine Flexible Environment](https://cloud.google.com/appengine/docs/flexible/)

## Overview

App Engine has two different "environments".

### Standard Environment

The App Engine standard environment has been in production since 2008. It builds
on Google's infrastructure for serving web applications and is well suited for
HTTP applications which can respond to requests quickly (maximum of 60 seconds).

### Flexible Environment

The App Engine flexible environment manages Google Compute Engine resources for
you. Since it is built on [Compute Engine](./g_compute_engine.html), it is able
to handle more flexible workloads than the standard environment can.

{% include links.html %}
