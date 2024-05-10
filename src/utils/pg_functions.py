from src.modules.call_postgresV2 import CallPostgres

def pg_conn(cred):
    return CallPostgres(
        _dbname = cred['db'], 
        _user = cred['user'], 
        _pass = cred['pass'],
        _host = cred['host'],
        _port = cred['port']
    )

def pg_query(prepared_query, db_conn):
    """Realizar a query """
    
    resposta, check= db_conn.query(query=prepared_query)

    if check == True:
        err = f'[Erro ao executar a query: {resposta}]\n[Base atual: {db_conn.conn_atual()}]\n\n'
        # log_utility.process_log(40, 500, "SYSTEM", "pg-query", {}, err)
        print(err)
        return err, True
    else:
        return resposta, False
