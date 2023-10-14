from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id' : '1',
    'title' : 'Data Scientist',
    'location' : 'Bengaluru, India',
    'salary' : 'Rs. 16,00,000'
  },
  {
    'id' : '2',
    'title' : 'Data Analyst',
    'location' : 'Bengaluru, India',
    'salary' : 'Rs. 10,00,000'
  },
  {
    'id' : '3',
    'title' : 'Software Engineer - I',
    'location' : 'Hyderabad, India',
    'salary' : 'Rs. 20,00,000'
  },
  {
    'id' : '4',
    'title' : 'Front-End Developer',
    'location' : 'San Francisco, US',
    'salary' : '$ 120,000'
  },
  
]


@app.route('/')
def hello_careers():
    return render_template('home.html', jobs = JOBS)
  
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81, debug = True)


