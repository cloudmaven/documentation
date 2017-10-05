---
title: Creating intelligent water systems to unlock the potential of Smart Cities 
keywords: Azure, smart_cities, water, crisis
last_updated: October 5, 2017
tags: [Azure,data_visualization,analytics, platform, IoT, systems,networks]
summary: "Water shortages in Bangalore are being solved by Azure. Using services from Microsoft's Azure, the project harnesses the power of the cloud to collect and process data from the network of IoT sensors."
sidebar: mydoc_sidebar
permalink: azcs_smart_cities.html
folder: azcs
---

## Creating intelligent water systems to unlock the potential of Smart Cities 
July 31, 2017 | Posted by Microsoft Research Blog 
*By Satish Sangameswaran, Principal Program Manager, and Vani Mandava, Director, Data Science*

The newspaper headlines about Bangalore's looming water crisis have been ominous, with one urban planning expert proclaiming that Bangalore will become unlivable in a few years because of water scarcity. This is a critical issue that threatens the future of one of India's fastest-growing cities. In fact, water availability is a cause for worry in the entire country. According to an estimate by The Asian Development Bank, India will have a water deficit of 50% by the year 2030.

The primary source of water for Bangalore is the Cauvery river, which is located some 100 kilometers (about 62 miles) from the city. Because the monsoon does not always bring dependable rain, planners must maximize the efficiency of distribution of water from the source, and avoid depletion of the ground water table level. A key challenge in the area of water management in Bangalore is tracking consumption. Currently, a staggering one-third of the water pumped is unaccounted for, in terms of usage. This is the problem that a team of scientists at the Indian Institute of Science IISc is looking to solve. IISc is India's oldest and among the most revered academic institutions, with a sprawling green campus in the heart of Bangalore. Under the aegis of a national initiative called Smart Cities, Professor Yogesh Simmhan and his fellow researchers have deployed an Internet of Things IoT-based network of sensors in the IISc campus to efficiently monitor the flow of water from source to consumption.

Using services from Microsoft's Azure, the project harnesses the power of the cloud to collect and process data from the network of IoT sensors. An important facet of this effort is monitoring each node of this network to generate alerts and glean insights from the data. Azure Event Hubs enable such functions as receiving water quality incident alerts from specific locations via a smartphone app. Leveraging the advanced analytics capabilities available on Azure, the team can make decisions to ensure that available water is efficiently pumped to every building on campus. We are looking at the Internet of Things as a technology platform for enabling [smart cities](http://smartcities.gov.in/content/) we use Microsoft Azure Cloud for collecting data, hosting it and processing it in the cloud, says Simmhan, principal investigator for the project and assistant professor in the computational and data sciences at IISc.

[View YouTube Video](https://youtu.be/HkY39WThRxk)

The system consists of three components physical sensors, networking components and cloud. The sensing is done through microcontrollers that communicate wirelessly to a gateway that then sends the data to the cloud. The analytics are enabled through an Apache Storm-based service on Azure. All the edge devices are visible in the Azure resource directory, helping monitor hardware malfunctions or failure.† Rashmi B., a project assistant on the team, is responsible for the execution and deployment of the network. She aspires to ultimately bring this product to the end user, who should be able to log in from anywhere and monitor the health of the water resource network and intervene to prevent water leakage and avert crises.

The government of India envisions designating 100 cities in the country as Smart Cities. The idea is to deliver citizen services in these cities comparable to the best global standards. Providing citizens with clean and safe water in the most efficient manner that meets the needs of the population will be an important part of this mission. The water management project at the IISc campus can serve as a model showcase of water services provisioning, which can be scaled out to these 100 cities, across the whole country. It offers a beacon of hope towards the goal of managing and conserving precious water resources and makes a lasting contribution in improving the lives of a billion people.

### Related
- [Internet of Things IoT For Smart Cities](https://www.microsoft.com/en-us/internet-of-things/smart-city)
- [Summer Institute unpacks the future of IoT](https://www.microsoft.com/en-us/research/blog/summer-institute-unpacks-future-iot/)
- [Smart cities harness the power of the Microsoft cloud](https://enterprise.microsoft.com/en-us/articles/industries/citynext/smart-cities-harness-power-microsoft-cloud/)
- [Explanimators: Internet of Things](https://news.microsoft.com/stories/explanimators/internet-of-things/)

{% include links.html %}
