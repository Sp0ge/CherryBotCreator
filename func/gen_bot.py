# -*- coding: utf-8 -*-
from jinja2 import Template
import os, zipfile, time
from flask import send_file, redirect, send_from_directory

def render_bot(name,args):
    f1 = open('shablons/template_main.py', "r", encoding='utf8')
    folder = 'data/' + name
    s1 = f1.read()

    f1.close()

    template = Template(s1)

    if not os.path.isdir(folder):
        os.mkdir(folder)

    file_name = 'data/' + name+"/main.py" 
    f2 = open(file_name, "w", encoding='utf8')

    f2.write(template.render(token=args["token"]))

    f2.close()

    f3 = open('data/' + name +"/funcs.py", "w", encoding='utf8')
    
    f3.write('"# -*- coding: utf-8 -*-" \n')
    f3.write("def work(text): \n")
    for i in range(args["n"]):
        f3.write("\n    if text =='"+str(args["q"][i][0])+"':\n        return '"+args["q"][i][1]+"'")
    f3.close()

    
    file_dir = os.listdir(folder)
    nAme = 'data/' + name + '.zip'
    with zipfile.ZipFile(nAme, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(folder+"/"+file)
            zf.write(add_file)
    nAme = name + ".zip"

    return (nAme)
