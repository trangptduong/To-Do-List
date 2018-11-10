from flask import Flask, jsonify, request, abort, render_template

import json



APP = Flask('To Do List')

token = None



def check_credentials():

  return session['logged_in']



Todo = []

"""super_secure_username = 'username_'

super_secure_password = 'password_'"""





@APP.route('/')

def index():

  return render_template('cs1122p1.html')



@APP.route('/Todo/create', methods=['POST'])

def createTodo():

  if(request.headers.get('token') != token or token is none):

    return abort(403)

  todo.extend(request.get_json().get('todo'))

  return jsonify(Todo)



@APP.route('/Todo/read', methods=['GET'])

def readTodo():

  print(token)

  if(request.headers.get('token') != token or token is none):

    return abort(403)

  return jsonify(Todo)

  



@APP.route('/Todo/update', methods=['POST'])

def updateTodo():

  if(request.headers.get('token') != token or token is none):

    return abort(403)

  old_Todo = Todo

  Todo = request.get_json().get('Todo')

  for item in old_Todo:

    if item not in Todo:

      return item

  return jsonify(Todo)



@APP.route('/Todo/delete', methods=['GET'])

def deleteTodo():

  if(request.headers.get('token') != token or token is none):

    return abort(403)

  item = request.get_json().get('Todo')

  global Todo

  Todo = list(filter(lambda x: x not in item, Todo))

  return jsonify(Todo)



@APP.route('/Todo/login', methods=['POST'])

def login():

    username = request.get_json().get("username")

    password = request.get_json().get("password")

    if username == super_secure_username and password == super_secure_password:

      global token

      token = uuid4().hex

      return token





if __name__=='__main__':

  APP.run()
