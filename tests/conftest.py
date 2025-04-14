import pytest
from app import create_app, db

class TestingConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

@pytest.fixture
def client():
    app = create_app(config_name="testing")
    app.config.from_object(TestingConfig)

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()
