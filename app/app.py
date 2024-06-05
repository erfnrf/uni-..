from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('students'))

@app.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        father_name = request.form.get('father_name')
        birth_date = request.form.get('birth_date')
        serial_part1 = request.form.get('serial_part1')
        serial_part2 = request.form.get('serial_part2')
        serial_part3 = request.form.get('serial_part3')
        city_of_birth = request.form.get('city_of_birth')
        address = request.form.get('address')
        postal_code = request.form.get('postal_code')
        phone_number = request.form.get('phone_number')
        home_phone = request.form.get('home_phone')
        national_id = request.form.get('national_id')
        department = request.form.get('department')
        major = request.form.get('major')
        married = request.form.get('married')
        student_course_ids = request.form.get('student_course_ids')
        professor_ids = request.form.get('professor_ids')
        extra_info = request.form.get('extra_info')
        membership_status = request.form.get('membership_status')
        employment_status = request.form.get('employment_status')
        student_condition = request.form.get('student_condition')

        # اعتبارسنجی اطلاعات
        errors = []
        if not student_id:
            errors.append("شماره دانشجویی لازم است.")
        if not first_name:
            errors.append("نام لازم است.")
        if not last_name:
            errors.append("نام خانوادگی لازم است.")
        # بقیه اعتبارسنجی‌ها را اینجا اضافه کنید

        if errors:
            return render_template('students.html', errors=errors)
        
        # پردازش و ذخیره‌سازی اطلاعات
        # می‌توانید اطلاعات را در دیتابیس ذخیره کنید

        return "اطلاعات با موفقیت ثبت شد!"

    return render_template('students.html')

if __name__ == '__main__':
    app.run(debug=True)
