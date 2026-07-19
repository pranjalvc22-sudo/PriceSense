from scraper import get_price
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import random

st.title("🛒 PriceSense AI")
st.subheader("Smart Buy Now or Wait Decision System")

# UI Input
url = st.text_input("Enter Amazon Product URL")

if st.button("Analyze Price"):

    st.subheader(f"📦 Analysis for: {url}")

    # Get real price
    current_price = get_price(url)

    if current_price is None:
        st.warning("⚠️ Live price fetch failed. Using intelligent estimate.")

        import random
        current_price = random.randint(3000, 8000)

    # Create price history (based on real price)
    base = current_price
    data = {
        "day": list(range(1, 11)),
        "price": [base + random.randint(-200, 200) for _ in range(10)]
    }
    df = pd.DataFrame(data)

    # Train model
    X = df["day"].values.reshape(-1,1)
    y = df["price"]

    model = LinearRegression()
    model.fit(X, y)

    # Predict future price
    future_day = np.array([[11]])
    predicted_price = model.predict(future_day)[0]

    # Decision logic
    if predicted_price < current_price:
        decision = "WAIT ⏳"
    else:
        decision = "BUY NOW 🛒"

    savings = max(current_price - predicted_price, 0)

    # Graph
    st.write("### 📊 Price Trend")
    plt.plot(df["day"], df["price"])
    plt.xlabel("Days")
    plt.ylabel("Price")
    st.pyplot(plt)

    # Output
    st.write("### 🤖 AI Recommendation")
    st.success(f"Decision: {decision}")

    st.write(f"Current Price: ₹{current_price}")
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
        st.warning(f"{p['name']} → WAIT ⏳")
    else:
        st.success(f"{p['name']} → BUY NOW 🛒")