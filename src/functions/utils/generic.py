from datetime import datetime, timedelta, timezone
import sys
from fastapi import status
from functions.modulos.call_postgresV2 import CallPostgres

class Cronometer():
    def __init__(self) -> None:
        self.starting_time = datetime.now()

    def elapsed_time(self) -> float:
        """
        Returns the elapsed time from the beginning until now, in seconds.
        """
        now = datetime.now()
        return (now - self.starting_time).total_seconds()

class ByteSize():
    def variable(var):
        return sys.getsizeof(var)

def pg_conn(cred):
    return CallPostgres(
        _dbname = cred['db'], 
        _user = cred['user'], 
        _pass = cred['pass'],
        _host = cred['host'],
        _port = cred['port']
    )

def remove_key_from_list_of_dicts(list_of_dicts, key_to_remove):
    return [{k: v for k, v in d.items() if k != key_to_remove} for d in list_of_dicts]

def version_compare(v1, v2):
    arr1 = v1.split(".") 
    arr2 = v2.split(".") 
    n = len(arr1)
    m = len(arr2)
     
    arr1 = [int(i) for i in arr1]
    arr2 = [int(i) for i in arr2]

    if n>m:
        for i in range(m, n):
            arr2.append(0)
    elif m>n:
        for i in range(n, m):
            arr1.append(0)

    for i in range(len(arr1)):
      if arr1[i]>arr2[i]:
         return 1
      elif arr2[i]>arr1[i]:
         return -1
    return 0

def removeduplicate(it):
    seen = []
    for x in it:
        if x not in seen:
            yield x
            seen.append(x)

def remove_null_none_empty(ob):
    l = {}
    for k, v in ob.items():
        if(isinstance(v, dict)):
            x = remove_null_none_empty(v)
            if(len(x.keys())>0):
                l[k] = x
        
        elif(isinstance(v, list)):
            p = []
            for c in v:
                if(isinstance(c, dict)):
                    x = remove_null_none_empty(c)
                    if(len(x.keys())>0):
                        p.append(x)
                elif(c is not None and c != ''):
                    p.append(c)
            l[k] = p
        elif(v is not None and v!=''):
            l[k] = v
    return l

def is_datetime_valid(hour, minute):
    try:
        current_datetime = datetime.now(timezone.utc)  # Get current UTC time
        current_datetime = current_datetime.astimezone(timezone(timedelta(hours=-3)))  # Convert to timezone -3
        input_datetime = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour, minute, tzinfo=timezone(timedelta(hours=-3)))

        if 0 <= hour <= 23 and 0 <= minute <= 59 and input_datetime > current_datetime:       
            return input_datetime.strftime("%d/%m/%Y %H:%M")
        
        else:
            print("nope, não é valido")
            return False
    
    except ValueError:
        return False  # Invalid date format
    
    except TypeError:
        return False

def remove_value_from_key(data, key):
    for d in data:
        if key in data[d]:
            data[d].remove(key)
    return data

STATUS_CODE = {
    200: status.HTTP_200_OK,
    201: status.HTTP_201_CREATED,
    202: status.HTTP_202_ACCEPTED,
    400: status.HTTP_400_BAD_REQUEST,
    401: status.HTTP_401_UNAUTHORIZED,
    500: status.HTTP_500_INTERNAL_SERVER_ERROR
}