# Case Study: Documenting GDP per Capita with the World Bank API

## 1. Introduction

This documentation shows how to retrieve Latvia’s GDP per capita using the World Bank API.

The World Bank assigns a unique indicator code to each dataset. For GDP per capita (current US dollars), the code is `NY.GDP.PCAP.CD`.

This code must be included in the request URL to retrieve the data.

The data is returned as a time series covering multiple years.

The API supports both XML (default) and JSON. No authentication is required.

In this documentation, I focus on structure and readability.
