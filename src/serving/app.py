from fastapi import FastAPI
from src.serving.schemas import PredictRequest, PredictResponse

app = FastAPI(title="ai-production-ml-system")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    score = min(1.0, (payload.amount / 10000.0) + (0.2 if payload.account_tenure_days < 30 else 0.0))
    label = "high" if score >= 0.7 else "medium" if score >= 0.4 else "low"
    return PredictResponse(
        risk_score=round(score, 4),
        risk_label=label,
        top_features=["amount", "account_tenure_days", "country"],
    )
