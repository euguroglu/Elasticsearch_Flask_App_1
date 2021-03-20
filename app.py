from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

@app.route('/',methods=["GET","POST"])
def index():

    #q = request.args.get("q") # For get method
    q = request.form.get("q")
    if q is not None:

        res = es.search(index="access-logs-2020-02", body={"query": {"prefix" : {"client.geo.city_name":q}}})
        return render_template("index.html", q=q, res=res)


    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
