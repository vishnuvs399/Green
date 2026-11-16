import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

st.set_page_config(page_title="GreenCompute", page_icon="🌱", layout="wide")

st.title("🌱 GreenCompute")
st.caption("Estimate the energy use and carbon footprint of everyday computing.")

with st.sidebar:
    st.header("⚙️ Usage settings")
    device = st.selectbox("Device type", ["Laptop", "Desktop PC", "Monitor", "Server"])
    watts_default = {"Laptop": 65, "Desktop PC": 250, "Monitor": 30, "Server": 500}
    watts = st.number_input("Average power (watts)", min_value=1.0, max_value=5000.0,
                            value=float(watts_default[device]), step=5.0)
    hours = st.slider("Hours used per day", 0.0, 24.0, 6.0, 0.5)
    days = st.slider("Days used per month", 1, 31, 26)
    devices = st.number_input("Number of devices", min_value=1, max_value=1000, value=1)
    factor = st.number_input("Grid emission factor (kg CO₂/kWh)",
                             min_value=0.0, max_value=3.0, value=0.70, step=0.01,
                             help="Editable estimate. Replace with a reliable local grid factor when available.")

daily_kwh = watts * hours * devices / 1000
monthly_kwh = daily_kwh * days
yearly_kwh = monthly_kwh * 12
monthly_co2 = monthly_kwh * factor
yearly_co2 = yearly_kwh * factor

st.info("This tool provides estimates based on the power and grid-emission values you enter. "
        "Actual consumption varies by workload, hardware, and electricity source.")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Daily electricity", f"{daily_kwh:.2f} kWh")
c2.metric("Monthly electricity", f"{monthly_kwh:.2f} kWh")
c3.metric("Monthly CO₂ estimate", f"{monthly_co2:.2f} kg")
c4.metric("Yearly CO₂ estimate", f"{yearly_co2:.2f} kg")

st.subheader("📊 Energy and emissions overview")
chart_data = pd.DataFrame({
    "Period": ["Daily", "Monthly", "Yearly"],
    "Electricity (kWh)": [daily_kwh, monthly_kwh, yearly_kwh],
    "CO₂ (kg)": [daily_kwh * factor, monthly_co2, yearly_co2]
})
left, right = st.columns(2)
with left:
    st.plotly_chart(px.bar(chart_data, x="Period", y="Electricity (kWh)",
                           title="Estimated electricity consumption"), use_container_width=True)
with right:
    st.plotly_chart(px.bar(chart_data, x="Period", y="CO₂ (kg)",
                           title="Estimated carbon emissions"), use_container_width=True)

st.subheader("♻️ What if you reduce usage?")
reduction = st.slider("Reduce daily usage by (%)", 0, 80, 20, 5)
saved_kwh = monthly_kwh * reduction / 100
saved_co2 = saved_kwh * factor
a, b, c = st.columns(3)
a.metric("Monthly energy saved", f"{saved_kwh:.2f} kWh")
b.metric("Monthly CO₂ avoided (estimate)", f"{saved_co2:.2f} kg")
c.metric("Yearly CO₂ avoided (estimate)", f"{saved_co2 * 12:.2f} kg")

st.subheader("💡 Sustainable computing recommendations")
tips = [
    ("Enable sleep mode", "Set your computer to sleep when inactive instead of leaving it running."),
    ("Reduce screen brightness", "Lowering monitor brightness can reduce display energy use."),
    ("Shut down unused devices", "Turn off devices and peripherals when they are not needed."),
    ("Extend hardware lifespan", "Repair, upgrade, and maintain devices instead of replacing them early."),
    ("Choose efficient workloads", "Avoid unnecessary background processes and repeated heavy computations."),
    ("Recycle responsibly", "Use certified e-waste collection points for retired electronics.")
]
for heading, body in tips:
    st.markdown(f"**{heading}:** {body}")

report = chart_data.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download energy report (CSV)", report,
                   file_name="greencompute_report.csv", mime="text/csv")

st.divider()
st.caption("GreenCompute | Sustainable Computing Course Project | Estimates are educational, not utility-billing measurements.")
