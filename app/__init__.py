from flask import Flask, request, render_template
import os


project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './')

app = Flask(__name__, template_folder=template_path)

from app import routes
