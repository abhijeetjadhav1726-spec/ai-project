from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/simulation')
def simulation():
    return render_template('simulation.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/traffic-data')
def traffic_data():
    # Simulated traffic counts for 4 lanes
    data = {
        "north_south": random.randint(0, 20),
        "east_west": random.randint(0, 20)
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
