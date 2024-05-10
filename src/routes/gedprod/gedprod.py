#!/usr/bin/env python3

from fastapi import APIRouter, Depends, HTTPException, Response, status, BackgroundTasks


from model.return_schemas import BasicServer

from functions.gedprod.change_status import change_status
from typing import Union
from vars.secrets import PRODWEB_CRED

#from fastapi_keycloak import OIDCUser
#from roles.permissions import Method, verify_permission, CURRENT_USER
#from main import log_utility, log_billing
#from functions.utils.generic import Cronometer, ByteSize

router = APIRouter(
    tags=["ERP"]
)

@router.put("/erp/gedprod/boletos", response_model=BasicServer)

def change_receipt_status(receipt_number: str, status_code: int
                          #, user: OIDCUser = Depends(CURRENT_USER)
                          ):
    """
    # <code class="highlight">/erp/gedprod/boletos</code>
    An endpoint to modify the client's receipt status, either to opened or paided.\n
    Confirmation with the finance team is required to confirm payment has been made.\n
    Request parameters:\n
        Receipt Number: Client's receipt number (numbers only).\n
        Status Code: A number that defines the status: 0 - opened, 1 - paided.\n
   
    Returns:\n
        status: Success/Failure;\n
        message: System message, if there is any;\n
        server_response: Response returned from the servers after execution.\n
    """
    # authorized = verify_permission(Method['PUT'], user, "/erp/skyone/status")
    # if not authorized:
    #     raise HTTPException(status_code=401, detail="User not Authorized")
    # if status > 1 or status < 0:
    #     raise HTTPException(status_code=code, detail="invalid operation")
    
    # cronometer = Cronometer()

    # time_finish = cronometer.elapsed_time()

    result, err, code = change_status(receipt_number, status_code, PRODWEB_CRED)

    if err:
        message = {'server': result[1], 'api': result[0]}
        # log_utility.process_log(40, code, user.preferred_username, 'PUT', "/erp/gedprod/boletos", {}, message)
        # log_billing.process_log(40, 'ERP API', user.preferred_username, f"/erp/gedprod/boletos", ByteSize.variable(result), time_finish, code)
        raise HTTPException(status_code=code, detail=result[0])

    # log_utility.process_log(20, code, user.preferred_username, 'PUT', "/erp/gedprod/boletos", {}, result)
    # log_billing.process_log(20, 'ERP API', user.preferred_username, f"/erp/gedprod/boletos", ByteSize.variable(result), time_finish, 200)

    return result