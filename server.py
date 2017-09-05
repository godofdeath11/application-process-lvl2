from flask import Flask, render_template, redirect, request, session
import queries
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/mentors")
def mentors_with_schools():
    query_result = queries.mentors_with_schools()
    titlelist = ("first_name", "last_name", "country", "name")
    return render_template("/list.html", titlelist=titlelist, query=query_result)


@app.route("/all-school")
def mentors_with_allschools():
    query_result = queries.mentors_with_allschool()
    titlelist = ("first_name", "last_name", "country", "name")
    print(query_result)
    return render_template("/list.html", titlelist=titlelist, query=query_result)


@app.route("/mentors-by-country")
def count_mentors_by_schools():
    query_result = queries.count_mentors_by_schools()
    titlelist = ("country", "count")
    return render_template("/list.html", titlelist=titlelist, query=query_result)


if __name__ == "__main__":
    app.secret_key = "youshouldntseethis"
    app.run(
        debug=True,
        port=5000
    )
