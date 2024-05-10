#!/usr/bin/env python3

from fastapi import APIRouter
from src.models.requests import Client
from src.functions.clients.query_clients import get_clients_by_doc


router = APIRouter(
    tags=["FAST"]
)

@router.post('/clients')
def get_clients(client: Client):
    """
    # <code class="highlight">/fast/status/{protocol}</code>\n
    Returns the SPcode/AMTcode and client provider\n
    Request Parameters:\n
        document: client CPF or CNPJ\n
    Returns:\n
        status: Success/Failure\n
        message: System message, if there is any;\n
        error: System error message, if there is any.
    """

    res, err = get_clients_by_doc(client.document)
    
    if err:
        return err

    return res