import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data_merge = pd.read_csv('data_merge.csv')
data_payments = pd.read_csv('data_payments.csv')

city_counts = data_merge['customer_city'].value_counts()
most_common_city = city_counts.index[0]
most_common_city_count = city_counts.iloc[0]

city_counts_min = city_counts.min()
least_common_cities = city_counts[city_counts == city_counts_min]

data_payments['payment_type'] = data_payments['payment_type'].replace('not_defined', pd.NA)
df_clean = data_payments.dropna(subset=['payment_type'])
payment_counts = df_clean['payment_type'].value_counts()
most_common_payment = payment_counts.index[0]
most_common_payment_count = payment_counts.iloc[0]

st.title("Customer and Payment Analysis Dashboard")

st.subheader("City with Most Customers")
st.write(f"**{most_common_city}** with {most_common_city_count} customers")

st.subheader("Cities with Fewest Customers")
for city, count in least_common_cities.items():
    st.write(f"**{city}** with {count} customers")

st.subheader("Top 10 Cities with Most Customers")
st.bar_chart(city_counts.head(10))

st.subheader("Most Common Payment Type")
st.write(f"**{most_common_payment}** with {most_common_payment_count} transactions")

st.subheader("Top 10 Payment Types")
st.bar_chart(payment_counts.head(10))

st.subheader("Analysis Insights")
st.write("""
**Solution 1:** Focus on increasing sales in cities with fewer customers, far below São Paulo.  
**Solution 2:** Increase sales using vouchers, such as promotions where customers who spend more get additional vouchers.
""")

st.write("Data is kept for future analysis, even if not currently cleaned.")
st.write("Link Analisis : https://colab.research.google.com/drive/1nu2rjJPe46O_EWtSMXGVcIXPP-lWZqZY#scrollTo=pM-C00K3eBRO")
