import importlib
import os
import uvicorn
from fastapi import FastAPI

from config import FastAPIConfig
from database import Base, engine
from schedular import register_jobs

app = FastAPI(
    title='EnderFastAPIBase',
    version='Developing'
)

module_dir = os.path.join(os.path.dirname(__file__), 'modules')

for module_name in os.listdir(module_dir):
    module_path = os.path.join(module_dir, module_name)
    if os.path.isdir(module_path) and not module_name.startswith('__'):
        try:
            module = importlib.import_module(f"modules.{module_name}.routes")
            app.include_router(module.router)
        except ImportError as e:
            print(f"Could not import {module_name}: {e}")

Base.metadata.create_all(bind=engine)

register_jobs()

if __name__ == '__main__':
    uvicorn.run(app, host=FastAPIConfig.HOST, port=FastAPIConfig.PORT)
