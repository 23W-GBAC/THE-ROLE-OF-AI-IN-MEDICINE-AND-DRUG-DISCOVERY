from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

prescriptions = []

@app.route('/')
def index():
    return render_template('prescriptions.html', prescriptions=prescriptions)

@app.route('/prescribe', methods=['GET', 'POST'])
def prescribe():
    if request.method == 'POST':
        patient_name = request.form.get('patient_name')
        medication_name = request.form.get('medication_name')
        dosage = request.form.get('dosage')

        prescription = {
            'patient_name': patient_name,
            'medication_name': medication_name,
            'dosage': dosage,
            'prescribed_at': datetime.datetime.now()
        }

        prescriptions.append(prescription)

        return redirect(url_for('index'))

    return render_template('prescribe.html')


if __name__ == '__main__':
    app.run(debug=True)
