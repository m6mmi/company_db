from sqlalchemy import engine_from_config, text
from sqlalchemy.orm import sessionmaker
from config import config

engine = engine_from_config(config, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

session.execute(text("SELECT 1;"))