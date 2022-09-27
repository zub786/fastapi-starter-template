from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", status_code=201, description="Endoint to get Users list")
def get_users(identifier: Optional[str] = None):
    return JSONResponse(status_code=500, content={
                "detail": [
                    {
                        'id': '001',
                        'full_name': 'Zubair Shkoor'
                    }
                ]
            })
