from flask import Flask, render_template, jsonify

app = Flask(__name__)

data = [{
            'number': 1,
            'name': 'Mahesh',
            'age': 25,
            'city': 'Bangalore',
            'country': 'India'
        },
        {
            'number': 2,
            'name': 'Alex',
            'age': 26,
            'city': 'London',
            'country': 'UK'
        },
        {
            'number': 3,
            'name': 'David',
            'age': 27,
            'city': 'San Francisco',
            'country': 'USA'
        },
        {
            'number': 4,
            'name': 'John',
            'age': 28,
            'city': 'Toronto',
            'country': 'Canada'
        },
        {
            'number': 5,
            'name': 'Chris',
            'age': 29,
            'city': 'Paris',
            'country': 'France'
        }]


@app.route('/')
def home():
    return render_template("index.html", lista=data)


@app.route('/dados')
def dados():
    return jsonify(data)
