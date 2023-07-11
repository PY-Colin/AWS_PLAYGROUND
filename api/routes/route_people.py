from fastapi import APIRouter, HTTPException
from ..dataMgt import gdb

base_db = "people"

router = APIRouter()


@router.get("/")
async def people():
    return {"message": "Hello people"}


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
        "MATCH (a:EQUIPMENT) where a.email = $email RETURN COLLECT(properties(a)) AS  equip ",
        ref,
        base_db,
    )
    print(f"entity_by_email = {resp}")
    print(f"ref = {ref}")
    return resp
