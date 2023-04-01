# -*- coding: utf-8 -*-
from flask import Flask, render_template,send_file, redirect,url_for,request,flash,send_from_directory
from func.gen_bot import render_bot
import random, time, os
app = Flask(__name__)
app.secret_key='killmeatnight'
@app.route('/', methods=['POST', 'GET'])
@app.route('/bot_editor', methods=['POST', 'GET'])
def setup():
    ans = ''
    que = ''
    n = 0
    token = ""
    if request.method == 'POST': 
        token = request.form.get('token')
        name = time.time()
        name = str(name).replace('.','')
        args = {
        "token": token,
        "q": []
        } 
        args["n"] = n
        while que!=None and ans!=None:
            ansid = 'a' + str(n+1)
            queid = 'q' + str(n+1)
            ans = request.form.get(ansid)
            que = request.form.get(queid)
            print("ans1-  +" , ansid , "que1-  +", queid)
            if que!=None:
                args["q"].append([que, ans])
                n += 1
                print("ans-  +" , ans , "que-  +", que) 
        args["n"] = n
        
        print(args)
        nAme = render_bot(name,args)
        return redirect(url_for('download',filename=nAme))
    return render_template('/bot_editor.html')

@app.route('/download/<filename>', methods=['POST', 'GET'])
def download(filename):
    return send_from_directory('data/',filename, as_attachment=True)
    
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == "__main__":
    app.run( debug=False,host='0.0.0.0',port=80)