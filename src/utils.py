from models.member import Member

def is_admin(current_user: Member):
    return current_user.username == "admin"