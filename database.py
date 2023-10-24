from typing_extensions import clear_overloads
import sqlalchemy
from sqlalchemy import create_engine, text
import os

#Get the Database string, username, hostname and password from the environment variables/secrets
db_conn_string = os.environ['DB_CONNECTION_STRING']

#create a connection, passing arguments with SSL certification for a secure connection

engine = create_engine(db_conn_string, pool_pre_ping=True, connect_args= {"ssl":{"ssl_ca":"etc/ssl/cert.pem"}})

def get_jobs_from_db():

  with engine.connect() as conn:
    jobs = []
    #query the Cloud-hosted MySQL Database for the jobs
    result = conn.execute(text('SELECT * FROM jobs'))
    for row in result.all():
# Get the row, change it to dict by invoking _asdict(), add to list of jobs
      jobs.append(row._asdict())
    return jobs

  
  
                       