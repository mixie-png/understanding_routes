from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

#### Assignment: Understanding Routing ####
# 1. localhost:5000/ - have it say "Hello World!"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# 2. localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return 'Dojo!'

# 3. Create one url pattern and function that can handle the following examples: localhost:5000/say/flask - have it say "Hi Flask!"
@app.route('/say/<string:word>')
def say(word):
    return f"Hi {word}!"

# 4. Create one url pattern and function that can handle the following examples (HINT: path variables are by default passed as strings. How might you handle a number?): localhost:5000/repeat/35/hello - have it say "hello" 35 times
@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return f"{word * num}"

# SENSEI BONUS
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404


# Bonus to number 3
@app.route('/say/<word>/<int:num>')
def sayAgain(word, num):
    return f"Hi {word * num}"











if __name__=="__main__":
    app.run(debug=True)