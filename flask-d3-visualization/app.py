from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage with buttons
@app.route('/')
def index():
    return render_template('index.html')

# Route for D3 and C3 Graph
@app.route('/d3-graph')
def d3_graph():
    return render_template('d3_graph.html')

@app.route('/c3-graph')
def c3_graph():
    return render_template('c3_graph.html')

if __name__ == '__main__':
    app.run(debug=True)
