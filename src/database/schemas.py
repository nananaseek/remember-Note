from tortoise.contrib.pydantic import pydantic_model_creator

from database.model import User, Project, Notification

get_pydantic_user = pydantic_model_creator(User)
create_pydantic_user = pydantic_model_creator(User)

get_pydantic_notification = pydantic_model_creator(Notification)
create_pydantic_notification = pydantic_model_creator(Notification, exclude=('id', 'time_to_remember'))

get_pydantic_project = pydantic_model_creator(Project)
create_pydantic_project = pydantic_model_creator(Project, exclude=('id', 'notes', 'is_end'))
