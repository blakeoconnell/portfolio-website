from flask import Flask, render_template, send_from_directory
import data
from project import Project

app = Flask(__name__)

projects = []

for item in data.project_data:
    new_project = Project(
        item["id"],
        item["title"],
        item["short_desc"],
        item["long_desc"],
        item["imgURL"],
        item["carouselImages"],
        item["githubURL"],
        item["technologies"],
        item["learnings"]
    )
    projects.append(new_project)


@app.route("/")
def home():
    return render_template('index.html', projects=projects)


@app.route("/projects/<int:id>")
def get_project(id):
    for project in projects:
        if project.id == id:
            return render_template('project.html', project=project)
    return render_template('project.html', project=None)


@app.route("/download")
def download_resume():
    return send_from_directory('static', 'assets/BlakeOConnellResume2021.pdf')


if __name__ == '__main__':
    app.run()
