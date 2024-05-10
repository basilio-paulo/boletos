from functions.utils.generic import pg_conn

def pg_query(prepared_query, db_conn, single_result = True, dict_result = False, transactionless = False):
    """
    Execute query and treat outputs.
    - Single result is for queries where you only want one item. Returns the item and nothing else.
    - Dict result is if you want to transform the result(s) into a dict following the scheme {"column": "item"}.
    - Transactionless is for queries that require transactionless connections (Drop, Create...).
    """
    if transactionless:
        db_conn.transactionless_query(prepared_query)
    else:
        response, check = db_conn.query(prepared_query)

    if check == 'Error':
        err = f'[Error executing query: {response}]'
        return err, True, check
    elif len(response) < 1 or type(response) == str or not (single_result or dict_result):
        return response, False, check
    elif dict_result:
        processed_result = []
        for result in response:
            processed_result.append(dict(zip(check, result)))
        return processed_result, False, check
    else:
        return response[0][0], False, check

def check_if_exists(db_name: str, server_cred: dict):
    """Check if a database exists on the given server"""
    db_conn = pg_conn(server_cred)
    db_server = server_cred["host"]

    prepared_query = \
    f"""SELECT 1 AS result FROM pg_database
    WHERE datname={db_name};
    """

    response, err, cols = pg_query(prepared_query, db_conn)

    if err:
        error = {"message": f"Error executing query on {db_server}, please contact a system administrator."}
        return (error, response), True, 500

    return False if len(response) < 1 else True, err, 404 if len(response) < 1 else 200