#!/usr/bin/env python3
from pydantic import BaseModel

class Client(BaseModel):
    document: str