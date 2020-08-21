import os
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({"message": "Hello there you go man!"})

@app.route('/hello')
def index2():
    return json.dumps({"message": "Pani chestundi ani cheppa ga...nammava. Dobbey."})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))