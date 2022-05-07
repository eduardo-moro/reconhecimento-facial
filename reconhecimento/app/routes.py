# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

import time

import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from mainModule import compareFaces
from mainModule import saveFile

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('about.html')


@app.route('/reconhecimento', methods=['GET', 'POST'])
def recognition():
    if request.method == 'POST':
        img1 = request.form.get('img1')
        img2 = request.form.get('img2')

        if img1 != '':
            path1 = saveFile('./temp/img1_' + str(time.time()) + '.jpeg', img1)

        if img2 != '':
            path2 = saveFile('./temp/img2_' + str(time.time()) + '.jpeg', img2)

        result = compareFaces(path1, path2)

        os.remove(path1)
        os.remove(path2)

        if float(result) > 0.72:
            message = "Biometria válida!"
        elif float(result) < 0:
            message = "Nenhum rosto identificado."
        else:
            message = "Biometria inválida."

        print('\nmensagem:   ' + message)
        print('resultado:  ' + str(result) + '\n')

        return jsonify(
            result=result,
            message=message,
        )

    else:
        return 'Nenhum parâmetro recebido.'


def strtr(string, replace):
    buf, i = [], 0
    if string is not None:
        while i < len(string):
            for s, r in replace.items():
                if string[i:len(s) + i] == s:
                    buf.append(r)
                    i += len(s)
                    break
            else:
                buf.append(string[i])
                i += 1
        return ''.join(buf)
    else:
        return False
