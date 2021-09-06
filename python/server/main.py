import os
from nacl.signing import VerifyKey
from fastapi import FastAPI, Request, HTTPException
from nacl.exceptions import BadSignatureError

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


@app.post("/")
async def index(request: Request) -> str:
    
    signature = request.headers["X-Signature-Ed25519"]
    timestamp = request.headers["X-Signature-Timestamp"]
    body = request.body.decode("utf-8")

    if verify_key(signature, timestamp, body):
        return request.json()
    else:
        return HTTPException(
            status_code=401, detail={"error": "Incorrect request"}
        )

