# Weather FastAPI

A small intro weather api server created while learning Python.

## Features

- ⚡ Real-time city weather

## Tech Stack

- [uv](https://github.com/astral-sh/uv) - package and project manager
- [FastAPI](https://fastapi.tiangolo.com/) - modern web framework
- [httpx](https://www.python-httpx.org/) - HTTP client for Python 3
- [uvicorn](https://www.uvicorn.org/) - web server

## Setup

### 1. Install Dependencies

```sh
uv sync
```

### 2. Environment Variables

Copy the values from `env.example` to a `.env.local` file:

```sh
openweather_api_key=your-api-key
```

#### OpenWeather API key

To get the API key, you need to [subscribe](https://openweathermap.org/price) to the **Current Weather Data** API.

### 3. Run Development Server

```sh
uv run python main.py
```

Visit [http://0.0.0.0:8000](http://0.0.0.0:8000)

## Usage

### Routes

- GET `http://0.0.0.0:8000` - Service health check
- GET `http://0.0.0.0:8000/weather/berlin` - Weather info for `berlin`

## Architecture

### Weather API

We use the [OpenWeather](https://openweathermap.org/) API to get the current weather data for a specified city. Using the [Geocoding API](https://openweathermap.org/current#geocoding) we can

### Key Files

- `./main.py` - Sets up FastAPI web server

## MVP Limitations

- Limited amount of weather data

## Next Steps

- Add tests
- Refactor env loading
