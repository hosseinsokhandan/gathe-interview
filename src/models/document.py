from tortoise import Model, fields


class Category(Model):
    name = fields.CharField(null=False, max_length=64)


class Document(Model):
    author = fields.ForeignKeyField("models.Member", related_name="docs")
    category = fields.ForeignKeyField("models.Category", related_name="docs")
    subject = fields.CharField(null=False, max_length=128)
    content = fields.TextField()
