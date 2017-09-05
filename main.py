from flask import Flask, render_template, redirect, request, session
import queries


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showall")
def showall():
    query_result = queries.showall()
    return render_template("/showall", results=query_result)

if __name__ == "__main__":
    app.secret_key = "youshouldntseethis"
    app.run(
        debug=True,
        port=5000
    )
