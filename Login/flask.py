from flask import Flask, request, render_template
app = Flask(__name__,static_folder='./static',template_folder='./templates')
@app.route('/Login', methods =["GET", "POST"])
def gfg():
  if request.method == "POST":
    a=request.form.get("fname")
    b= request.form.get("email")
    c=request.form.get("password")
    f=open("aaa.txt","a")
    x=b+"   "+c
    f.write(x)
    f.write("\n")
    f.close()
    return render_template("index.html")

if __name__=='main':
  app.run()

@app.route('/signup', methods =["GET", "POST"])
def gf():
  if request.method == "POST":
    a=request.form.get("login1")
    b= request.form.get("login2")
    f=open("aaa.txt","r")
    values=f.readlines()
    lol=''
    for i in values:
        lol=lol+i
    hmm=lol.split()
    for i in range(0,len(b),2):
        if hmm[i]==a and hmm[i+1]==b:
            return render_template("index.html")
        else:
            return render_template("login1.html")
if __name__=='main':
  app.run()