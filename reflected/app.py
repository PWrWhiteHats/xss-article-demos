#!/usr/bin/env python

import re
from flask import Flask, render_template, request

app = Flask(__name__)

# Emulate the database of words
memory = [
    'white',
    'hats',
    'whitehats',
    'wust',
    'ctf'
]

@app.route('/')
def main():
    if request.args.get('q'):
        q = request.args.get('q')
        r = re.compile(f".*{q}.*")
        findings = list(filter(r.match, memory))
        return render_template('index.html', q=q, findings=findings)
    return render_template('index.html')

app.run(debug=True)