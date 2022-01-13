from tortoise import Model, fields


class Permission(Model):
    member = fields.ForeignKeyField("models.Member")
    can_create = fields.BooleanField(default=False)
    can_read = fields.BooleanField(default=False)
    can_update = fields.BooleanField(default=False)
    can_delete = fields.BooleanField(default=False)

    class Meta:
        abstract = True


class CategoryPermission(Permission):
    category = fields.ForeignKeyField("models.Category", related_name="cat_permission")

    class Meta:
        table = "category_permission"


class DocumentPermission(Permission):
    document = fields.ForeignKeyField("models.Document", related_name="doc_permission")

    class Meta:
        table = "document_permission"
