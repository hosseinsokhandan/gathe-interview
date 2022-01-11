from models.member import Member
from schemas.permission import PermissionInSchema


class MemberService:
    async def filter(self, username: str):
        return await Member.filter(username=username)


member_service = MemberService()
