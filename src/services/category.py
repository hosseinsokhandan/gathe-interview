from models.document import Category


class CategoryService:
    async def create(self, name):
        return await Category.create(name=name)

    async def list_all(self):
        return await Category.all()


category_service = CategoryService()
