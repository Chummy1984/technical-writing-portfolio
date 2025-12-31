import requests
import pandas as pd
import matplotlib.pyplot as plt

COUNTRY = "EE"  # Estonia
INDICATOR = "NY.GDP.PCAP.CD"  # GDP per capita (current US$)
DATE_RANGE = "2000:2020"

URL = (
    f"https://api.worldbank.org/v2/country/{COUNTRY}/indicator/{INDICATOR}"
    f"?date={DATE_RANGE}&format=json&per_page=500"
)

def fetch_data(url):
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    data = response.json()

    # World Bank API returns: [metadata, data_records]
    return data[1]

def to_dataframe(records):
    rows = []
    for item in records:
        year = item.get("date")
        value = item.get("value")

        if year is None:
            continue

        rows.append({
            "year": int(year),
            "value": value
        })

    df = pd.DataFrame(rows)
    df = df.dropna(subset=["value"]).sort_values("year")
    return df

def plot(df):
    plt.figure()
    plt.plot(df["year"], df["value"])
    plt.title("GDP per capita (Estonia)")
    plt.xlabel("Year")
    plt.ylabel("GDP per capita (current US$)")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    records = fetch_data(URL)
    df = to_dataframe(records)
    plot(df)
