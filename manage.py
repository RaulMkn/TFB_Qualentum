import os

from app import create_app, db
from app.models import Data

env_name = os.getenv("FLASK_ENV", "development")
app = create_app(env_name)

with app.app_context():
    db.create_all()

    sample_data = Data(name="SQL Test User")
    db.session.add(sample_data)
    db.session.commit()

print("Database tables created.")
