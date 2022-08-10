from app.models.base import ExtBaseModel, PyObjectId
from app.models import Action, Step, Environment
from typing import List, Optional


class Solution(ExtBaseModel):
    solution_id: Optional[PyObjectId] = None
    environment_id: Environment
    step_id: Step
    actions: List[Action]
