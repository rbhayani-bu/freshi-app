SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost:5432/freshi"
if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
SECRET_KEY='dev'