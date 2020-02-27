from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from urllib.parse import unquote

def predict(x, y, find):
    x = np.array(x).reshape((-1, 1))
    print(x)
    y = np.array(y)

    clf = LinearRegression()

    clf.fit(x, y)

    inp = np.array([[int(find)]])
    inp = inp.reshape(1, -1)
    final = clf.predict(inp)
    # print the output.
    print('The precipitation in inches for the input is:', final)
    return final

@app.route("/get")
def get_bot_response():
    x = request.args.get('x')
    print(x)
    xint = unquote(x)
    x = [float(x) for x in xint.split(',')]
    y = request.args.get('y')
    yint = unquote(y)
    y = [float(x) for x in yint.split(',')]
    find = request.args.get('find')
    find = unquote(find)
    return str(predict(x, y, find))

if __name__ == "__main__":
    app.run()