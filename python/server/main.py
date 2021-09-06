import os
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from fastapi import FastAPI, Request, HTTPException
from starlette.responses import JSONResponse, Response

app = FastAPI()
# Your public key can be found on your application in the Developer Portal
PUBLIC_KEY = os.environ["PUBLIC_KEY"]
EXAMPLE_RESPONSE = {
    "type": 4,
    "data":{
        "content": "Successfully received command",
        "flags": 1
    }
}

# Simple function to verify request sent from Discord
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
async def interactions(request: Request) -> Response:
    
    signature = request.headers["X-Signature-Ed25519"]
    timestamp = request.headers["X-Signature-Timestamp"]
    body = await request.body()
    body = body.decode("utf-8")
       
    if verify_key(signature, timestamp, body):

        json_body = await request.json()

        if json_body["type"] == 1:
            return {"type": 1} # Ack ping
        else:
            return EXAMPLE_RESPONSE # If not ping, send example response
    else:
        return HTTPException(
            status_code=401, detail={"error": "Incorrect request"}
        )