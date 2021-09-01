import time
from flask import Flask

app=Flask(__name__)

@app.route('/api/time')
@app.route('/')
def get_current():
  return {'time': time.time()}