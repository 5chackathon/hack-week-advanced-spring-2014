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

@app.route('/major/<major>/<number>', methods=['GET', 'POST'])
def ratings(major, number):
    number = int(number)
    if request.method == 'POST':
        # Store the review in the database
        review_text = request.form.get('review', None)
        name = request.form.get('name', None)
        rating = int(request.form['rating'])
        if review_text:
            if not name:
                name = 'Anonymous'

            review = {
                'name': name,
                'text': review_text,
                'major': major,
                'course_number': number,
                'rating': rating
            }

            db.reviews.insert(review)

    reviews = list(db.reviews.find({'major': major, 'course_number': number}))
    course = db.course_col.find({"major": major, "number" : number})
    rating = sum([r.get('rating', 0) for r in reviews]) / float(len(reviews))
    rating = round(rating, 2)
    course = course[0]
    return render_template("ratings.html", course=course, rating=rating,
            reviews=reviews)


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
