import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv(r"C:\Users\AakashMahawar\PycharmProject\jupyter\rumah.csv")
df = df[0:1000]

# Display the data using Streamlit
st.title('Rumah123')

# Create the histogram using Matplotlib with more visible bars
fig, ax = plt.subplots()  # Create a figure and axes object
ax.hist(df['normalized_price'], bins=30, color='blue', alpha=0.75, rwidth=0.85, edgecolor='black')  # Increase the number of bins
ax.set_xlabel('Price')  # Set x-axis label
ax.set_ylabel('Frequency')  # Set y-axis label
ax.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid lines

# Display the Matplotlib figure in Streamlit
st.pyplot(fig)
