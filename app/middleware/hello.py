from fastapi import Request
from fastapi.responses import JSONResponse
# Some test text
async def hello_middleware(request: Request, call_next):
    if request.url.path == "/hello":
        return await call_next(request)
    if not hasattr(request.state, "message_parts"):
        request.state.message_parts = []
    
    response = await call_next(request)
    
    full_message = " ".join(["Hello"] + request.state.message_parts)
    return JSONResponse(content={"message": full_message})
    # return response