from typing import TypeVar

from pydantic import BaseModel
from tortoise import models

from database.model import User, Project, Notification
from database import schemas

ModelType = TypeVar("ModelType", bound=models.Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
GetSchemaType = TypeVar("GetSchemaType", bound=BaseModel)


class BaseServices:
    model = ModelType
    create_schema = CreateSchemaType
    get_schema = GetSchemaType

    async def create(self, schema: create_schema, **kwargs) -> ModelType:
        return await self.model.create(**schema.model_dump(exclude_unset=True), **kwargs)

    async def get(self, **kwargs) -> ModelType:
        return await self.model.get(**kwargs)

    async def delete(self, **kwargs) -> None:
        return await self.model.delete(**kwargs)

    async def all(self) -> list[ModelType]:
        return await self.model.all()


class UserServices(BaseServices):
    model = User
    create_schema = schemas.create_pydantic_user
    get_schema = schemas.get_pydantic_user


class ProjectServices(BaseServices):
    model = Project
    create_schema = schemas.create_pydantic_project
    get_schema = schemas.get_pydantic_project


class NotificationServices(BaseServices):
    model = Notification
    create_schema = schemas.create_pydantic_notification
    get_schema = schemas.get_pydantic_notification
