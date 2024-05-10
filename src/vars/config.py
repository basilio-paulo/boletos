import os
from dotenv import load_dotenv

load_dotenv('default.env')

"""Credenciais diretorio"""
DIR_CRED = {
    'db': os.getenv('_pgdb'),
    'user': os.getenv('_pguser'),
    'pass': os.getenv('_pgpass'),
    'host': os.getenv('_pghost'),
    'port': os.getenv('_pgport')
}