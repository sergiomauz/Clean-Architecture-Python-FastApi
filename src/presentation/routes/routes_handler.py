"""
    ToDo: DocString
"""

from fastapi import APIRouter
from presentation.routes.system_management import people


router = APIRouter()
router.include_router(people.router)
