from flask import Flask, redirect, render_template, url_for, request, jsonify
import folium, plotly 

app = Flask(__name__)

def calculer_pourcentage(lat, lng):
    return 1.6*lat


@app.route('/calculer_pourcentage', methods=['POST'])
def get_pourcentage():
    data = request.json
    lat = data['lat']
    lng = data['lng']
    pourcentage = calculer_pourcentage(lat, lng)
    return jsonify({"pourcentage": pourcentage})


@app.route('/simple-map')
def simple_map():
    return render_template('simple_map.html')

@app.route('/')
def home():
    return redirect(url_for('simple_map'))

if __name__ == '__main__':
    app.run(debug=True)