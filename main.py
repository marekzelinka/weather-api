import sys

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Weather API with uv!", "python_version": sys.version}


@app.get("/weather/{city}")
async def get_weather(city: str):
    return {
        "city": city,
        "temperature": 22,
        "condition": "sunny",
        "powered_by": "uv",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


def hello():
    print("Hello")


def world():
    print("world")
