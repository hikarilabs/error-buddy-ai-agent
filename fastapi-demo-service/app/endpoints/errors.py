from fastapi import APIRouter


error_router = APIRouter()

def handle_error(error_type: str, message: str):
    """Handle different types of errors"""
    return {"error_type": error_type, "message": message}

@error_router.get("/warning-error")
async def test_error():
    """Test error endpoint"""
    return handle_error("test", "This is a test error")
