---
title: Azure Best Practices 
keywords: azure, best, practices
last_updated: October 26, 2017
tags: [Azure, best_practices, API, Autoscaling, background_jobs, caching, monitoring, naming]
summary: "Microsoft Azure Best Practice Documention." 
sidebar: mydoc_sidebar
permalink: az_best_practices.html
folder: az
---

# Introduction
This section is an annotation of Microsoft Best Practices for your successful use of Azure to aid your research.  At the bottom of this page is a form for suggestions and to request assistance.

## Azure API Design
Many modern web-based solutions make the use of web services, hosted by web servers, to provide functionality for remote client applications. The operations that a web service exposes constitute a web API. A well-designed web API should aim to support:

**Platform independence** Client applications should be able to utilize the API that the web service provides without requiring how the data or operations that API exposes are physically implemented. This requires that the API abides by common standards that enable a client application and web service to agree on which data formats to use, and the structure of the data that is exchanged between client applications and the web service.

**Service evolution** The web service should be able to evolve and add (or remove) functionality independently from client applications. Existing client applications should be able to continue to operate unmodified as the features provided by the web service change. All functionality should also be discoverable, so that client applications can fully utilize it.

The purpose of this guidance is to describe the issues that you should consider when designing a web API. [Read more...](https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design)

## API Implementation
A carefully-designed RESTful web API defines the resources, relationships, and navigation schemes that are accessible to client applications. When you implement and deploy a web API, you should consider the physical requirements of the environment hosting the web API and the way in which the web API is constructed rather than the logical structure of the data. This guidance focusses on best practices for implementing a web API and publishing it to make it available to client applications.
[Read more...](https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-implementation)

## Autoscaling
Autoscaling is the process of dynamically allocating resources to match performance requirements. As the volume of work grows, an application may need additional resources to maintain the desired performance levels and satisfy service-level agreements (SLAs). As demand slackens and the additional resources are no longer needed, they can be de-allocated to minimize costs.

Autoscaling takes advantage of the elasticity of cloud-hosted environments while easing management overhead. It reduces the need for an operator to continually monitor the performance of a system and make decisions about adding or removing resources.

There are two main ways that an application can scale: 

**Vertical scaling**, also called scaling up and down, means changing the capacity of a resource. For example, you could move an application to a larger VM size. Vertical scaling often requires making the system temporarily unavailable while it is being redeployed. Therefore, it's less common to automate vertical scaling.

**Horizontal scaling**, also called scaling out and in, means adding or removing instances of a resource. The application continues running without interruption as new resources are provisioned. When the provisioning process is complete, the solution is deployed on these additional resources. If demand drops, the additional resources can be shut down cleanly and deallocated. 

Many cloud-based systems, including Microsoft Azure, support automatic horizontal scaling. The rest of this article focuses on horizontal scaling. [Read more...](https://docs.microsoft.com/en-us/azure/architecture/best-practices/auto-scaling)

## Background Jobs
Many types of applications require background tasks that run independently of the user interface (UI). Examples include batch jobs, intensive processing tasks, and long-running processes such as workflows. Background jobs can be executed without requiring user interaction--the application can start the job and then continue to process interactive requests from users. This can help to minimize the load on the application UI, which can improve availability and reduce interactive response times.

For example, if an application is required to generate thumbnails of images that are uploaded by users, it can do this as a background job and save the thumbnail to storage when it is complete--without the user needing to wait for the process to be completed. In the same way, a user placing an order can initiate a background workflow that processes the order, while the UI allows the user to continue browsing the web app. When the background job is complete, it can update the stored orders data and send an email to the user that confirms the order.

When you consider whether to implement a task as a background job, the main criteria is whether the task can run without user interaction and without the UI needing to wait for the job to be completed. Tasks that require the user or the UI to wait while they are completed might not be appropriate as background jobs.
[Read more...](https://docs.microsoft.com/en-us/azure/architecture/best-practices/background-jobs)

## Caching
Caching is a common technique that aims to improve the performance and scalability of a system. It does this by temporarily copying frequently accessed data to fast storage that's located close to the application. If this fast data storage is located closer to the application than the original source, then caching can significantly improve response times for client applications by serving data more quickly.

Caching is most effective when a client instance repeatedly reads the same data, especially if all the following conditions apply to the original data store:
- It remains relatively static.
- It's slow compared to the speed of the cache.
- It's subject to a high level of contention.
- It's far away when network latency can cause access to be slow

[Read more...](https://docs.microsoft.com/en-us/azure/architecture/best-practices/caching)

## Content Delivery Network
The Microsoft Azure Content Delivery Network (CDN) offers developers a global solution for delivering high-bandwidth content that is hosted in Azure or any other location. Using the CDN, you can cache publicly available objects loaded from Azure blob storage, a web application, virtual machine, application folder, or other HTTP/HTTPS location. The CDN cache can be held at strategic locations to provide maximum bandwidth for delivering content to users. The CDN is typically used for delivering static content such as images, style sheets, documents, files, client-side scripts, and HTML pages.

You can also use the CDN as a cache for serving dynamic content, such as a PDF report or graph based on specified inputs; if the same input values are provided by different users the result should be the same.

The major advantages of using the CDN are lower latency and faster delivery of content to users irrespective of their geographical location in relation to the datacenter where the application is hosted.  [Read more...](https://docs.microsoft.com/en-us/azure/architecture/best-practices/cdn)

## Data Partitioning
In many large-scale solutions, data is divided into separate partitions that can be managed and accessed separately. The partitioning strategy must be chosen carefully to maximize the benefits while minimizing adverse effects. Partitioning can help improve scalability, reduce contention, and optimize performance. Another benefit of partitioning is that it can provide a mechanism for dividing data by the pattern of use. For example, you can archive older, less active (cold) data in cheaper data storage.
[Read more...](https://docs.microsoft.com/en-us/azure/architecture/best-practices/data-partitioning)

## Monitoring and Diagnostics
Distributed applications and services running in the cloud are, by their nature, complex pieces of software that comprise many moving parts. In a production environment, it's important to be able to track the way in which users utilize your system, trace resource utilization, and generally monitor the health and performance of your system. You can use this information as a diagnostic aid to detect and correct issues, and also to help spot potential problems and prevent them from occurring.
[Read more...](https://docs.microsoft.com/en-us/azure/architecture/best-practices/monitoring)

## Naming Conventions
This article is a summary of the naming rules and restrictions for Azure resources and a baseline set of recommendations for naming conventions. You can use these recommendations as a starting point for your own conventions specific to your needs.

The choice of a name for any resource in Microsoft Azure is important because:

- It is difficult to change a name later.
- Names must meet the requirements of their specific resource type.

Consistent naming conventions make resources easier to locate. They can also indicate the role of a resource in a solution.

The key to success with naming conventions is establishing and following them across your applications and organizations. [Read more...](https://docs.microsoft.com/en-us/azure/architecture/best-practices/naming-conventions)

## Retry guidance for specific services
Most Azure services and client SDKs include a retry mechanism. However, these differ because each service has different characteristics and requirements, and so each retry mechanism is tuned to a specific service. This guide summarizes the retry mechanism features for the majority of Azure services, and includes information to help you use, adapt, or extend the retry mechanism for that service.
[Read more...](https://docs.microsoft.com/en-us/azure/architecture/best-practices/retry-service-specific)

## Transient fault handling
All applications that communicate with remote services and resources must be sensitive to transient faults. This is especially the case for applications that run in the cloud, where the nature of the environment and connectivity over the Internet means these types of faults are likely to be encountered more often. Transient faults include the momentary loss of network connectivity to components and services, the temporary unavailability of a service, or timeouts that arise when a service is busy. These faults are often self-correcting, and if the action is repeated after a suitable delay it is likely succeed.

This document covers general guidance for transient fault handling. [Read more...](https://docs.microsoft.com/en-us/azure/architecture/best-practices/transient-faults)

## Request Form
Please use this [form](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbRxLOqWUi_fJItLLsEfSA7I9UQzk5TVNQMThJRUJQMk00Wk1BWE9CMENCMC4u) to provide feedback, request more documentation, request someone to contact you for help, etc.


{% include links.html %}
