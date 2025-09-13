"""
API Router which combines all the endpoints of the application
"""
from fastapi import APIRouter
from app.endpoints.errors import error_router