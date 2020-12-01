from flask import Flask #We imported the Flask class. Import Flask to allow us to create our app
app = Flask(__name__) #We made an instance of the Flask class called "app" Create a new instance of the Flask class called "app"

@app.route('/') # The "@" decorator associates this route with the function immediately following
def hello_world():
  return 'Hello World hi' # Return the string 'Hello World!' as a response
# if the client requests localhost:5000/, the hello_world function will run

@app.route('/success')
def success():
  return "success!"

# VARIABLE NAMES
@app.route("/hello/<name>")# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
  print(name)
  return f"Hello, {name}"

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
  print('username ->', username)
  print('id       ->', id)
  return "username: " + username + ", id:" + id


if __name__=="__main__": # Ensure this file is being run directly and not from a different module    
  app.run(debug=True) # Run the app in debug mode.