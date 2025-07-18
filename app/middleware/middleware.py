from fastapi import Request
from fastapi.responses import JSONResponse

async def middleware_middleware(request: Request, call_next):
    if not hasattr(request.state, "message_parts"):
        request.state.message_parts = []
    
    response = await call_next(request)
    
    request.state.message_parts.append("Middleware,")
    return response