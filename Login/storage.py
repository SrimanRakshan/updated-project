'''
from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/', methods =["GET", "POST"])
def gfg():
	if request.method == "POST":
	    user_id = request.form.get("login1")
	    Enter_password = request.form.get("login2")
        return "hi"
	return render_template("login1.html")
if __name__=='__main__':
    app.run() 
    '''
    from flask import Flask , render_template ,flash , redirect,url_for,request,Response
import json , requests , mysql.connector ,smtplib,random,base64,io,ast
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
app = Flask(__name__)

password_of_db="Saraswathi"

def cities_know(x):
    mydb_11 = mysql.connector.connect(
                      host="localhost",
                      user="root",
                      password=password_of_db,
                      database="wphdb"
                    )
    z = f"select username from wph_table"
    z = f"select places from wph_table where username='{x}'"
    mycursor = mydb_11.cursor()
    mycursor.execute(z)
    result_2 = mycursor.fetchall()
    x=result_2[0][0]
    res = ast.literal_eval(x)
    cities = res[0]
    return(cities)

def does_cities_exist(city,country):
api_key = "0c42f7f6b53b244c78a418f4f181282a"
weather_url = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')
try:
weather_data = weather_url.json()
temp_dummy = weather_data['main']['temp']
print('The printing of cities exist')
return('Exist')
except:
return('Not existing')

def countries_know(x):
    mydb_11 = mysql.connector.connect(
                      host="localhost",
                      user="root",
                      password=password_of_db,
                      database="wphdb"
                    )
    z = f"select username from wph_table"
    z = f"select places from wph_table where username='{x}'"
    mycursor = mydb_11.cursor()
    mycursor.execute(z)
    result_2 = mycursor.fetchall()
    x=result_2[0][0]
    res = ast.literal_eval(x)
    countries = res[1]
    return(countries)



def email_otp(x,y):
global otp
otp = ''
for i in range(4):
otp+=str(random.randint(1,9))

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("harshaachu29@gmail.com", "dykpcpwaasasuhzq")
message = f"Hello {x} of best weather forecasting website the Harsha weather forecasting user . \n Your one time password for entering into the website is {otp} ,\n cheers"
s.sendmail("harshaachu29@gmail.com",y, message)
s.quit()


def existing_user(username):
b = []
mydb_10 = mysql.connector.connect(
 host="localhost",
 user="root",
 password=password_of_db,
 database="wphdb"
)
z = f"select username from wph_table"
mycursor = mydb_10.cursor()
mycursor.execute(z)
resulter = mycursor.fetchall()
print(resulter)
uname = (username,)
print(uname)
if uname not in resulter:
return "Unique"

def graph_teller():
global temper
temper = []
for k in range(0,len(cities)):
city = cities[k]
country = countries[k]
api_key = "0c42f7f6b53b244c78a418f4f181282a"
weather_url = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')
weather_data = weather_url.json()
temp = weather_data['main']['temp']
temper.append(temp)

return temper

@app.route("/")
def home():
return render_template('home.html')

@app.route("/result",methods=['GET','POST'])
def result():
if request.method=='POST':
return redirect(url_for('dashboard'))

return render_template("result.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city)


cities=[]
countries=[]
tempertaures = []
humidities = []
windspeeds = []
error = ''

@app.route("/dashboard",methods=['GET','POST'])
def dashboard():
global temp , humidity , wind_speed , city , error
tempertaures=[]
humidities=[]
windspeeds=[]
if request.method=='GET':
try:
 if error=='The name of the city or the country entered is wrong . Please check the spelling again ':
   print('yes')
except:
 error = None
print(cities , countries)
for k in range(len(cities)):
print(k)
city = cities[k]
country = countries[k]
api_key = "0c42f7f6b53b244c78a418f4f181282a"
weather_url = requests.get(
           f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')
weather_data = weather_url.json()
temp = weather_data['main']['temp']
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']
print(temp,humidity,wind_speed)
temp_mod = round((int(temp) - 32) / 1.8)
tempertaures.append(temp_mod)
humidities.append(humidity)
windspeeds.append(wind_speed)
length = len(cities)
return render_template("dashboard.html",tempertaures=tempertaures,humidities=humidities,cities=cities,windspeeds=windspeeds,length=length,name=x,error=error)


if request.method == "POST":
city = request.form['city']
country = request.form['country']
does_cities_exist(city,country)
if does_cities_exist(city,country)=='Exist':
error = None
print('the post print is happening')
mydb_2 = mysql.connector.connect(
 host="localhost",
 user="root",
 password=password_of_db,
 database="wphdb"
)
print(x)
z = f"select places from wph_table where username='{x}'"
mycursor = mydb_2.cursor()
mycursor.execute(z)
result_2 = mycursor.fetchall()
cities.append(city)
countries.append(country)
xx = "'"+x+"'"
api_key = "0c42f7f6b53b244c78a418f4f181282a"
weather_url = requests.get(
           f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')
weather_data = weather_url.json()
temp = round(weather_data['main']['temp'])
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']
z = f'update wph_table set places="[{cities},{countries}]" where username={xx};'
mycursor = mydb_2.cursor()
mycursor.execute(z)
mydb_2.commit()
return redirect(url_for("result"))
else:
error = 'The name of the city or the country entered is wrong . Please check the spelling again '
print(error)
print('this is inside post , now redirecting to get')
return redirect(url_for("dashboard"))


@app.route("/return_graph",methods=['GET','POST'])
def return_graph():
  fig = Figure()
  axis = fig.add_subplot(1, 1, 1)
  xs = np.random.rand(100)
  ys = np.random.rand(100)
  templist = graph_teller()
  print(templist)
  print(f'the current cities are {cities}')
  print(f'the current tempertaures are {tempertaures}')
  axis.scatter(cities, templist)
  output = io.BytesIO()
  FigureCanvas(fig).print_png(output)
  return Response(output.getvalue(), mimetype='image/png')


@app.route("/weather_graph",methods=['GET','POST'])
def weather_graph():
if request.method=='POST':
pass
if request.method=="GET":
return render_template('weather_graph.html')

@app.route("/otpverification",methods=['GET', 'POST'])
def otpverification():
error=None
if request.method=='POST':
s = (request.form['otp'])
if s==otp:
return redirect(url_for('dashboard'))
else:
error='You have entered the wrong otp . Please try again.'
return render_template('otpverification.html',error=error)


@app.route("/register",methods=['GET','POST'])
def register():
error = None
if request.method=='POST':
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password=password_of_db,
 database="wphdb"
)

global x , y , z

x = (request.form['username'])
y = (request.form['password'])
a = (request.form['cpassword'])
z = (request.form['email'])
if y==a:

if existing_user(x) == "Unique":
try:
email_otp(x,z)
f = f"insert into wph_table values('{x}','{y}','{z}','NULL')"

mycursor = mydb.cursor()
mycursor.execute(f)
mydb.commit()

return redirect(url_for(('otpverification')))

except:
error='The email does not exist . Please enter a valid email id.'


else:
error = "The username is already taken please try a new one"

else:
error='Password and confirm password do not match'

return render_template('register.html',error=error)






@app.route("/source")
def source():
return render_template('source.html')


@app.route("/login",methods=['GET','POST'])
def login():
error = None
global x , cities , countries
if request.method=='POST':
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password=password_of_db,
 database="wphdb"
)

mycursor = mydb.cursor()
mycursor.execute('select * from wph_table')
result = mycursor.fetchall()

ulist = []
plist = []

for i in range(0,len(result)):
ulist.append(result[i][0])
plist.append(result[i][1])
x = request.form['username']
if request.form['username'] in ulist and request.form['password'] in plist and ulist.index(request.form['username'])==plist.index(request.form['password']):
cities = cities_know(x)
countries = countries_know(x)
return redirect(url_for('dashboard'))
else:
error='Invalid Credentials , Please try again'
#form = Login_form()
return render_template('login.html',error=error)

if __name__ == "__main__":
   app.run()
