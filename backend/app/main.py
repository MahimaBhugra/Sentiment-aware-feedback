from fastapi import FastAPI

app = FastAPI(
    title="Sentiment-Aware Feedback Classifier",
    description="API for analyzing customer feedback"
)


@app.get("/")
def home():
    return {
        "message": "Backend is running successfully!"
    }