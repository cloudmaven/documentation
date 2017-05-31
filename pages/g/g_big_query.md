---
title: Google BigQuery
keywords: google, bigquery
last_updated: May 31, 2017
tags: [research_computing, Google, GCP]
summary: "Google BigQuery"
sidebar: mydoc_sidebar
permalink: g_big_query.html
folder: g
---

# Google BigQuery

Google BigQuery is a data warehouse for running analytic SQL queries. It
automatically scales to query datasets of up to petabytes in size.

## Links

- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs/)

## Overview

Use the [BigQuery web UI](https://cloud.google.com/bigquery/quickstart-web-ui),
[`bq` command-line
tool](https://cloud.google.com/bigquery/quickstart-command-line), or
[APIs](https://cloud.google.com/bigquery/docs/reference/libraries) to make SQL
queries.

## How it works

BigQuery is the cloud offering for the Dremel service ([see
paper](https://research.google.com/pubs/pub36632.html)). Data is stored by
column in a compressed format called
[Capacitor](https://cloud.google.com/blog/big-data/2016/04/inside-capacitor-bigquerys-next-generation-columnar-storage-format).

To run a SQL query, the query engine scans all rows in the table. The query
uses many parallel workers to scan the compressed data directly. The query
scans only the columns and
[partitions](https://cloud.google.com/bigquery/docs/partitioned-tables) it
needs.

## Pricing

BigQuery [pricing](https://cloud.google.com/bigquery/pricing) is somewhat
unique.

### Queries

You are charged per query based on the amount of data the query needed to
access. The
[project](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects)
running the query is charged, not the project that stores the data (unless of
course these are the same). See the [query pricing
table](https://cloud.google.com/bigquery/pricing#queries) for details.

You can query [1 TB of data for
free](https://cloud.google.com/bigquery/pricing#free-tier) per month. You can
[try BigQuery without a credit
card](https://cloud.google.com/blog/big-data/2017/01/how-to-run-a-terabyte-of-google-bigquery-queries-each-month-without-a-credit-card).
You don't need to start a free trial to use it.

### Storage

Data is charged per GB per month, but prorated per MB, per second. See the
[storage pricing table](https://cloud.google.com/bigquery/pricing#storage).
Data which is not modified for 90 days is charged a lower [long-term storage
rate](https://cloud.google.com/bigquery/pricing#long-term-storage)

You can use up to [10 GB of storage for
free](https://cloud.google.com/bigquery/pricing#free-tier-storage) per month.

## Public Data

Google hosts many [public
datasets](https://cloud.google.com/bigquery/public-data/) on BigQuery. You can
query these tables directly or join them to your own data.

[Contact the public data team at
Google](https://cloud.google.com/bigquery/public-data/#how-to-list-your-public-data-set-on-bigquery)
if you think your dataset would be a good fit for the program: bq-public-data AT google.com.

### Hosting your own public dataset

Since queries are charged to the project running the queries not the one
storing the data, you can make a popular dataset but only get charged for
storage and the queries you run yourself.

See [this tweet](https://twitter.com/felipehoffa/status/761635507080081408) for
how to make a dataset public:

1. Go to the dataset on the [BigQuery web
   UI](https://bigquery.cloud.google.com/).
1. Click the down arrow next to the dataset name.
1. Select **Share dataset**.
1. Select **All authenticated users** (meaning anyone with a Google account and cloud project).
1. Ensure the **View** permissions are set.
1. Click the **Add** button.
1. Click the **Save changes** button.

## External data sources

You can use BigQuery to run SQL queries against data stored outside of BigQuery
datasets by using the [external data
sources](https://cloud.google.com/bigquery/external-data-sources). For example:

1. Query files in [Cloud
   Storage](https://cloud.google.com/bigquery/external-data-cloud-storage) of
   several different data formats.
1. Query a [Bigtable
   database](https://cloud.google.com/bigquery/external-data-bigtable). This
   supports key range SQL queries so that a full table scan is not always
   needed.
1. Query files stored in [Google
   Drive](https://cloud.google.com/bigquery/external-data-drive).

{% include links.html %}
