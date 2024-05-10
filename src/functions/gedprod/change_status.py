from functions.utils.generic import pg_conn
from functions.postgres.common_queries import pg_query


def update_query(receipt_number:int, status_code: int, db_conn):

    prepared_query = \
        f"""
        UPDATE financas.titulos 
        SET situacao = {status_code} 
        WHERE numero = '{receipt_number}'
        AND tenant = '47'
        ;"""

    response, err, cols = pg_query(prepared_query, db_conn)

    return response, err, cols



def change_status(receipt_number:int, status_code:int, PRODWEB_CRED: dict):
    db_conn = pg_conn(PRODWEB_CRED)

    if status_code == 0:
        status = "opened"
    if status_code == 1:
        status = "paided"

    response, err, code = update_query(receipt_number, status_code, db_conn)
    
    result = {}

    if err and code == 400:
        result["message"] = response["message"]
        result["status"] = "Failed"
        return (result, response), err, 500    
    elif err:
        result["message"] = f"Unable to update status to {status} for receipt: {receipt_number}"
        result["status"] = "Failed"
        return (result, response), err, 500


    result["message"] = f"Change completed, receipt '{receipt_number}' had its status changed to: {status} "
    result["status"] = "Success"
    result["server_response"] = response

    return result, err, code
