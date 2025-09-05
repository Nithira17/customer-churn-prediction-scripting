from typing import Dict, Any
from abc import ABC, abstractmethod
import joblib
import os
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

class BaseModelBuilder(ABC):
    def __init__(self, model_name:str, **kwargs):
        self.model_name = model_name
        self.model = None
        self.model_params = kwargs

    @abstractmethod
    def build_model(self):
        pass

    def save_model(self, filepath):
        if self.model is None:
            raise ValueError("No model to save. Build the model first")
        
        joblib.dump(self.model, filepath)

    def load_model(self, filepath):
        if os.path.exists(filepath):
            raise ValueError("Can't load. File not found")
        
        self.model = joblib.load(filepath)

class RandomForestModelBuilder(BaseModelBuilder):
    def __init__(self, **kwargs):
        default_params = {
                            'max_depth': 10,
                            'n_estimators': 100,
                            'min_samples_leaf': 1,
                            'random_state': 42
                        }
        default_params.update(kwargs)
        super().__init__('RandomForest', **default_params)

    def build_model(self):
        self.model = RandomForestClassifier(self.model_params)
        return self.model
    
class XGboostModelBuilder(BaseModelBuilder):
    def __init__(self, **kwargs):
        default_params = {
                            'max_depth': 10,
                            'n_estimators': 100,
                            'min_samples_leaf': 1,
                            'random_state': 42
                        }
        default_params.update(kwargs)
        super().__init__('XGboost', **default_params)

    def build_model(self):
        self.model = XGBClassifier(self.model_params)
        return self.model

# Testing    
# rf = RandomForestModelBuilder()
# rf_model = rf.build_model()
# print(rf_model)

# xgb = XGboostModelBuilder()
# xgb_model = xgb.build_model()
# print(xgb_model)