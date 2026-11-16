# 🌱 GreenCompute — Sustainable Computing Monitor

GreenCompute is a Streamlit application that estimates electricity consumption and associated carbon emissions from computer usage. It also simulates potential savings when device usage is reduced.

## Features
- Estimate daily, monthly, and yearly electricity consumption.
- Estimate CO₂ emissions using an editable grid-emission factor.
- Compare electricity use and emissions with interactive charts.
- Simulate energy and emissions savings from reduced usage.
- View practical sustainable-computing recommendations.
- Download a CSV report.

## Technology
- Python
- Streamlit
- Pandas
- Plotly

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (recommended).
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   streamlit run app.py
   ```

## Deploy using GitHub + Streamlit Community Cloud

1. Create a GitHub repository named `greencompute`.
2. Upload `app.py`, `requirements.txt`, and `README.md` to the repository root.
3. Sign in to Streamlit Community Cloud using GitHub.
4. Select **Create app**, choose your repository and branch, and set the main file path to `app.py`.
5. Deploy. Streamlit will build the app using `requirements.txt`.

## Calculation methodology

Electricity consumption:

`kWh = (Power in watts × hours per day × number of devices × days) / 1000`

Estimated emissions:

`CO2 (kg) = electricity (kWh) × grid emission factor (kg CO2/kWh)`

The default emission factor is an illustrative value and is editable. Replace it with a credible, location-appropriate value and cite that source in any academic submission.

## Limitations
- Power consumption is entered by the user; the app does not measure hardware power directly.
- Emissions depend on the chosen grid-emission factor.
- Results are estimates and should not be presented as measured electricity-bill data.

## Possible future improvements
- Save multiple devices and compare them.
- Add monthly usage history with SQLite.
- Add region-specific emission-factor presets with citations.
- Add a campus computer-lab dashboard.
