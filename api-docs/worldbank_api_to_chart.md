# From API to Chart: World Bank GDP per Capita (Latvia)

**Goal:** Fetch GDP per capita data from the World Bank API, normalise it, and use it for a simple time-series chart.

## Data source
Indicator: `NY.GDP.PCAP.CD` (GDP per capita, current US$)  
Country: `LV` (Latvia)  
Years: `2000–2020`

Open in browser:
https://api.worldbank.org/v2/country/LV/indicator/NY.GDP.PCAP.CD?date=2000:2020&format=json&per_page=500

## Pipeline
1. Fetch JSON data
2. Extract records array
3. Map to `{ year, value }`
4. Filter `null` values
5. Sort by year
6. Visualise as a line chart

## Example code
See: `src/fetchSeries.js`

## Output
*(Add chart image here once generated)*

