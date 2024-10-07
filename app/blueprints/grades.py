from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db

grades = Blueprint('grades', __name__)

@grades.route('/grade', methods=['GET', 'POST'])
def grade():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new grade
    if request.method == 'POST':
        number_grade = request.form['number_grade']
        student_name = request.form['student_name']
        if number_grade >= 90:
            letter_grade = "A"
        elif number_grade >= 80:
            letter_grade = "B"
        elif number_grade >= 70:
            letter_grade = "C"
        elif number_grade >= 60:
            letter_grade = "D"
        else:
            letter_grade = "you suck"
        # Insert the new grade info into the database
        cursor.execute('INSERT INTO grades (letter_grade, student_name) VALUES (%s, %s)', (letter_grade, student_name))

        return redirect(url_for('grades.grade'))

    # Handle GET request to display all grades
    cursor.execute('SELECT * FROM grades')
    all_grades = cursor.fetchall()
    return render_template('grades.html', all_grades=all_grades)








