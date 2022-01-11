from fastapi import APIRouter
from fastapi.params import Depends
from models.member import Member
from deps import get_current_user, admin_only
from schemas.permission import PermissionInSchema, PermissionOutSchema
from services.permission import permission_service

router = APIRouter()


@router.post("/create", response_model=PermissionOutSchema)
async def create_permission(
    permission_data: PermissionInSchema,
    current_user: Member = Depends(get_current_user),
    admin_only: bool = Depends(admin_only),
):
    return await permission_service.set_permission(permission_data)
