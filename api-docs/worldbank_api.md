# Documenting GDP per Capita with the World Bank API

## **tl;dr**
- Explains how to retrieve GDP per capita via the World Bank API
- Focus: endpoint structure, JSON responses, clear example requests
- Demonstrates API logic, technical clarity, and developer-facing documentation skills

## 1. Quickstart 
To quickly retrieve Latvia’s GDP per capita between 2000 and 2020 as JSON in a single response, use:

```bash 
  curl "https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD?date=2000:2020&format=json&per_page=500" 
  ```

This request:
- uses GET to read data from the World Bank API
- limits the time range to 2000–2020 via the date parameter
- requests JSON instead of the default XML via format=json
- sets per_page=500 to avoid pagination and return the full time series in one response

The response contains:
- metadata (pagination and total number of records)
- a list of yearly GDP per capita values for Latvia

## 2. Introduction

This documentation shows how to retrieve Latvia’s GDP per capita using the World Bank API.

The World Bank assigns a unique indicator code to each dataset. For GDP per capita (current US dollars), the code is `NY.GDP.PCAP.CD`.

This code must be included in the request URL to retrieve the data.

The data is returned as a time series covering multiple years.

The API supports both XML (default) and JSON. No authentication is required.

In this documentation, I focus on structure and readability.
## 3. Endpoint and Response Format

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

## 4. Optional Parameters

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

## 5. Sample Responses - XML and JSON

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

### 5.2. Sample Response JSON (with `format=json`)

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

## 6. Use Case: Retrieve Latvia’s GDP per Capita

### 6.1. Goal

This section walks you through retrieving Latvia’s GDP per capita between 2000 and 2020 using the World Bank API.

### 6.2. Step-by-step Explanation

To retrieve Latvia’s GDP per capita between 2000 and 2020, follow these steps:

1. **Choose the correct indicator.**
    
    The World Bank uses the indicator code `NY.GDP.PCAP.CD` to refer to GDP per capita in current US dollars.
    
2. **Define the endpoint.**
    
    The base endpoint for retrieving indicator data for a specific country is:
    
    For Latvia and GDP per capita, this becomes:
    
    ```
    https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD
    ```
    
3. **Add optional parameters.**
    
    To refine the query and make the response easier to process, use the following parameters:
    
    - `date=2000:2020` limits the data to the desired time range.
    - `format=json` requests the response in JSON rather than the default XML.
    - `per_page=500` ensures that the entire time series is returned in a single response without pagination.
4. **Construct the complete request.**
    
    Combining the endpoint and parameters results in the following URL:
    
    ```
    https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD?date=2000:2020&format=json&per_page=500
    ```
    
5. **Send the request.**
    
    Use the HTTP method `GET` to retrieve the data. No authentication is required
    

### 6.3. Sample Request

#### 6.3.1. Requesting XML (default)

The following request retrieves Latvia’s GDP per capita between 2000 and 2020 in the default XML format:

```
GET https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD?date=2000:2020&per_page=500
```

This request includes:

– `date=2000:2020` to specify the time range

– `per_page=500` to avoid pagination and return the full time series

– No `format` parameter is needed, as XML is the default

---

#### 6.3.2. Requesting JSON

To receive the response in JSON format instead of XML, use:

```
GET https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD?date=2000:2020&format=json&per_page=500
```

This version adds the `format=json` parameter to the request.

## **7. Response Interpretation and Documentation**

### 7.1 XML Response (default)

By default, the API returns data in XML format. Shortened example:

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
  <!-- ... -->
</data>
```

**Explanation:**

- `<indicator>` and `<country>` define the context
- Each `<record>` contains one data point: `<date>` + `<value>`
- Metadata elements (`<page>`, `<total>`) describe pagination and result size

To find Latvia’s GDP per capita for a specific year, locate the `<record>` with the matching `<date>`.

---

### 7.2 JSON Response

If the request includes `format=json`, the response is returned in JSON format:

```javascript
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
      "date": "2019",
      "value": 18051.391
      // indicator and country omitted for brevity
    }
    // ...
  ]
]
```

**Explanation:**

- The JSON response has two elements:
    1. An object with metadata (pagination, total results)
    2. An array of data records, each with `date`, `value`, and context fields
- The GDP per capita for a specific year is under the `value` key of the matching `date`

## **8. Error Handling and Edge Cases**

The World Bank API does not provide detailed error messages. However, some typical failure scenarios can occur:

### 8.1 Invalid Indicator Code

If the indicator code is incorrect (e.g. `NY.GDP.PCAP.WRONG`), the API returns an empty response:

```xml
<data/>
```

In JSON, the same request returns an empty array `[]`.

**Interpretation:** Check the indicator code. If invalid, adjust and retry.

---

### 8.2 No Data Available

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

---

### 8.3 Pagination Issues

By default, the API limits results to 50 records per page. If the time series is longer, additional pages must be requested.

**Recommendation:** Always set `per_page=500` (maximum allowed value) to receive the full series in one response.

---

### 8.4 HTTP Status Codes

The API uses standard HTTP status codes:

- `200 OK`: Request successful, data returned
- `400 Bad Request`: Invalid parameter (e.g. wrong indicator or country code)
- `404 Not Found`: The resource does not exist (wrong URL)
- `500 Internal Server Error`: Temporary problem on the World Bank server

## 9. Best Practices for Using the World Bank API

When working with the World Bank API, the following practices help ensure reliable and efficient results:

- **Set `per_page=500`:**
    
    Avoid pagination by requesting the entire time series in one response.
    
- **Choose the right format:**
    
    JSON is easier to parse in most programming environments and integrates well with data analysis tools.
    
    XML may be preferred in organisations that use schema validation or have existing XML-based workflows.
    
- **Specify a date range:**
    
    Use `date=YYYY:YYYY` to limit the dataset to relevant years.
    
    This reduces response size and makes the output easier to handle.
    
- **Check for null values:**
    
    Some years may not have published data.
    In JSON this appears as `"value": null`, in XML as `<value xsi:nil="true"/>`
    
    **Why it matters:**
    
    – Prevents calculation errors in analysis (e.g. averages, growth rates).
    
    – Avoids misleading visualisations (null interpreted as 0).
    
    – Helps distinguish between “no data yet” and “real numeric value”.
    
- **Verify codes:**
    
    Make sure the **country code** (e.g. `LV`) and the **indicator code** (e.g. `NY.GDP.PCAP.CD`) are correct before sending the request.
    
    Typos result in empty responses.

## 10. Extending to Other Countries and Indicators

The approach shown in this case study can be easily transferred to other datasets. 

- **Change the country code:**
    
    Replace `LV` with another ISO country code (e.g. `DE` for Germany, `US` for the United States).
    
- **Change the indicator code:**
    
    Replace `NY.GDP.PCAP.CD` with another World Bank indicator (e.g. `SP.POP.TOTL` for total population).
    

**Example:** Retrieve Germany’s population between 2010 and 2020 in JSON format:

```
GET https://api.worldbank.org/v2/country/DE/indicator/SP.POP.TOTL?date=2010:2020&format=json&per_page=500
```

This demonstrates how the same request structure can be reused across multiple indicators and countries.

As a result, the World Bank API offers a consistent and flexible way to access diverse economic and demographic data.

## 11. Conclusion

This case study demonstrated how to construct a request to the World Bank API, interpret both XML and JSON responses, and apply best practices for reliable results.

Key insights include:

- The API’s response structure is predictable and can be applied across different datasets.
- JSON is generally easier for analysis, while XML may be required in specific workflows.
- Null values and pagination must be handled carefully to avoid errors.
- By adjusting country and indicator codes, the same method can be extended to a wide range of economic and demographic indicators.

Overall, the World Bank API is an accessible and robust resource for retrieving time series data.

With clear documentation and attention to best practices, it can be seamlessly integrated into research, reporting, and data-driven applications.
