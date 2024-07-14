from sqlalchemy import engine_from_config, text
from sqlalchemy.orm import sessionmaker
from config import config, postgres_conf

# MySQL
# engine = engine_from_config(config, echo=False)

# PostgreSQL
engine = engine_from_config(postgres_conf, prefix='sqlalchemy.')

Session = sessionmaker(bind=engine)
session = Session()

session.execute(text("SELECT 1;"))