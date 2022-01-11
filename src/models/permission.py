from tortoise import Model, fields


class CategoryPermission(Model):
    category = fields.ForeignKeyField("models.Category", related_name="cat_permission")
    member = fields.ForeignKeyField("models.Member", related_name="cat_permission")
    can_create = fields.BooleanField(default=False)
    can_read = fields.BooleanField(default=False)
    can_update = fields.BooleanField(default=False)
    can_delete = fields.BooleanField(default=False)


class DocumentPermission(Model):
    document = fields.ForeignKeyField("models.Document", related_name="doc_permission")
    member = fields.ForeignKeyField("models.Member", related_name="doc_permission")
    can_create = fields.BooleanField(default=False)
    can_read = fields.BooleanField(default=False)
    can_update = fields.BooleanField(default=False)
    can_delete = fields.BooleanField(default=False)
