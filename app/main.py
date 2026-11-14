from fastapi import FastAPI
from loguru import logger

from app.routers import api, dashboard

logger.add("logs/app.log", rotation="1 week", retention="1 month")

# Initialise the core app.
app = FastAPI(title="NHS Performance Dashboard")

logger.info("Starting NHS Performance Dashboard API")

# not used. commented out.
# app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Connect to the hospital routers folder
logger.info("Including API and dashboard routers")
app.include_router(dashboard.router)
app.include_router(api.router)


@app.get("/health")
async def health_check():
    """A quick system check to see if the the server is up and running."""

    return {"status": "online", "version": "1.0.0"}
