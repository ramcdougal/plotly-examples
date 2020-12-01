from flask import Flask, render_template_string

my_template = """
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<div id="myGraph"></div>
<script>
    Plotly.newPlot("myGraph", {{data|tojson}}, {"title": "{{state}}"})
</script>
"""

app = Flask(__name__)


@app.route("/")
def index():
    return render_template_string(
        my_template,
        state="Connecticut",
        data=[
            {
                "values": [12.7, 87.3],
                "labels": ["smokers", "non-smokers"],
                "type": "pie",
            }
        ],
    )


if __name__ == "__main__":
    app.run(debug=True)
