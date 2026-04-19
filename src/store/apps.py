from django.apps import AppConfig
import os

class StoreConfig(AppConfig):
    name = 'store'
    def ready(self):
        if os.environ.get('RUN_MAIN'):
            # This will only execute in the main process
            pass