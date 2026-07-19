import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("🛒 PriceSense AI")
st.subheader("Smart Buy Now or Wait Decision System")

# Dummy dataset
df = pd.read_csv("data/price_history.csv")

# Train model
X = df["day"].values.reshape(-1,1)
y = df["price"]

model = LinearRegression()
model.fit(X, y)

# UI Input
product = st.text_input("Enter Product Name")

if st.button("Analyze Price"):
    st.subheader(f"📦 Analysis for: {product}")
    current_price = df["price"].iloc[-1]
    future_day = np.array([[11]])
    predicted_price = model.predict(future_day)[0]

    # Decision logic
    if predicted_price < current_price:
        decision = "WAIT ⏳"
    else:
        decision = "BUY NOW 🛒"

    savings = max(current_price - predicted_price, 0)

    # Output
    st.write("### 📊 Price Trend")
    plt.plot(df["day"], df["price"])
    plt.xlabel("Days")
    plt.ylabel("Price")
    st.pyplot(plt)

    st.write("### 🤖 AI Recommendation")
    st.success(f"Decision: {decision}")

    st.write(f"Predicted Price: ₹{int(predicted_price)}")
    st.write(f"Potential Savings: ₹{int(savings)}")

    # Smart Alert
    if decision == "WAIT ⏳":
        st.warning("📢 Smart Alert: Price likely to drop. Wait!")
    else:
        st.success("📢 Smart Alert: Good time to buy!")

# Smart Cart Section
st.write("---")
st.subheader("🛍 Smart Cart Optimization")

products = [
    {"name": "Laptop", "current": 50000, "predicted": 48000},
    {"name": "Headphones", "current": 3000, "predicted": 3200}
]

for p in products:
    if p["predicted"] < p["current"]:
        decision = "WAIT"
        st.warning(f"{p['name']} → WAIT ⏳")
    else:
        decision = "BUY NOW"
        st.success(f"{p['name']} → BUY NOW 🛒")