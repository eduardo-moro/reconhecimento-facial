# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from recognition import compareFaces
from recognition import saveFile
from urllib.parse import unquote
import time
import logging
import os

app = Flask(__name__)



@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('about.html')

@app.route('/reconhecimento', methods=['GET', 'POST'])
def recognition():
    if request.method == 'POST':
        img1 = request.form.get('img1')
        img2 = request.form.get('img2')

        print(img1)
        print(img2)

        if(img1 != ''):
            path1 = saveFile('./temp/img1_'+ str(time.time()) + '.jpeg', img1)

        if(img2 != ''):
            path2 = saveFile('./temp/img2_'+ str(time.time()) + '.jpeg', img2)

        result = compareFaces(path1, path2)

        os.remove(path1)
        os.remove(path2)

        if(float(result) > 0.72):
            message = "Biometria válida!"
        elif (float(result) < 0):
            message = "Nenhum rosto identificado."
        else:
            message = "Biometria inválida."


        return jsonify(
            result = result,
            message = message,
        )

    else:
        return 'Nenhum parâmetro recebido.'

def strtr(strng, replace):
    buf, i = [], 0
    if strng is not None:
        while i < len(strng):
            for s, r in replace.items():
                if strng[i:len(s)+i] == s:
                    buf.append(r)
                    i += len(s)
                    break
            else:
                buf.append(strng[i])
                i += 1
        return ''.join(buf)
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


