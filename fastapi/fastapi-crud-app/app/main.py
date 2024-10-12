# from fastapi import FastAPI
# from .routes import router

# app = FastAPI()

# app.include_router(router)

# # Swagger available at /docs
# app/main.py
from fastapi import FastAPI
from app.routers import items, clock_in
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FastAPI CRUD Assignment",
    description="APIs for managing items and clock-in records",
    version="1.0.0"
)

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(items.router, tags=["Items"])
app.include_router(clock_in.router, tags=["Clock-In Records"])

# Root
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI CRUD Assignment!"}
