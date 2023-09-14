from flask import Flask
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv
from pathlib import Path
import os
env_path = Path(__file__).resolve().parent.parent.parent / '.env'

load_dotenv(dotenv_path=env_path)

db = MongoEngine()
def create_app():
    app=Flask(__name__)
    
    app.config['MONGODB_SETTINGS'] = {
        'db': os.getenv("DB"),
        'host': os.getenv("HOST"),
        'port': int(os.getenv("PORT")),
    }
    
    db.init_app(app)

    from flaskmongo.userf.routes import userf
    app.register_blueprint(userf)
    return app