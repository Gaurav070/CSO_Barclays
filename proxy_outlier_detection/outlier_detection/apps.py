import os
from django.apps import AppConfig
from proxy_outlier_detection import settings 
import joblib

class OutlierDetectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'outlier_detection'
    model = None
    model_path = os.path.abspath(os.path.join(settings.CONFIG['model']['model_path']))
    print(model_path)
    #with open(model_path, "rb") as pkl_file:
    model = joblib.load(model_path)



