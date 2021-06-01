#!/usr/bin/env python

from flask import Flask, render_template, request

app = Flask(__name__)

# Emulate the database of notes
memory = [
    {
        'id': 1,
        'note': 'First note'
    },
    {
        'id': 2,
        'note': 'Second note'
    }
]

@app.route('/', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        memory.append(
            {
                'id': len(memory)+1,
                'note': request.form.get('note')
            }
        )
    return render_template('index.html', memory=memory)

app.run(debug=True)