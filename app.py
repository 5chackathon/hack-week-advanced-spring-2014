from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/major/<major>/<int:number>', methods=['GET', 'POST'])
def ratings(major, number):
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
            # Change the request type to GET
            return redirect(url_for('ratings', major=major, number=number), code=303)

    reviews = list(db.reviews.find({'major': major, 'course_number': number}))
    course = db.course_col.find({"major": major, "number" : number})
    avg_rating = None
    if reviews:
        ratings_sum = sum([r.get('rating', 0) for r in reviews])
        avg_rating = float(ratings_sum) / len(reviews)
        avg_rating = round(avg_rating, 2)
    course = course[0]
    return render_template("ratings.html", course=course, avg_rating=avg_rating,
            reviews=reviews)


@app.route('/courses')
def classes_for_major():
    major_code = request.args.get('major', 'any')
    school = request.args.get('school', 'any')

    major = None

    filter_doc = {}

    if major_code != 'any':
        filter_doc['major'] = major_code
        major = MAJORS[major_code]
    else:
        major_code = None

    if school != 'any':
        filter_doc['school'] = school
    else:
        school = None

    def by_name(course):
        return course['name']

    courses = sorted(list(db.course_col.find(filter_doc)), key=by_name)

    return render_template("courses.html", courses=courses,
                           major_code=major_code, major=major)


@app.route('/')
def index():
    courses = list(db.course_col.find())
    return render_template('index.html', courses=courses, majors=MAJORS)


if __name__ == '__main__':
    app.run(debug=True)
