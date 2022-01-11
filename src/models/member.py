from tortoise import Model, fields


class Member(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=128, unique=True)
