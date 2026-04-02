from fastapi import FastAPI
from app.routers import dashboard, api

# Initialize the core app.
app = FastAPI(title="NHS Performance Dashboard")

# not used. commented out.
#app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Connect to the hospital routers folder
app.include_router(dashboard.router)
app.include_router(api.router)

@app.get("/health")
async def health_check():
    """A quick system check to see if the the server is up and running."""

    return {"status": "online", "version": "1.0.0"}