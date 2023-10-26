from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/')
def get_main_page():
    if request.method == 'GET':
        return render_template('mainPage.html')


@app.route('/mobile')
def get_main_page_mobile():
    if request.method == 'GET':
        return render_template('mainPage.html')


@app.route('/projects')
def get_projects_page():
    if request.method == 'GET':
        response = requests.get("https://api.github.com/users/awawakum/repos")
        response_dict = response.json()
        projects = []
        for proj in response_dict:
            print(proj)
            projects.append((proj['name'], proj['description'], proj['html_url'], proj['language']))
        return render_template('projects.html', projects=projects)


@app.route('/contacts')
def get_contacts_page():
    if request.method == 'GET':
        return render_template('contacts.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
