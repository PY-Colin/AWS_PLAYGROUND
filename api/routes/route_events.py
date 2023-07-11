from fastapi import APIRouter, HTTPException
from ..dataMgt import gdb

base_db = "events"

router = APIRouter()


@router.get("/")
async def events():
    return {"message": "Hello Events"}


@router.post("/create")
async def create():
    pass


@router.put("/update")
async def update():
    pass


@router.get("/read_all")
async def get_all():
    pass


@router.get("/read_by_ref/{ref}")
async def get_by_ref(ref: str = ""):
    resp = gdb.read_entity_by_email(
        "MATCH (e :EQUIPMENT) where e.uid = $uid RETURN COLLECT(properties(e)) AS equip ",
        ref,
        base_db,
    )
    print(f"entity_by_email = {resp}")
    print(f"ref = {ref}")
    return resp
