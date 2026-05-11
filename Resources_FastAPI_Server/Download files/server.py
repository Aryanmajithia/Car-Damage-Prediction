from fastapi import FastAPI, File, UploadFile
from tempfile import NamedTemporaryFile
from model_helper import predict

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
async def get_prediction(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        with NamedTemporaryFile(delete=True, suffix=".jpg") as temp_file:
            temp_file.write(image_bytes)
            temp_file.flush()
            prediction = predict(temp_file.name)

        return {"prediction": prediction}
    except Exception as e:
        return {"error": str(e)}
