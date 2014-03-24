from flask import Flask, render_template, request
import random
import pymongo
import yaml

app = Flask(__name__)

mongodb_uri = 'mongodb://pomonashuffle:arrokearroke@ds033907.mongolab.com:33907/pomonashuffle'
db_name = 'pomonashuffle'
connection = pymongo.Connection(mongodb_uri)
db = connection[db_name]

course_col = db.course_col

MAJORS = yaml.load(file('majors.yaml', 'r'))

@app.route('/majors')
def majors():
    return render_template('majors.html', majors=MAJORS)


@app.route('/courses')
def classes_for_major():
    major_code = request.args.get('major', 'any')
    school = request.args.get('school', 'any')

    if major_code not in MAJORS:
        # Show all the majors
        courses = list(db.course_col.find())
        major = None
        major_code = None
    else:
        courses = list(db.course_col.find({ 'major': major_code }))
        major = MAJORS[major_code]
    return render_template("courses.html", courses=sorted(courses),
            major_code=major_code, major=major)


@app.route('/')
def index():
    courses = list(db.course_col.find())
    random.shuffle(courses)
    return render_template('index.html', courses=courses, majors=MAJORS)


if __name__ == '__main__':
    app.run(debug=True)
