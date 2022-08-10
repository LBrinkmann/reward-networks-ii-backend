from app.models.base import ExtBaseModel, PyObjectId
from app.models import Experiment, Treatment, Environment
from typing import List, Optional


class Chain(ExtBaseModel):
    chain_id: Optional['PyObjectId'] = None
    experiment_id: 'Experiment'
    treatment_name: 'Treatment'
    environment_ids: List['Environment']
