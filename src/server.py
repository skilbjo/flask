#!/usr/bin/env python3

from flask import Flask, Blueprint, render_template, abort
from jinja2 import TemplateNotFound
# import api as api

app = Flask(__name__, template_folder='views')
# routes = Blueprint('skilbjo', __name__, template_folder='views/')
# app.register_blueprint(routes)

@app.route('/', methods=['GET'], defaults={'page': 'index'})

@app.route('/hello', methods=['GET'])
def hello(name=None):
  page = 'hello'
  return render_template('{page}.html'.format(page=page))

@app.route('/<page>', methods=['GET'])
def show(page):
  try:
    render_template('{page}.html'.format(page=page))
  except TemplateNotFound:
    abort(404)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# @app.route('/user/<user>', methods=['GET'])
# api.show_user_profile(user)

def main():
  app()

if __name__ == '__main__':
  main()
