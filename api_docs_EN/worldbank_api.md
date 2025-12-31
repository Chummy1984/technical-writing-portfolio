# Documenting GDP per Capita with the World Bank API

## **tl;dr**
- Retrieve GDP per capita time series data from the World Bank API
- Focus on endpoint structure, parameters, and JSON responses
- Includes a minimal Quickstart with example requests

## 1. Quickstart 
To quickly retrieve Latvia’s GDP per capita between 2000 and 2020 as JSON in a single response, use:

```bash
curl "https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD?date=2000:2020&format=json&per_page=500"
```
This request:
- limits the time range to 2000–2020 using `date`
- requests JSON output using `format=json`
- avoids pagination by returning the full time series using `per_page=500`

The response contains:
- metadata (pagination and total number of records)
- a list of yearly GDP per capita values for Latvia

## 2. Introduction

This documentation explains how to retrieve GDP per capita data from the World Bank API.

Each dataset is identified by a unique indicator code.  
For GDP per capita (current US dollars), the indicator code is `NY.GDP.PCAP.CD`.

The API returns the requested data as a time series for the specified years.
Responses are available in XML (default) and JSON format.
No authentication is required.

## 3. Endpoint and Response Format

To retrieve GDP per capita data for Latvia, use the following endpoint:

```http
GET https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD
```

By default, the response is returned in XML. To get the data in JSON, add the `format=json` parameter: 

```http
GET https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD?format=json
```

## 4. Optional Parameters

The following optional parameters can be used to refine the request:

| Parameter | Description | Type | Default | Notes |
| --- | --- | --- | --- | --- |
| `date` | Limits the data to a specific time range. | string | full dataset | Format: `YYYY:YYYY` (e.g. `2000:2020`). |
| `format` | Defines the response format. | string | XML | Use `json` for JSON output. Affects only presentation, not data. |
| `per_page` | Number of results per page. | integer | 50 | Set to 500 to return the full time series in one response. Otherwise, multiple pages may be needed. |

**Example request with all parameters combined:**

```http
GET https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD?date=2000:2020&format=json&per_page=500
```

## 5. Sample Responses 

### 5.1. Sample Response XML (default format)

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
</data>

```

The XML response includes metadata, indicator and country information, and a sample yearly record.

### 5.2. Sample Response JSON (with `format=json`)

To receive the response in JSON format, add the `format=json` parameter to the request. 

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
    }
  ]
]
```

The JSON response is a two-element array:
- the first element contains metadata
- the second element contains the data records

Note: some numeric fields (e.g. `per_page`) are returned as strings.

## 6. Use Case: Retrieve Latvia’s GDP per Capita

### 6.1. Goal
This section shows how to retrieve Latvia’s GDP per capita between 2000 and 2020 using the World Bank API.

### 6.2. Step-by-step Explanation

1. Select the indicator (`NY.GDP.PCAP.CD`).
2. Use the country-specific endpoint.
3. Add optional parameters (`date`, `format`, `per_page`) to refine the request.
4. Send the complete request and process the response.
    
### 6.3. Sample Request

#### 6.3.1. XML (default)

The following request retrieves Latvia’s GDP per capita between 2000 and 2020 in the default XML format:

```http
GET https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD?date=2000:2020&per_page=500
```

`date=2000:2020` specifies the time range

`per_page=500` avoids pagination

XML is returned by default

#### 6.3.2. JSON

```http
GET https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD?date=2000:2020&format=json&per_page=500
```

This version adds the `format=json` parameter to the request.

### 6.4 Typical integration workflow

In practice, the World Bank API is typically used as part of a simple data pipeline:

1. **Fetch data**  
   Send a `GET` request with the desired `country`, `indicator`, `date`, and `per_page` parameters.

2. **Parse the response**  
   Convert the JSON or XML response into native data structures.

3. **Filter by year**  
   Select the records relevant for the analysis or visualisation.

4. **Handle missing values**  
   Account for missing data (`null` in JSON, `xsi:nil="true"` in XML).

5. **Pass processed data to the next layer**  
   Use the cleaned time series for charts, dashboards, reports, or further analysis.

This workflow is reusable across countries and indicators by changing only the `country` and `indicator` codes.


## **7. Error Handling and Edge Cases**

The World Bank API does not provide detailed error messages. However, some typical failure scenarios can occur:

### 7.1 Invalid Indicator Code

If the indicator code is incorrect (e.g. `NY.GDP.PCAP.WRONG`), the API returns an empty response:

```xml
<data/>
```

In JSON, the same request returns an empty array `[]`.

**Interpretation:** Check the indicator code. If invalid, adjust and retry.

### 7.2 No Data Available

If no value exists for the requested year or country, the response contains a null value.

**Example JSON (excerpt):**

```json
[
  {
    "date": "2021",
    "value": null}
]
```

**Example XML:**

```xml
<record>
  <date>2021</date>
  <value xsi:nil="true"/>
</record>
```

**Interpretation:** The data for this year has not yet been published.

### 7.3 Pagination Issues

By default, the API limits results to 50 records per page. If the time series is longer, additional pages must be requested.

**Recommendation:** Always set `per_page=500` (maximum allowed value) to receive the full series in one response.

### 7.4 HTTP Status Codes

The API uses standard HTTP status codes:

- `200 OK`: Request successful, data returned
- `400 Bad Request`: Invalid parameter (e.g. wrong indicator or country code)
- `404 Not Found`: The resource does not exist (wrong URL)
- `500 Internal Server Error`: Temporary problem on the World Bank server

## 8. Best Practices for Using the World Bank API

When working with the World Bank API, the following practices help ensure reliable and efficient results:

- **Set `per_page=500`:** Avoid pagination by requesting the entire time series in a single response.
    
- **Choose the right format:** JSON is easier to parse in most environments; XML may be preferred in organisations that use schema validation or have existing XML-based workflows.
    
- **Specify a date range:** Use `date=YYYY:YYYY` to limit the dataset to relevant years and reduce response size.
    
- **Handle null values explicitly.** Missing data appears as `"value": null` (JSON) or `<value xsi:nil="true"/>` (XML).

- **Verify country and indicator codes before sending requests.** Typos result in empty responses.

## 9. Extending to Other Countries and Indicators

The same request structure can be reused across different countries and indicators.

- **Change the country code.**  
  Replace `LV` with another ISO country code (e.g. `DE`, `US`).

- **Change the indicator code.**  
  Replace `NY.GDP.PCAP.CD` with another World Bank indicator (e.g. `SP.POP.TOTL` for total population).

Example: Retrieve Germany’s population between 2010 and 2020 in JSON format:

```http
GET https://api.worldbank.org/v2/country/DE/indicator/SP.POP.TOTL?date=2010:2020&format=json&per_page=500
```


## 10. Conclusion

This documentation showed how to retrieve and work with GDP per capita data using the World Bank API.

Key takeaways:
- The API follows a consistent request and response structure across countries and indicators.
- JSON responses are generally easier to process, while XML may be required in specific environments.
- Null values and pagination require explicit handling to avoid downstream errors.
- The same request pattern can be reused by adjusting country and indicator codes.

These patterns make the World Bank API suitable for integration into data analysis, reporting, and other data-driven workflows.
