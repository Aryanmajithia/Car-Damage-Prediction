# Vehicle Damage Detection Frontend (Streamlit)

This app uploads a car image to the FastAPI backend and shows the predicted damage class.
The model is trained on third-quarter front and rear car views.

![app](app_screenshot.jpg)

## How it works
1. User uploads a `.jpg` or `.png` image in Streamlit.
2. Streamlit sends the image to backend `POST /predict`.
3. FastAPI runs inference with the trained model and returns JSON.
4. Streamlit displays the returned prediction.

## Setup
1. Install dependencies:
   ```commandline
   pip install -r requirements.txt
   ```

2. Start FastAPI backend first (default at `http://127.0.0.1:8000`).

3. Start Streamlit:
   ```commandline
   streamlit run app.py
   ```

4. In UI, keep backend URL as `http://127.0.0.1:8000/predict` (or set env var `BACKEND_PREDICT_URL`).