from flask import Flask, render_template
from forms import CheckPrice
import pandas as pd
import pickle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = CheckPrice()
    if form.validate_on_submit():
        feature = pd.DataFrame(dict(
            airline = [form.airline.data],
            date_of_journey = [form.date_of_journey.data.strftime("%Y-%m-%d")],
            source = [form.source.data],
            destination= [form.destination.data],
            dep_time = [form.dep_time.data.strftime("%H:%M:%S")],
            arrival_time = [form.arrival_time.data.strftime("%H:%M:%S")],
            duration = [form.duration.data],
            total_stops = [form.total_stops.data],
            additional_info = [form.additional_info.data]
        ))
        prediction = model.predict(feature)[0]

        message = f'The predicted price is {prediction}'
    else:
        message = f'Please enter valid data to know the price'
    return render_template('predict.html', title = 'Booking', form = form, output=message)

if __name__ == '__main__':
    app.run(debug=True)