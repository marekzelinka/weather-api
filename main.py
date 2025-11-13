import os
import sys

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

apiKey = os.getenv("OPENWEATHER_API_KEY")
if apiKey is None:
    raise ValueError("Missing env var: apiKey")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Weather API with uv!", "python_version": sys.version}


@app.get("/weather/{city}")
async def get_weather(city: str):
    r = httpx.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={apiKey}"
    )
    weather = r.json()

    return {
        "city": city,
        "temperature": weather["main"]["temp"],
        "condition": weather["weather"][0]["description"],
        "powered_by": "uv",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
