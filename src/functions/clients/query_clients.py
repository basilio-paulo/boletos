#!/usr/bin/env python3
import json
from src.utils.pg_functions import pg_conn, pg_query
from src.models.requests import Client
# from src.models.response import ClientsResponse
from src.vars.config import DIR_CRED

def pg_get_client_info(client: str):
    dir_conn = pg_conn(DIR_CRED)
    prepared_query = f"""
        select na.codigo from diretorio.nuvem_ambientes na
        join diretorio.clientes c on na.clientes_id = c.id
        where c.cnpj='{client}' or c.cpf='{client}'
    """
    res, err = pg_query(prepared_query, dir_conn)

    if err:
        return err, True

    return res, False

def get_clients_by_doc(client: str):
    res, err = pg_get_client_info(client)

    if res == []:
        return {"message": "cliente não possui ambiente nuvem"}, False

    if err:
        return {"message": "erro ao consultar documento na base"}, True
    
    data = []
    for i in res:
        if 'SP' in i[0]:
            client_res = {
                'document': client,
                'cloudcli': i[0],
                'provider': 'SKYONE'
            }
        elif 'AMT' in i[0]:
            client_res = {
                'document': client,
                'cloudcli': i[0],
                'provider': 'AMT'
            }
        else:
            client_res = {
                'document': client,
                'cloudcli': i[0],
                'provider': ''
            }

        data.append(client_res)

    return data, False