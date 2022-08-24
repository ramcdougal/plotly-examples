from flask import Flask

my_template = """
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<div id="myGraph"></div>
<script>
(
    fetch("/api/data")
    .then(response => response.json())
    .then(function (data) {Plotly.newPlot("myGraph", data)})
)
</script>
"""

app = Flask(__name__)


@app.route("/api/data")
def data():
    return [{"x": [1, 2, 3, 4, 5], "y": [1, 4, 9, 16, 25], "type": "scatter"}]


@app.route("/")
def index():
    return my_template


if __name__ == "__main__":
    app.run(debug=True)
