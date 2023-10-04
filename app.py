from flask import Flask, render_template, request

import networkx as nx

import cities as G


app = Flask(__name__)

Graph = G.buildGraph()

@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/result", methods=["POST"])
def distance():
    source = request.form['source']
    target = request.form['target']

    road_to = nx.dijkstra_path(Graph, source, target)

    
    path_length = round(nx.dijkstra_path_length(Graph, source, target), 2)
  

    return render_template("result.html", data =[source, target, road_to, path_length])



if __name__ == "__main__":
    app.run(debug=True)
