#!/usr/bin/env python3

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys

class CallPostgres():
    """Carga inicial do Objeto, para instanciar a conexao com o banco"""
    def __init__(
        self, 
        _dbname = "postgres",
        _user = "postgres", 
        _pass = "admin", 
        _host = "localhost", 
        _port = "5432") -> None:

        self._dbname = _dbname
        self._user = _user
        self._pass = _pass
        self._host = _host
        self._port = _port

        self.create_connection()

    def change_database(self, database):
        self._dbname = database
        self.create_connection()

    def get_host(self):
        return self._host

    def conn_atual(self):
        return f'Host - {self._host}, Db - {self._dbname}'

    # def __setattr__(self, attr, value):
    #     if attr == 'teste':
    #         print('teste changed to {}'.format(value))
    #     super().__setattr__(attr, value)

    """Metodo para criar a conexao"""
    def create_connection(self):
        self.conn = psycopg2.connect(
            dbname=self._dbname, 
            user=self._user, 
            password=self._pass, 
            host=self._host, 
            port=self._port,
            connect_timeout=5)

    """Query generica de teste de conexao"""
    def test_connection(self):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.execute('SELECT 1')
                    teste = cur.fetchall()
                    print("OK")
                except:
                    print("Erro de conexao com o banco de dados")
                    sys.exit(2)

    """Funcao de execucao de querys"""
    def query(self, query):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute(query)
                    try:
                        records = cur.fetchall()
                        colnames = [desc[0] for desc in cur.description]
                        return records, colnames
                    except:
                        records = cur.statusmessage
                        count = cur.rowcount
                        return records, count
        except Exception as e:
            return str(e), 'Error'
    
    def transactionless_query(self, query):
        self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            try:
                records = cursor.fetchall()
                colnames = [desc[0] for desc in cursor.description]
                return records, colnames
            except:
                records = cursor.statusmessage
                count = cursor.rowcount
                return records, count
        except Exception as e:
            records = str(e)
            colnames =  'Error'
        finally:
            cursor.close()
        
        return records, colnames 

    def open_transaction(self):
        self.transaction = self.conn.cursor()

    def query_open_transaction(self, query):
        if not self.transaction:
            return None, None

        try:
            self.transaction.execute(query)
            try:
                records = self.transaction.fetchall()
                colnames = [desc[0] for desc in self.transaction.description]
                return records, colnames
            except:
                records = self.transaction.statusmessage
                count = self.transaction.rowcount
                return records, count
        except Exception as e:
            return str(e), 'Error'

    def close_transaction(self):
        self.transaction.close()

"""
Em construcao
Finalidade: limpar a poluicao de querys cruas em codigo
"""
class QueryBuilder():
    def get(vars, source, condition= None):
        prefix = f"Select {vars} From {source}"

        if condition != None:
            suffix = f"Where {condition}"
        else:
            suffix = ";"

        return prefix + " " + suffix