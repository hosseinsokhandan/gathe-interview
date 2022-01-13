from fastapi import Request, HTTPException, Depends
from models.member import Member
from services.member import member_service
from services.permission import permission_service
import utils


async def get_current_user(request: Request) -> Member:
    try:
        username: str = request.headers["username"]
    except KeyError:
        raise HTTPException(status_code=401, detail="Unauthorized!")

    qs = await member_service.filter(username=username)
    if not qs:
        raise HTTPException(status_code=404, detail="User not found")

    return qs[0]


def admin_only(current_user: Member = Depends(get_current_user)):
    if not utils.is_admin(current_user):
        raise HTTPException(status_code=403, detail="Only admin is allowed!")


def is_admin(current_user: Member = Depends(get_current_user)):
    return utils.is_admin(current_user)


    
