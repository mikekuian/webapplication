from flask import Flask, request, escape, redirect, render_template
import db

app = Flask(__name__)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        x = int(request.form.get('x'))
        y = int(request.form.get('y'))
        expression = f'{x} {request.form.get("operation")} {y}'
        errors = ""
        try:
            equation = f'{expression} = {eval(expression)}'
        except ZeroDivisionError:
            errors = "Zero division!"
            equation = expression
        return render_template('calculator.html', equation=equation, x=x, y=y, selected=request.form.get("operation"),
                               errors=errors)
    elif request.method == 'GET':
        return render_template('calculator.html', selected="0", equation=None, x=0, y=0, errors=None)


@app.route('/about')
def about():
    return render_template('about.html', selected="0")


@app.route('/students', methods=['GET', 'POST'])
def students_list():
    if request.method == 'POST':
        id = int(request.form.get('id'))
        name = request.form.get('name')
        email = request.form.get('email')
        db.insert(id=id, name=name, email=email)
        return render_template('students.html', students=db.search(), id=id, name=name, email=email)
    elif request.method == 'GET':
        return render_template('students.html', students=db.search(), id="", name="", email="")


@app.route('/students/<int:student_id>', methods=['POST','GET'])
def student_detail_view(student_id):
    if request.method == 'GET':
        db_search = db.search(id=student_id)
        student = db_search and db_search[0] or None
        return render_template('student_detail.html', student=student)


@app.route('/students/<int:student_id>/student_update', methods=['POST', 'GET'])
def student_update(student_id):
    student=db.search(id=student_id)[0]
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        db.update({'name': name, 'email': email}, {'id':student_id})
        return redirect('/students')
    elif request.method == 'GET':
        return render_template('student_update.html', student=student)


@app.route('/students/<int:student_id>/confirm_delete', methods=['POST', 'GET'])
def confirm_delete(student_id):
    if request.method == 'GET':
        return render_template('confirm_delete.html')
    elif request.method == 'POST':
        if request.form['submit_button'] == 'Yes':
            db.delete(id=student_id)
            return redirect('/students')
        else:
            return redirect('/students')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
