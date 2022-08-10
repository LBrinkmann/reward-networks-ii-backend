from app.models.base import ExtBaseModel, PyObjectId
from app.models import Experiment
from typing import Optional


class User(ExtBaseModel):
    user_id: Optional[PyObjectId] = None
    experiment_id: Experiment
    prolific_id: str
