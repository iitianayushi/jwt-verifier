from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import jwt
from jwt.exceptions import InvalidTokenError
app = FastAPI(title="JWT Verification Gateway")
PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2okOHspNjgA+2rTLbeuY
cxiP/hG8C6Sb9iwg3yiLAA4HCnpITcbWCSelbvbYGuc3EbNy4xFyf5Cbj5DHJMID
EkryOgyd2giIIIBOUBj8S63uGcnRpOBh9NFatfNwheKuzsPuVNldu6A9cNteNpXc
WyJjG2axVfmq7i6SuKr1JoWYG7xTTAvKPujSl4OtsQfO3h5NepzdfXpr28oNnzfW
ed+zclR6BcmNNo/WVfJ4xyCLSf0BCOgdTgW6PdaChd1l9VDetJZVEgC5tkyvXsfI
SI6iyrYbKR0NEBSqq4XkadEjsCs4F1RncsS4LlgniT7GlkL9Mce3b0wGLs9/7ZIX
dQIDAQAB
-----END PUBLIC KEY-----"""
EXPECTED_ISSUER = "https://idp.exam.local"
EXPECTED_AUDIENCE = "tds-31xtcf1r.apps.exam.local"
class VerifyRequest(BaseModel):
    token: str
class VerifySucessResponse(BaseModel):
    valid: bool
    email: str
    sub: str
    aud: str
@app..get("/")
def read_root():
    return {"status": "Serverless FastAPI is running"}
@app.post("/verify")
async def verify_token(payload: VerifyRequest):
    try:
        decoded_token = jwt.decode(
            payload.token,
            PUBLIC_KEY,
            algorithms=["RS256"],
            audience=EXPECTED_AUDIENCE,
            issuer=EXPECTED_ISSUER
        )
        audience_claim = decoded_payload.get("aud", "")
        if isinstance(audience_claim, list):
            audience_str = audience_claim[0] if audience_claim else ""
        else:
            audience_str = audience_claim
        return VerifySuccessResponse(
            valid=True,
            email=decoded_payload.get("email", ""),
            sub=decoded_payload.get("sub", ""),
            aud=audience_str
             
            
        )
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"valid": False}
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"valid": False}
        )