from fastapi import APIRouter, HTTPException
from ..dataMgt import gdb

router = APIRouter()


@router.get("/")
@router.get("/health")
async def intel_pic_health():
    return {"intel_pic_status": "active", "intel_pic_version": "v0.0.1"}
