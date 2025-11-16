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

## 4. Sample Responses - XML and JSON

### 4.1. Sample Response XML (default format)

By default, the World Bank API returns XML.

Below is a shortened example of the response:

```xml
<data>
  <page>1</page>
  <pages>1</pages>
  <per_page>500</per_page>
  <total>32</total>
  <indicator id="NY.GDP.PCAP.CD">GDP per capita (current US$)</indicator>
  <country id="LV">Latvia</country>
  <record>
    <date>2020</date>
    <value>17384.412</value>
  </record>
  <record>
    <date>2019</date>
    <value>18051.391</value>
  </record>
</data>

```

This response contains:

- **Metadata** (page info, total entries)
- **Indicator and country information**
- A list of `<record>` elements, each with a year and a value

### 4.2. Sample Response JSON (with `format=json`)

To receive the response in JSON format, add the `format=json` parameter to the request. See above in “3. Optional Parameters”.

```json
[
  {
    "page": 1,
    "pages": 1,
    "per_page": "500",
    "total": 32
  },
  [
    {
      "indicator": {
        "id": "NY.GDP.PCAP.CD",
        "value": "GDP per capita (current US$)"
      },
      "country": {
        "id": "LV",
        "value": "Latvia"
      },
      "date": "2020",
      "value": 17384.412
    },
    {
      "indicator": {
        "id": "NY.GDP.PCAP.CD",
        "value": "GDP per capita (current US$)"
      },
      "country": {
        "id": "LV",
        "value": "Latvia"
      },
      "date": "2019",
      "value": 18051.391
    }
  ]
]
```

The JSON response contains:

- **Metadata** (page info, total entries)
- An **array of records**, each with indicator, country, date, and value
- Note: some numeric fields (e.g. `"per_page"`) are returned as strings
