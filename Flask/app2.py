from flask import Flask, redirect, render_template, url_for
import folium, plotly 

app = Flask(__name__)

@app.route('/simple-map')
def simple_map():
    return render_template('simple_map.html')

@app.route('/')
def home():
    return redirect(url_for('simple_map'))

if __name__ == '__main__':
    app.run(debug=True)