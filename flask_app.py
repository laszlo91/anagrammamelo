from flask import Flask, request, render_template
from anagram import anagram, openmorphit
import os

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './')

app = Flask(__name__, template_folder=template_path)


@app.route('/')
def my_form():
    return render_template('templates/form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    morphit = openmorphit()
    text = request.form['fname']
    listofanagrams = anagram(text, morphit)
    if len(listofanagrams) == 0:
        return "Ci spiace, nessun anagramma disponibile per questo nome. Puoi tornare a dedicarti alle cose importanti della tua giornata."
    else:
        return render_template("templates/anagrammi.html", data=listofanagrams)

#if __name__ == "__main__":
#    app.run(debug=True)
