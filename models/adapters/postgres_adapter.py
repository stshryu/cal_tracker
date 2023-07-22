from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import psycopg2

conn_url = 'postgresql+psycopg2://test_user:Testing123!@db:5432/test_db'

engine = create_engine(conn_url)

db = scoped_session(sessionmaker(bind=engine))
