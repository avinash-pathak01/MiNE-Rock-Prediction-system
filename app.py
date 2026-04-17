import streamlit as st
import pickle
import numpy as np
import os

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Rock vs Mine", page_icon="🚀")

# -------------------------------
# Load Model (Cached)
# -------------------------------
@st.cache_resource
def load_model():
    model_path = "model.pkl"
    
    if not os.path.exists(model_path):
        st.error("❌ model.pkl file not found. Please upload it.")
        return None
    
    with open(model_path, "rb") as f:
        return pickle.load(f)

model = load_model()

# -------------------------------
# UI
# -------------------------------
st.title("🚀 Rock vs Mine Prediction")
st.write("rebuild")  # ✅ ADDED LINE (force rebuild)
st.write("Enter 60 sonar values to classify object")

# Input box
input_data = st.text_area(
    "Enter 60 comma-separated values:",
    height=100
)

# Example helper
st.caption("Example: 0.02,0.03,0.01,...")

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):
    if model is None:
        st.stop()

    try:
        data = list(map(float, input_data.strip().split(',')))

        if len(data) != 60:
            st.error("❌ You must enter exactly 60 values")
        else:
            data_array = np.array(data).reshape(1, -1)
            prediction = model.predict(data_array)[0]

            if prediction == 'R' or prediction == 0:
                st.success("🪨 Result: ROCK")
            else:
                st.success("💣 Result: MINE")

    except:
        st.error("❌ Invalid input! Please enter numbers only.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
