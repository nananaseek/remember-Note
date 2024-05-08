from tortoise import Model, fields


class User(Model):
    user_id = fields.IntField(pk=True, unique=True)
    projects: fields.ReverseRelation["Project"]


class Project(Model):
    id = fields.IntField(pk=True, unique=True)
    name = fields.CharField(max_length=32)
    description = fields.CharField(max_length=128)
    user: fields.ForeignKeyRelation['User'] = fields.ForeignKeyField(
        'models.User', related_name='project_user'
    )
    notes: fields.ReverseRelation['Notification']
    is_end = fields.BooleanField(default=False)


class Notification(Model):
    id = fields.IntField(pk=True, unique=True)
    project: fields.ForeignKeyRelation['Project'] = fields.ForeignKeyField(
        'models.Project', related_name='project_notifications'
    )
    notification = fields.CharField(max_length=2048)
    time_to_remember = fields.DatetimeField()
