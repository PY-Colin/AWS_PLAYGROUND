from fastapi import APIRouter, HTTPException

base_db = "people"

router = APIRouter()


@router.get("/")
async def people():
    return {"message": "Hello staff"}


@router.post("/create")
async def create():
    pass


@router.put("/update")
async def update():
    pass


@router.get("/read_all")
async def get_all():
    pass


@router.get("/read_by_ref")
async def get_by_ref():
    pass
