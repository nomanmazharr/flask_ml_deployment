import pandas as pd
from flask_wtf import FlaskForm
from wtforms import(
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField

)

from wtforms.validators  import(
    DataRequired
)

train = pd.read_csv('dataset\\train.csv')
val = pd.read_csv('dataset\\val.csv')
x_data = pd.concat([train, val], axis=0).drop(columns='price')

class CheckPrice(FlaskForm):
    airline = SelectField(
        label= 'Airline',
        choices=x_data.airline.unique().tolist(),
        validators=[DataRequired()]
    )

    date_of_journey = DateField(
        label='Date of Journey',
        validators=[DataRequired()]
    )

    source = SelectField(
        label= 'Source',
        choices=x_data.source.unique().tolist(),
        validators=[DataRequired()]
    )

    destination = SelectField(
        label= 'Destination',
        choices=x_data.destination.unique().tolist(),
        validators=[DataRequired()]
    )

    dep_time = TimeField(
        label = 'Depart Time',
        validators=[DataRequired()]
    )

    arrival_time = TimeField(
        label = 'Arrival Time',
        validators= [DataRequired()]
    )
    
    duration = IntegerField(
        label="Duration",
        validators=[DataRequired()]
    )

    total_stops = IntegerField(
        label = 'Total Stops',
        validators=[DataRequired()]
    )

    additional_info = SelectField(
        label='Additional Info',
        choices=x_data.additional_info.unique().tolist(),
        validators = [DataRequired()]
    )

    submit = SubmitField('Predict')