# Case Study: Documenting GDP per Capita with the World Bank API

## 1. Introduction

This documentation shows how to retrieve Latvia’s GDP per capita using the World Bank API.

The World Bank assigns a unique indicator code to each dataset. For GDP per capita (current US dollars), the code is `NY.GDP.PCAP.CD`.

This code must be included in the request URL to retrieve the data.

The data is returned as a time series covering multiple years.

The API supports both XML (default) and JSON. No authentication is required.

In this documentation, I focus on structure and readability.
## 2. Endpoint and Response Format

To retrieve GDP per capita data for Latvia, use the following endpoint:

```
GET https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD
```

By default, the response is returned in XML. To get the data in JSON, add the `format=json` parameter: 

```
GET https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD?format=json
```

The request uses the HTTP method `GET`, which is used to read data from the server.

No authentication is required.

## 3. Optional Parameters

The following optional parameters can be used to refine the request:

| Parameter | Description | Type | Default | Notes |
| --- | --- | --- | --- | --- |
| `date` | Limits the data to a specific time range. | string | full dataset | Format: `YYYY:YYYY` (e.g. `2000:2020`). |
| `format` | Defines the response format. | string | XML | Use `json` for JSON output. Affects only presentation, not data. |
| `per_page` | Number of results per page. | number | 50 | Set to 500 to return the full time series in one response. Otherwise, multiple pages may be needed. |

**Example request with all parameters combined:**

```
GET https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD?date=2000:2020&format=json&per_page=500
```


