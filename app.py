import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Qahwa Corner - Sales Dashboard")
st.write("Cloud Computing for Data Science - Assignment 1")

@st.cache_data
def load_data():
    df = pd.read_csv("cafe_sales.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()


branches = df['branch'].unique().tolist()
selected_branch = st.selectbox("Select Branch", ["All Branches"] + branches)

if selected_branch != "All Branches":
    filtered_df = df[df['branch'] == selected_branch]
else:
    filtered_df = df

total_revenue = filtered_df['total_sar'].sum()
st.metric(label="Total Revenue (SAR)", value=f"{total_revenue:,.2f} SAR")

st.subheader("Revenue by Product")
product_revenue = filtered_df.groupby('product')['total_sar'].sum().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(product_revenue['product'], product_revenue['total_sar'], color='skyblue')
plt.xticks(rotation=45, ha='right')
ax.set_ylabel("Revenue (SAR)")
ax.set_xlabel("Product")
st.pyplot(fig)
