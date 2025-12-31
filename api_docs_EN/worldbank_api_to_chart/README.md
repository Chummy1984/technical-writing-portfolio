# From API to Chart: GDP per Capita (World Bank API)

## Goal
Fetch GDP per capita data from the World Bank API and turn it into a simple line chart.  
This mini project demonstrates the workflow from API request → parsing → data preparation → visual output.

## Data source
World Bank API endpoint:
`/v2/country/{country}/indicator/{indicator}`

Example:
https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD?date=2000:2020&format=json&per_page=500

## How it works (high level)
1. Request JSON data for a country + indicator
2. Extract year/value pairs from the response
3. Remove missing values and sort by year
4. Plot the time series

## Run locally
```bash
pip install -r requirements.txt
python plot_gdp_per_capita.py

Notes

World Bank responses may contain null values for some years.

The API returns metadata + data in a two-element JSON array.


### 2) `from-api-to-chart/requirements.txt`
```txt
requests
pandas
matplotlib
import requests
import pandas as pd
import matplotlib.pyplot as plt

COUNTRY = "LV"  # Latvia
INDICATOR = "NY.GDP.PCAP.CD"  # GDP per capita (current US$)
DATE_RANGE = "2000:2020"

URL = (
    f"https://api.worldbank.org/v2/country/{COUNTRY}/indicator/{INDICATOR}"
    f"?date={DATE_RANGE}&format=json&per_page=500"
)

def fetch_data(url: str) -> list[dict]:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    data = r.json()

    # World Bank JSON: [metadata, data_records]
    if not isinstance(data, list) or len(data) < 2:
        raise ValueError("Unexpected response format (expected [metadata, records]).")

    return data[1]

def to_dataframe(records: list[dict]) -> pd.DataFrame:
    rows = []
    for item in records:
        year = item.get("date")
        value = item.get("value")
        if year is None:
            continue
        rows.append({"year": int(year), "value": value})

    df = pd.DataFrame(rows)
    df = df.dropna(subset=["value"]).sort_values("year")
    return df

def plot(df: pd.DataFrame) -> None:
    plt.figure()
    plt.plot(df["year"], df["value"])
    plt.title(f"GDP per capita ({COUNTRY})")
    plt.xlabel("Year")
    plt.ylabel("GDP per capita (current US$)")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    records = fetch_data(URL)
    df = to_dataframe(records)
    if df.empty:
        raise RuntimeError("No data after cleaning (all values missing?).")
    plot(df)

3) from-api-to-chart/plot_gdp_per_capita.py
