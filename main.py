from fastapi import *
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from endpoints import router as api_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

app.include_router(api_router, prefix='/api')

@app.get('/')
def read_root():
    return{'Status': 'Active'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)