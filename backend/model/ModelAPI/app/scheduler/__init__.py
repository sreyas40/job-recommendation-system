"""
Module for the scheduler for the ModelAPI application.

"""

from ..schemas import schemas
from ..crud import crud
from ..utils import get_db

from .scheduler import job_recommendation_scheduler
