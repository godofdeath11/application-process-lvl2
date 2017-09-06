from flask import Flask, render_template, redirect, request, session
import queries
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/mentors")
def mentors_with_schools():
    query_result = queries.mentors_with_schools()
    column_list = ("first_name", "last_name", "country", "name")
    title_list = ("First name", "Last name", "Country", "School")
    return render_template("/list.html", column_list=column_list, query=query_result, title_list=title_list)


@app.route("/all-school")
def mentors_with_allschools():
    query_result = queries.mentors_with_allschool()
    column_list = ("first_name", "last_name", "country", "name")
    title_list = ("First name", "Last name", "Country", "School")
    print(query_result)
    return render_template("/list.html", column_list=column_list, query=query_result, title_list=title_list)


@app.route("/mentors-by-country")
def count_mentors_by_schools():
    query_result = queries.count_mentors_by_schools()
    column_list = ("country", "count")
    title_list = ("Country", "Sum")
    return render_template("/list.html", column_list=column_list, query=query_result, title_list=title_list)


@app.route("/contacts")
def schools_with_mentors():
    query_result = queries.schools_with_mentors()
    column_list = ("name", "first_name", "last_name")
    title_list = ("School", "First name", "Last name")
    return render_template("/list.html", column_list=column_list, query=query_result, title_list=title_list)


@app.route("/applicants")
def applicants_with_date():
    query_result = queries.applicants_with_date()
    column_list = ("first_name", "application_code", "creation_date")
    title_list = ("First name", "Application code", "Creation date")
    return render_template("list.html", column_list=column_list, query=query_result, title_list=title_list)


@app.route("/applicants-and-mentors")
def applicants_with_mentors():
    query_result = queries.applicants_with_mentor()
    column_list = ("applicant_first_name", "application_code", "first_name", "last_name")
    title_list = ("applicant's First name", "Application code", "First name", "Last name")
    return render_template("list.html", column_list=column_list, query=query_result, title_list=title_list)


if __name__ == "__main__":
    app.secret_key = "youshouldntseethis"
    app.run(
        debug=True,
        port=5000
    )
