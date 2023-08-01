from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import success
from errors import errors

def create_connection():
    conn_url = 'postgresql+psycopg2://test_user:Testing123!@db:5432/test_db'
    engine = create_engine(conn_url)
    return sessionmaker(engine)

def save(save_object):
    Session = create_connection()
    with Session.begin() as session:
        try:
            session.add(save_object)
        except:
            session.rollback()
            return errors.UnexpectedError("Error committing data")
        else:
            session.flush()
            return_id = save_object.id
            session.commit()
            return success.Success(return_id)
