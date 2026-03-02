from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    amount: float = Field(..., ge=0)
    account_tenure_days: int = Field(..., ge=0)
    country: str = Field(..., min_length=2, max_length=2)

class PredictResponse(BaseModel):
    risk_score: float
    risk_label: str
    top_features: list[str]
