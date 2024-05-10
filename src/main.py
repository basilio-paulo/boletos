#!/usr/bin/env python3
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.gedprod import gedprod


app = FastAPI(
    title="SRE API",#API_DATA['PROJECT_NAME'],
    description="API infraestrutura",#API_DATA['PROJECT_DESCRIPTION'],
    version="2024.02.21"#API_DATA['API_VERSION'],
)

app.include_router(gedprod.router)

@app.get("/")
def root():
    return {
        "message": "For documentation, access /docs, /redoc or /mkdocs",
        "links": [f"{os.environ['DNS']}/docs", f"{os.environ['DNS']}/redoc", f"{os.environ['DNS']}/mkdocs"]
        }