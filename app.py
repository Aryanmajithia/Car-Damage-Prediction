import os

import requests
import streamlit as st

st.title("Vehicle Damage Detection")
st.caption("Upload a car image and get prediction from FastAPI backend")

backend_url = st.text_input(
    "Backend URL",
    value=os.getenv("BACKEND_PREDICT_URL", "http://127.0.0.1:8000/predict"),
)

uploaded_file = st.file_uploader("Upload the file", type=["jpg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded File", use_container_width=True)
    if st.button("Predict Damage", type="primary"):
        try:
            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type or "image/jpeg",
                )
            }
            response = requests.post(backend_url, files=files, timeout=60)
            response.raise_for_status()
            data = response.json()

            if "prediction" in data:
                st.success(f"Predicted Class: {data['prediction']}")
            else:
                st.error(f"Backend error: {data.get('error', 'Unknown error')}")
        except requests.exceptions.RequestException as exc:
            st.error(f"Could not reach backend: {exc}")
