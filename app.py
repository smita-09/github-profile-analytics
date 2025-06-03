import os
import pandas as pd
import streamlit as st
import pytz

# Page Configuration
st.set_page_config(page_title="GitHub Views Dashboard", layout="wide")

# Title
st.title("📊 GitHub Profile Analytics")
st.markdown("This dashboard shows traffic data (views) for your public repositories over the last 14 days.")

# Load Data
DATA_FOLDER = "data"
repo_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith("_views.csv")]

if not repo_files:
    st.warning("No data found. Please run fetch_github_data.py to generate view data.")
    st.stop()

repo_names = [f.replace("_views.csv", "") for f in repo_files]  # trims unnecessary stuff
selected_repo = st.selectbox("Select a repository", repo_names)

# Read selected data
df = pd.read_csv(os.path.join(DATA_FOLDER, f"{selected_repo}_views.csv"))

# Process timestamps
df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
df["timestamp_local"] = df["timestamp"].dt.tz_convert("Europe/Amsterdam")


# Show metrics
total_views = df["count"].sum()
unique_visitors = df["uniques"].sum()
st.metric("🔁 Total Views", total_views)
st.metric("👤 Unique Visitors", unique_visitors)

# Visualizations
st.subheader("📈 Views over Time")
st.line_chart(df.set_index("timestamp_local")[["count"]])

st.subheader("👥 Unique Visitors over Time")
st.bar_chart(df.set_index("timestamp_local")[["uniques"]])

# Raw data toggle
with st.expander("See raw data"):
    st.dataframe(df)
