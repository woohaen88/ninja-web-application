from ninja import Router
from django.contrib.auth import get_user_model
from core.models import Camping
from camping.schema import CampingIn

router = Router()


@router.post("/")
def create_camping(request, payload: CampingIn):
    camping = Camping.objects.create(user=request.user, **payload.dict())

    return camping
