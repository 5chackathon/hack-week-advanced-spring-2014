from flask import Flask, render_template, request
import random
from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo


app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

mongodb_uri = 'mongodb://pomonashuffle:arrokearroke@ds033907.mongolab.com:33907/pomonashuffle'
db_name = 'pomonashuffle'
connection = pymongo.Connection(mongodb_uri)
db = connection[db_name]

course_col = db.course_col

@app.route('/majors')
def majors():
	course_list = list(db.course_col.find())
	major_list = set([])
	for i in range(0,len(course_list)):
		major_list.add(course_list[i]['major'])
	major = list(major_list)
	major.sort()
	length = len(major)
	return render_template('majors.html',length =length,major= major)

@app.route('/major/<major>')
def classlist(major):
	course_list = list(db.course_col.find( {"major" : major}))
	for c in course_list:
		print(c)
	return render_template("courses.html",course_list = course_list)
	


@app.route('/')
def index():
	course_list = list(db.course_col.find())
	random.shuffle(course_list)
	return render_template('index.html', course_list=course_list)

if __name__ == '__main__':
    app.run()
