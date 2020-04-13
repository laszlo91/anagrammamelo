from app import app
from app.anagram import anagram
from flask import request, render_template, Response
import random


@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = anagram(text)
    return ', '.join(processed_text)
