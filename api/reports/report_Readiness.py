from fastapi import APIRouter, HTTPException
from ..dataMgt import gdb

router = APIRouter()


@router.get("/")
@router.get("/health")
async def readiness_health():
    return {"readiness_status": "active", "readiness_version": "v0.0.1"}
