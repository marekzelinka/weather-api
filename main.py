import sys

import httpx
from fastapi import FastAPI

from settings import Settings

app = FastAPI()
settings = Settings.model_validate({})


@app.get("/")
async def root():
    return {
        "message": "Weather API with uv and OpenWeather!",
        "python_version": sys.version,
    }


@app.get("/weather/{city}")
async def get_weather(city: str):
    r = httpx.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={
            settings.openweather_api_key
        }"
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
