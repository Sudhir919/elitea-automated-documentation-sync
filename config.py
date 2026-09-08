import os


class Config:
    APP_NAME = os.getenv("APP_NAME", "EliteA Documentation Sync")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
