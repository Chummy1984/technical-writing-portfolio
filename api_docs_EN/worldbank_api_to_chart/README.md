# From API to Chart: GDP per Capita (World Bank API)

## Goal
Fetch GDP per capita data for Estonia (EE) from the World Bank API and turn it into a simple line chart.
This demonstrates the workflow from API request → parsing → data preparation → visual output.

## Data source
Example request:
`GET /v2/country/EE/indicator/NY.GDP.PCAP.CD?date=2000:2020&format=json&per_page=500`

Base URL: https://api.worldbank.org


