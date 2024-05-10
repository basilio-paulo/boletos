from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, SecretStr, EmailStr
from model import internal_models, request_schemas

class BasicResponse(BaseModel):
    status: str
    message: str

class BasicHit(BasicResponse):
    hit: bool

class BasicHost(BasicResponse):
    host: Union[str, None] = None

class BasicJob(BasicResponse):
    job: str

class BasicJob(BasicResponse):
    job: str

class BasicDataResponse(BasicResponse):
    data: Union[str, list, dict]

class FoundJobs(BasicResponse):
    num_items: int
    items: list

class FoundJob(BasicJob):
    hits: int
    items: list

class JobStatus(BasicJob):
    job_status: bool

class BasicServer(BasicResponse):
    server_response: Union[str, list, dict]

class BasicSkyone(BasicResponse):
    id_skyone: str

class BasicPod(BasicResponse):
    pod_response: list

class BasicGit(BasicResponse):
    squads: str

class BasicGitBranch(BasicResponse):
    branch: str

class BasicApp(BasicResponse):
    app: str

class AppVersions(BasicApp):
    versions: list

class AppVersion(BasicApp):
    version: str

class AppUpdateRequest(AppVersion):
    id_skyone: str
    email: str

class SyncResponse(BasicResponse):
    sync_code: str

class GitRepoResponse(BasicResponse):
    sync_code: str
    repo_name: str
    created_at: datetime
    repo_url: str

class BasicRoles(BaseModel):
    user: str
    roles: list

class ClientRoles(BasicRoles):
    client: str

class RealmRoles(BasicRoles):
    realm: str

class LoginLink(BaseModel):
    login_link: str

class LogoutLink(BaseModel):
    logout_link: str

class QueryReturn(BasicResponse):
    successfully_executed: Union[list, None] = None
    responses: Union[list, None] = None
    offending_queries: Union[list, None] = None

class MigrationFastu(BaseModel):
    status: str
    errors: dict
    execution_times: dict | None = None

class FastuBase(BaseModel):
    app: str | None = None
    id_skyone: str
    version: str
    ver_db: str | None = None
    task: str | dict
    data: datetime
    email: EmailStr
    execution_times: dict | None = None
    migration: MigrationFastu | None = None

class LogFastu(BaseModel):
    status: FastuBase

class InsertIntoVault(internal_models.VaultInsertResponse):
    pass

class GetFromVault(request_schemas.VaultCert):
    expires_at: str

class VaultPathsList(BaseModel):
    returned_paths: list