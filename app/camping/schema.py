from core.models import Camping
from ninja import ModelSchema
from django.contrib.auth import get_user_model


class UserSchema(ModelSchema):
    class Config:
        model = get_user_model()
        model_exclude = ["password"]


class CampingIn(ModelSchema):
    class Config:
        model = Camping
        model_fields = ["title", "visited_dt", "review", "price"]


class CampingOut(ModelSchema):
    # user = UserSchema

    class Config:
        model = Camping
        model_fields = [
            "title",
            "visited_dt",
            "review",
            "price",
            "created_dt",
            "updated_dt",
            # "user",
        ]
