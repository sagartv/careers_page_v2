from typing_extensions import clear_overloads
import sqlalchemy
from sqlalchemy import create_engine, text
import os

db_conn_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_conn_string, pool_pre_ping=True, connect_args= {"ssl":{"ssl_ca":"etc/ssl/cert.pem"}})

def get_jobs_from_db():

  with engine.connect() as conn:
    jobs = []
    result = conn.execute(text('SELECT * FROM jobs'))
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

  
  
                       