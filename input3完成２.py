#!/usr/bin/env python
# coding: utf-8
from flask import Flask, render_template, request
import datetime
import sqlite3,linecache
import numpy as np
import matplotlib.pyplot as plt
app = Flask(__name__)

@app.route('/')#('/input')
def input():
    time = datetime.date.today()
    return render_template('output3.html',time=time)

@app.route('/output', methods = ['POST', 'GET'])
def output():
    if request.method == 'POST':
        time = datetime.datetime.today()
        #ブラウザから金額取得
        num1 = request.form.getlist("num1")
        num2 = request.form.getlist("num2")
        
        #list変換
        numlist1 = [int(s) for s in num1]
        numlist2 = [int(s) for s in num2]
        #計算
        ansr =numlist1[0]-numlist2[0]
        
        #ファイル書き込む       
        f = open('text.txt', 'w') # 書き込みモードで開く
        f.write(str(numlist1[0])+'\n') # 引数の文字列をファイルに書き込む
        f.write(str(numlist2[0])+'\n')
        f.write(str(ansr )+'\n')
        #ファイルから読み込み

        with open('text.txt', "r") as f:
            
            data = [v.rstrip() for v in f.readlines()]
        
        f.close() # ファイルを閉じる
           
        sendnum3=int(data[2])


        ans = request.form


        #ブラウザに送信し表示
        return render_template("output3.html",time=time,ans=ans,sendnum3=sendnum3)


  
if __name__ == "__main__":
    
    app.run(host='0.0.0.0', debug=True)
