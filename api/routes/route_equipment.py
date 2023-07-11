from typing import List
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from ..dataMgt import gdb
import uuid
import json

base_db = "equipment"

router = APIRouter()


class Equipment(BaseModel):
    name: str
    age: int
    skill: List[str]
    email: str
    uid: str | None = None


@router.get("/")
async def equipment():
    return {"message": "Hello Equipment"}


@router.post("/create")
async def create(equip: Equipment):
    print(f" equip = {type(equip)}")
    equip_dict = equip.dict()
    uid = str(uuid.uuid4())
    print(f" uid = {uid}")
    equip_dict["uid"] = uid
    print(f" equip_dist = {equip_dict} of type {type(equip_dict)}")
    gdb.create_entity(
        "create (a:EQUIPMENT) " "set a +=  $data ",
        equip_dict,
        base_db,
    )
    return equip_dict


@router.put("/update")
async def update():
    qry = "MATCH (a:EQUIPMENT)  WHERE a.email= $email   set a +=  $data "
    data = {
        "name": "Jim Weber",
        "age": 45,
        "skill": ["Whovian", "Bike Maniac"],
        "email": "jim@neo4j.net",
    }
    db = base_db
    gdb.update_entity(qry, data, db)


@router.get("/read_all")
async def get_all():
    resp = gdb.read_all_entities(
        "MATCH (a:EQUIPMENT) RETURN COLLECT(properties(a)) AS  equip ",
        base_db,
    )
    print(f"entity_by_email = {resp}")
    return resp


@router.get("/read_by_ref/{reference}")
async def get_by_ref(reference: str = ""):
    resp = gdb.read_entity_by_email(
        "MATCH (a:EQUIPMENT) where a.email = $email RETURN COLLECT(properties(a)) AS  equip ",
        reference,
        base_db,
    )

    if resp == []:
        raise HTTPException(
            status_code=404,
            detail=f"Equipment with {reference=} could not be found!",
        )
    return resp
