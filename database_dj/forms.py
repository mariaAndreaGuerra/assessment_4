from wtforms import SelectField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length


class PlaylistForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])

class SongForm(FlaskForm):
   title = StringField('Title', validators=[DataRequired(), Length(min=1, max=100)])
   artist = StringField('Artist', validators=[DataRequired(), Length(min=1, max=100)])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)

