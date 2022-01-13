from models.permission import Permission


async def create_permission_helper(
    model: Permission,
    user: int,
    can_read=True,
    can_delete=True,
    can_update=True,
    can_create=True,
    **kwargs
):

    return await model.create(
        member_id=user,
        can_read=can_read,
        can_delete=can_delete,
        can_update=can_update,
        can_create=can_create,
        **kwargs
    )
