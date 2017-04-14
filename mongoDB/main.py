from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'python-db'
app.config['MONGO_URI'] = 'mongodb://test:test@ds161400.mlab.com:61400/python-db'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def index():
  return 'Please run route /star or /star/Siris'

@app.route('/star', methods=['GET'])
def get_all_stars():
  star = mongo.db.stars
  output = []
  for s in star.find():
    output.append({'name' : s['name'], 'distance' : s['distance']})
  return jsonify({'result' : output})

@app.route('/star/<name>', methods=['GET'])
def get_one_star(name):
  star = mongo.db.stars
  s = star.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'distance' : s['distance']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/star', methods=['POST'])
def add_star():
  star = mongo.db.stars
  name = request.form.get('name')
  distance = request.form.get('distance')
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})




## readme
# For URL Query parameter, use request.args
#search = request.args.get("search")
#page = request.args.get("page")

# For Form input, use request.form
#email = request.form.get('email')
#password = request.form.get('password')

#For data type application/json, use request.data
# data in string format and you have to parse into dictionary
#data = request.data
#dataDict = json.loads(data)



if __name__ == '__main__':
    app.run(debug=True)
# app.run(host='0.0.0.0', debug=True)