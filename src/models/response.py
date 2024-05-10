from pydantic import BaseModel

class ClientsResponse(BaseModel):
    document: str
    cloudcli: str
    provider: str