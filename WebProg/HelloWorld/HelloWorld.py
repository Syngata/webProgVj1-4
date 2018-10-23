'''
Created on 23. lis 2018.

@author: Ink
'''

from flask import Flask
import random

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
        return "{:0,.2f} {} je {:0,.2f} {}".format(float(iznos),v1, float(rezVal),v2)
    
    elif v1=="eur" and v2=="hrk":
        rezVal=float(iznos)*hrkEuTec
        return "{:0,.2f} {} je {:0,.2f} {}".format(float(iznos),v1, float(rezVal),v2)
    
    elif v1==v2:
        return "{:0,.2f} {} je {:0,.2f} {}".format(float(iznos),v1, float(iznos),v2)
   
    elif v1=="hrk" and v2=="usd":
        rezVal=float(iznos)/hrkUsTec
        return "{:0,.2f} {} je {:0,.2f} {}".format(float(iznos),v1, float(rezVal),v2)
    
    elif v1=="usd" and v2=="hrk":
        rezVal=float(iznos)*hrkUsTec
        return "{:0,.2f} {} je {:0,.2f} {}".format(float(iznos),v1, float(rezVal),v2)
   
    elif v1=="eur" and v2=="usd":
        rezVal=(float(iznos)*hrkEuTec)/hrkUsTec
        return "{:0,.2f} {} je {:0,.2f} {}".format(float(iznos),v1, float(rezVal),v2)
    
    elif v1=="usd" and v2=="eur":
        rezVal=(float(iznos)*hrkUsTec)/hrkEuTec
        return "{:0,.2f} {} je {:0,.2f} {}".format(float(iznos),v1, float(rezVal),v2)
      
    
   
    else:
        return "Nema te valute"
    
   
    
@app.route("/random/<r1>/<r2>")
def rndNum(r1,r2):
    return "Odabrao sam {} kao slučajan broj između {} i {}".format(random.randint(int(r1),int(r2)),int(r1),int(r2))

@app.route("/kalkulator/<o>/<b1>/<b2>")
def calc(o,b1,b2):
    rez=0.0
    
    if o=="zbroji":
        rez=float(b1)+float(b2)
        return "Zbroj {} i {} je: {}".format(float(b1),float(b2), rez)
    
    elif o=="oduzmi":
        rez=float(b1)-float(b2)
        return "Razlika {} i {} je: {}".format(float(b1),float(b2), rez)
    
    elif o=="pomnozi":
        rez=float(b1)*float(b2)
        return "Umnožak {} i {} je: {}".format(float(b1),float(b2), rez)
    elif o=="podijeli":
        rez=float(b1)/float(b2)
        return "Količnik {} i {} je: {}".format(float(b1),float(b2), rez)
        
        
    