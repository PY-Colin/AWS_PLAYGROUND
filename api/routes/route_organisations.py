from fastapi import APIRouter, HTTPException

base_db = "organisations"

router = APIRouter()


@router.get("/")
async def organisations():
    return {"message": "Hello organisations"}


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
