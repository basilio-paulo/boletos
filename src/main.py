#!/usr/bin/env python3
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Cloud Api",#API_DATA['PROJECT_NAME'],
    version="2024.04.0"#API_DATA['API_VERSION'],
)

"""Configuracoes de CORS"""
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from src.routes.clients import clients

app.include_router(clients.router)

@app.get("/")
def root():
    return {
        "message": "For documentation, access /docs or /redoc",
        "links": [f"{os.environ['DNS']}/docs", f"{os.environ['DNS']}/redoc"]
        }