from flask import Flask, render_template, jsonify
from database import get_jobs_from_db, get_job_from_db

app = Flask(__name__)

#route to this function when nothing succeeds the "/" in the url
@app.route('/')
def hello_careers():
  
  #Get the Jobs from the MySQL database hosted in the cloud
  jobs = get_jobs_from_db()
  #Render the home.html page
  return render_template('home.html', jobs = jobs)


#route to this function when "/api/jobs" is in the url
@app.route('/api/jobs')
def list_jobs():
  
  #Get the Jobs from the MySQL database hosted in the cloud
  jobs = get_jobs_from_db()
  #return a JSON with the jobs list
  return jsonify(jobs)

@app.route('/api/job/<id>')
def show_job(id):
  job = get_job_from_db(id)
  return jsonify(job)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81, debug = True)


