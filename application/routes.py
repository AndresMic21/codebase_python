
from unittest.util import _MAX_LENGTH
from application import app, db
from flask import render_template,request, json,Response
import urllib.request, json
from icecream import ic


resp = urllib.request.urlopen('https://query2.finance.yahoo.com/v10/finance/quoteSummary/MSFT?modules=price')
data = json.loads(resp.read())
price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
print(price)
ic(price)
ic(price)





courseData = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,
"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,
"term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,
"term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"},
{"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}]


#decorators
@app.route("/")
@app.route("/index")
@app.route("/home")

def index():
    return render_template("index.html",index=True)

@app.route("/login")
def login():
    return render_template("login.html",login=True)


@app.route("/course/")
@app.route("/course/<term>")
def course(term="Spring 2022 //",stock=price):
    return render_template("course.html",courseData=courseData,course=True,term=term,stock=stock)

@app.route("/register")
def register():
    return render_template("register.html",register=True)


@app.route("/enrollment", methods=["GET","POST"])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template("enrollment.html",enrollment=True, data={"id":id,"title":title,"term":term})


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if (idx==None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    return Response(json.dumps(jdata), mimetype="application/json")


class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField( max_lenght=50)
    last_name = db.StringField( max_lenght=50)
    email =  db.StringField( max_lenght=50)
    password =  db.StringField( max_lenght=50)

@app.route("/user")
def user():
    #User(user_id=1,first_name='Cuco', last_name="Smith",email='cuco@gmail.com',password='abc123').save()
    users = User.objects.all()
    return render_template("user.html",users=users)


