# Car Damage Prediction

This project predicts vehicle damage category from car images using a ResNet50 model and serves it through a FastAPI backend with a Streamlit frontend.

## Project Structure
- `Data Science/` - training notebooks and dataset
- `Resources_FastAPI_Server/Download files/` - inference API backend
- `Resources_StreamLit_App/Download files/` - frontend UI that calls backend API

## End-to-End Flow
1. User uploads image in Streamlit app.
2. Streamlit sends image to `POST /predict` on FastAPI.
3. FastAPI loads trained model and runs inference.
4. API returns JSON prediction.
5. Streamlit shows predicted class in the UI.

## Run Backend
From `Resources_FastAPI_Server/Download files/`:

```commandline
pip install -r requirements.txt
fastapi dev server.py
```

Backend runs at `http://127.0.0.1:8000`.

## Run Frontend
From `Resources_StreamLit_App/Download files/`:

```commandline
pip install -r requirements.txt
streamlit run app.py
```

Set backend URL in app as `http://127.0.0.1:8000/predict` (default already set).
