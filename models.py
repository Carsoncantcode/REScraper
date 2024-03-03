from pydantic import BaseModel, Field, HttpUrl
from typing import Optional

class ScrapePropertyParameters(BaseModel):
    location: str = Field(..., example="Irvine, CA", description="The location to scrape properties from.")
    past_days: int = Field(..., gt=0, example=7, description="Number of past days to search.")
    radius: int = Field(..., gt=0, example=10, description="The miles radius around the location.")

    class Config:
        schema_extra = {
            "example": {
                "location": "Irvine, CA",
                "past_days": 7,
                "radius": 10,
            }
        }
