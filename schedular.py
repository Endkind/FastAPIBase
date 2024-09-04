import os
import importlib
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.start()

def register_jobs():
    module_dir = os.path.join(os.path.dirname(__file__), 'modules')

    for module_name in os.listdir(module_dir):
        module_path = os.path.join(module_dir, module_name)
        if os.path.isdir(module_path) and not module_name.startswith('__'):
            jobs_file = os.path.join(module_path, 'jobs.py')
            if os.path.exists(jobs_file):
                try:
                    module = importlib.import_module(f"modules.{module_name}.jobs")
                    if hasattr(module, "register_jobs"):
                        module.register_jobs(scheduler)
                except ImportError as e:
                    print(f"Could not import {module_name}: {e}")
