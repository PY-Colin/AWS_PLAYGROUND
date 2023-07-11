from fastapi import APIRouter, HTTPException
from ..dataMgt import gdb

router = APIRouter()


@router.get("/")
@router.get("/health")
async def compare_health():
    return {"comparison_status": "active", "comparison_version": "v0.0.1"}
