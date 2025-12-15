from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_emi(principal, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12
    emi = principal * monthly_rate * ((1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1)
    return round(emi, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    emi = None

    if request.method == 'POST':
        total_amount = float(request.form['total_amount'])
        down_payment = float(request.form['down_payment'])
        rate = float(request.form['interest_rate'])
        duration = int(request.form['duration'])

        loan_amount = total_amount - down_payment
        emi = calculate_emi(loan_amount, rate, duration)

    return render_template('index.html', emi=emi)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
