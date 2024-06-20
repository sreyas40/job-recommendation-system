from fastapi import APIRouter
from ..crud import jobrecommendation as jobcrud
from ..utils import get_db

from .jobrecommendation import router as jobrecommendation



router = APIRouter(prefix="/model")
router.include_router(jobrecommendation)