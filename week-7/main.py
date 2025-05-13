#!/usr/bin/env python
# coding: utf-8

# Data Collection & Setup

# In[3]:


# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px  # For choropleth map
from datetime import datetime
from IPython.display import display


# Set visualization style
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)


# Data Collection & Setup

# In[4]:


# Load the dataset (replace with your local path if needed)
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
try:
    covid_df = pd.read_csv(url)
    print("Dataset loaded successfully!")

    # Initial exploration
    print("\nFirst 5 rows:")
    display(covid_df.head())

    print("\nDataset info:")
    display(covid_df.info())

    print("\nMissing values summary:")
    display(covid_df.isnull().sum().sort_values(ascending=False).head(20))

except Exception as e:
    print(f"Error loading dataset: {e}")


# Data Cleaning

# In[ ]:


# Select countries of interest
countries = ["Kenya", "United States", "India", "Brazil", "Germany"]
filtered_df = covid_df[covid_df["location"].isin(countries)].copy()

# Convert date column
filtered_df["date"] = pd.to_datetime(filtered_df["date"])

# Handle missing values for key metrics
cols_to_fill = [
    "total_cases",
    "total_deaths",
    "new_cases",
    "new_deaths",
    "total_vaccinations",
]
filtered_df[cols_to_fill] = filtered_df[cols_to_fill].fillna(0)

# Calculate death rate
filtered_df["death_rate"] =\
    filtered_df["total_deaths"] / filtered_df["total_cases"]

print("\nCleaned data summary:")
display(filtered_df.describe())


# Exploratory Data Analysis (EDA)

# Total Cases Over Time

# In[ ]:


plt.figure(figsize=(14, 7))
sns.lineplot(data=filtered_df, x="date", y="total_cases", hue="location")
plt.title("Total COVID-19 Cases Over Time")
plt.ylabel("Total Cases")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.show()


# Total Deaths Over Time

# In[ ]:


plt.figure(figsize=(14, 7))
sns.lineplot(data=filtered_df, x="date", y="total_deaths", hue="location")
plt.title("Total COVID-19 Deaths Over Time")
plt.ylabel("Total Deaths")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.show()


# Daily New Cases Comparison

# In[ ]:


plt.figure(figsize=(14, 7))
sns.lineplot(data=filtered_df, x="date", y="new_cases", hue="location")
plt.title("Daily New COVID-19 Cases")
plt.ylabel("New Cases")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.show()


# Death Rate Analysis

# In[ ]:


latest_data = filtered_df[filtered_df["date"] == filtered_df["date"].max()]
plt.figure(figsize=(10, 6))
sns.barplot(data=latest_data, x="location", y="death_rate")
plt.title("COVID-19 Death Rate by Country")
plt.ylabel("Death Rate (Deaths/Cases)")
plt.xlabel("Country")
plt.show()


# Total Vaccinations Over Time

# In[ ]:


plt.figure(figsize=(14, 7))
sns.lineplot(
    data=filtered_df, x="date", y="total_vaccinations", hue="location")
plt.title("Total Vaccinations Over Time")
plt.ylabel("Total Vaccinations")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.show()


# People Fully Vaccinated (%)

# In[ ]:


plt.figure(figsize=(14, 7))
sns.lineplot(
    data=filtered_df, x="date", y="people_fully_vaccinated_per_hundred",
    hue="location"
)
plt.title("Percentage of Population Fully Vaccinated")
plt.ylabel("% Fully Vaccinated")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.show()


# Choropleth Map (Global View)

# In[5]:


# Prepare latest global data
latest_global = covid_df[covid_df["date"] == covid_df["date"].max()]
latest_global = latest_global[
    ["iso_code", "location", "total_cases_per_million"]
].dropna()

# Create interactive map
fig = px.choropleth(
    latest_global,
    locations="iso_code",
    color="total_cases_per_million",
    hover_name="location",
    color_continuous_scale=px.colors.sequential.Plasma,
    title="Global COVID-19 Cases per Million People",
)
fig.show()


# In[ ]:
