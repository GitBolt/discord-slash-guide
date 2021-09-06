import os
from typing import Union
from nacl.signing import VerifyKey
from fastapi import FastAPI, Request, HTTPException
from nacl.exceptions import BadSignatureError
from starlette.responses import JSONResponse

# Your public key can be found on your application in the Developer Portal
PUBLIC_KEY = os.environ["PUBLIC_KEY"]

app = FastAPI()

def verify_key(signature: str, timestamp: str, body: str) -> bool:
    print(timestamp)
    print(signature)

    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))
    
    try:
        verify_key.verify(f'{timestamp}{body}'.encode(),
                          bytes.fromhex(signature))
        return True
    except BadSignatureError:
        return False


@app.get("/")
async def index() -> JSONResponse:
    return JSONResponse(
        status_code=200, 
        content={"Message": "Welcome to interaction webhook server"}
        )
        
        
@app.post("/interactions")
async def index(request: Request) -> Union[JSONResponse, HTTPException]:
    
    signature = request.headers["X-Signature-Ed25519"]
    timestamp = request.headers["X-Signature-Timestamp"]
    body = request.body.decode("utf-8")

    if verify_key(signature, timestamp, body):
        return JSONResponse(status_code=200, content=request.json())
    else:
        return HTTPException(
            status_code=401, detail={"error": "Incorrect request"}
        )

