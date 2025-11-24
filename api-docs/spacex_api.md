# Retrieving Launch Data with the SpaceX API

## **tl;dr**
> **Status:** Work in Progress  
> This documentation is currently being developed and will be expanded step by step.
- Explains how to retrieve launch and rocket data from the SpaceX API
- Focus: endpoint structure, filtering, and readable JSON examples
- Demonstrates developer-focused documentation for a real-world API

## 1. Introduction

The SpaceX API provides public information about launches, rockets, and missions.  
It requires no authentication and returns structured JSON data.  
This guide demonstrates the basic pattern of retrieving launch information.

## 2. Base URL

### Base URL

```
https://api.spacexdata.com/v4/
```

---

## 3. Retrieve Latest Launch

### Endpoint
### Endpoint

```
GET /launches/latest
```

---

### Example Request

```
curl https://api.spacexdata.com/v4/launches/latest
```

---

### Example Response (truncated)

```json
{
  "name": "FalconSat",
  "date_utc": "2006-03-24T22:30:00.000Z",
  "success": false,
  "rocket": "5e9d0d95eda69955f709d1f1"
}
```

### Field Overview
- name — mission name  
- date_utc — launch date in UTC  
- success — indicates launch success (true/false)  
- rocket — ID for requesting rocket details (via /rockets/{id})

## 4. Next Steps (Planned)

- Document corresponding rocket details  
- Explain nested JSON fields  
- Add parameter usage and error handling  

---



