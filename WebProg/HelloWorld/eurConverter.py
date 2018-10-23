'''
Created on 23. lis 2018.

@author: Ink
'''

from flask import Flask

app= Flask(__name__)
@app.route("/")

def index():
    return "<h1>Hello world</h1>"


@app.route("/eurhrk/<value>")

def eurhrk(value):
    hrk = float(value) *7.42
    return "{:0,.2f} eura je {:0,.2f} kuna".format(float(value), hrk)

@app.route("/valuta/<v1>/<v2>/<iznos>")
def valConv(v1,v2,iznos):
    hrkEuTec=7.42
    hrkUsTec=6.52
    
    rezVal=0.0
    
    if v1=="hrk" and v2=="eur":
        rezVal=float(iznos)/hrkEuTec
        return "{:0,.2f} kuna je {:0,.2f} eura".format(float(iznos), float(rezVal))
    else:
        return "Nema te valute"