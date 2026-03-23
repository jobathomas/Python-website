import streamlit as st
import pandas as pd
import numpy as np


data = {
    "Price":[100,230,970,300,20,823,124],
    "Month":["January","February","March","April","May","June","July"]
}

df = pd.DataFrame(data)
st.header("Asteroid Store")
st.subheader("Welcome to the Asteroid belt")
st.bar_chart(data,x="Month",y="Price",x_label="Month of the Year",
              y_label="Price of Palladium",color=["green"])


sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f'Thanks for the feedback\nYou rated us {sentiment_mapping[selected]} stars!')