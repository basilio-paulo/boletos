from datetime import datetime, date, time
from typing import Optional
from pydantic import BaseModel, SecretStr
from typing import Union

class DatabaseCredentials(BaseModel):
    db: str
    user: str
    password: str
    host: str
    port: int

class VaultAuth(BaseModel):
    method: str
    parameter: str = ""
    payload: dict

class VaultMetadataResponse(BaseModel):
    created_time: Union[str, datetime]
    custom_metadata: Union[str, None]
    deletion_time: Union[str, datetime]
    destroyed: bool
    version: int

class VaultInsertResponse(BaseModel):
    request_id: str
    lease_id: str
    renewable: bool
    lease_duration: int
    data: VaultMetadataResponse
    wrap_info: Union[str, None]
    warnings: Union[str, None]
    auth: Union[str, None]
    
class VaultSecretData(BaseModel):
    data: dict
    metadata: VaultMetadataResponse

class VaultSecretResponse(BaseModel):
    request_id: str
    lease_id: str
    renewable: bool
    lease_duration: int
    data: VaultSecretData
    wrap_info: Union[str, None]
    warnings: Union[str, None]
    auth: Union[str, None]