import os

from sqlalchemy import create_engine, text

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

#query the Cloud-hosted MySQL Database for a specific job
def get_job_from_db(id):
  values = {'val' : id}
  with engine.connect() as conn:
    result= conn.execute(text('SELECT * from jobs where id = :val'),values)
    rows =result.all()
    if(len(rows) == 0):
      return None
    else:
      return rows[0]._asdict()

#add job application obtained from form to SQL Database
def add_application_to_db(job_id, application):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name,:email, :linkedin_url, :education, :work_experience, :resume_url)")
    conn.execute(statement = query, 
                parameters = dict(job_id = job_id,
                full_name = application['full_name'],
                email = application['email'],
                linkedin_url = application['linkedin_url'],
                education = application['education'],
                work_experience = application['work_experience'],
                resume_url = application['resume_url']))
    
    
  

  
  
                       