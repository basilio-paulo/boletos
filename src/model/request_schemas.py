from datetime import datetime, date, time
from typing import Optional, List
from pydantic import BaseModel, SecretStr, EmailStr
from typing import Union
from enum import Enum

class NewUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: SecretStr

class AttrGit(BaseModel):
    user_name: str
    squad: str

class RepoGit(BaseModel):
    repo_name: str
    squad: str

class TempPgUser(BaseModel):
    user_name: str
    client_db: str
    password: SecretStr

class ApiConfSearch(BaseModel):
    user_name: str
    client_db: str

class ApiConfUser(TempPgUser):
    host: str

class CloudOp(BaseModel):
    cloud_id: str
    emails: str

class BranchGit(BaseModel):
    repo_name: str
    branch: str

class AnalyJob(BaseModel):
    tenant: int
    ano: int
    mes: int
    nome_query: str
    empresa: Union[str, None] = None
    estabelecimento: Union[str, None] = None
    grupo_query: Union[str, None] = None
    data: Union[date, None] = None
    hora: Union[time, None] = None

class AnalyQuery(BaseModel):
    nome_query: str
    sql: str
    nome_tabela: str
    run_date: time

class CloudInstallation(BaseModel):
    cloud_code: str
    app_server: str
    db_srever: str
    erp_version: str
    db_name: str
    directory: str
    homolog: bool

class QueryVars(BaseModel):
    dbschema: str
    tablename: str
    query: str
    checkpoint: int

class SQLHotfix(BaseModel):
    query: List[QueryVars]
    total_checkpoint: int

class HotfixCloud(SQLHotfix):
    cloud_code: str
    database: str

class LogBase(BaseModel):
    app: str
    id_skyone: str | List[str]
    version: str
    ver_db: str | None = None

class MigrationOnly(BaseModel):
    id_skyone: str | List[str]
    version: str

class LogBaseIn(LogBase):
    task: str
    data: datetime
    email: EmailStr

class Status(Enum):
    active = 0
    revoked = 1

class Tenant(BaseModel):
    tenant: int

# class Certs(Enum):
#     ecnpj = ["a1", "a2", "a3"]
#     ecpf = ["a1", "a2", "a3"]

class VaultCert(BaseModel):
    base64: str
    password: str
    expires_at: date
    status: Status
    md5: str
    notify: Union[str, None] = None

class InsertVaultCert(BaseModel):
    cpfcnpj: str
    certname: str
    certificate: VaultCert