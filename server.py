from flask import Flask
import random
app = Flask(__name__)

rand_number = random.randint(0, 9) # generates a random number between 0 and 9


@app.route('/')
def home_route():
    return '<h1> Guess a number between 0 and 9 </h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def random_route(number):
    if number < rand_number:
        return '<h1 style="color:red"> The number you guessed is too low, try again ! <h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif number > rand_number:
        return '<h1 style="color:purple"> The number you guessed is too high, try again ! <h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1 style="color:green"> The number you guessed is the correct one ! <h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
