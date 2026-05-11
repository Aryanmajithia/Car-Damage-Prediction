### Vehicle Damage Detection Backend Server

This FastAPI backend accepts a car image and returns the predicted damage class.

## Endpoints
- `GET /health`
```commandline
{
    "status": "ok"
}
```

- `POST /predict` (form-data field name: `file`)
```commandline
{
    "prediction": "Rear Breakage"
}
```

### Model Details
1. Used ResNet50 for transfer learning
2. Model was trained on around 1700 images with 6 target classes
   1. Front Normal
   1. Front Crushed
   1. Front Breakage
   1. Rear Normal
   1. Rear Crushed
   1. Rear Breakage
9. The accuracy on the validation set was around 80%

### Set Up
1. Install dependencies:
   ```commandline
   pip install -r requirements.txt
   ```

2. Run FastAPI server:
   ```commandline
   fastapi dev server.py
   ```

3. Verify server:
   ```commandline
   curl http://127.0.0.1:8000/health
   ```
