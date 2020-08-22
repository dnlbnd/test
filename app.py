import os
import json
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/hello")
@cross_origin()
def helloWorld():
  return json.dumps({"message": "ANIL!!"})

@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8088)))