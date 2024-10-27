from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, SelectField
from wtforms.validators import InputRequired, email

# form used in basket
class CheckoutForm(FlaskForm):
    firstname = StringField("First name", validators=[InputRequired()])
    surname = StringField("Surname", validators=[InputRequired()])
    contact_time = SelectField(
        "Preferred Contact Time",
        choices=[
            ('morning', 'Morning'),
            ('afternoon', 'Afternoon'),
            ('evening', 'Evening')
        ],
        validators=[InputRequired()],
        default='morning'
    )
    email = StringField("Email", validators=[InputRequired(), email()])
    phone = StringField("Phone number", validators=[InputRequired()])
    submit = SubmitField("Send")