# app.py
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'andrea_key'

db = SQLAlchemy(app)

@app.route('/')
def index():
    playlists = Playlist.query.all()
    return render_template('index.html', playlists=playlists)

@app.route('/playlist/<int:playlist_id>', methods=['GET', 'POST'])
def playlist(playlist_id):
    playlist = Playlist.query.get(playlist_id)
    form = SongForm()

    if form.validate_on_submit():
        title = form.title.data
        artist = form.artist.data

        song = Song(title=title, artist=artist)
        db.session.add(song)
        db.session.commit()

        playlist.songs.append(song)
        db.session.commit()

        return redirect(url_for('playlist', playlist_id=playlist_id))

    return render_template('playlist.html', playlist=playlist, form=form)

@app.route('/create_playlist', methods=['GET', 'POST'])
def create_playlist():
    form = PlaylistForm()

    if form.validate_on_submit():
        name = form.name.data
        playlist = Playlist(name=name)
        db.session.add(playlist)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('create_playlist.html', form=form)

@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
  playlist = Playlist.query.get_or_404(playlist_id)
  form = NewSongForPlaylistForm()
  curr_on_playlist = [s.id for s in playlist.songs]
  form.song.choices = (db.session.query(Song.id, Song.title)
                      .filter(Song.id.notin_(curr_on_playlist))
                      .all())

  if form.validate_on_submit():
      playlist_song = PlaylistSong(song_id=form.song.data,
                                  playlist_id=playlist_id)
      db.session.add(playlist_song)

      db.session.commit()

      return redirect(f"/playlists/{playlist_id}")

  return render_template("add_song_to_playlist.html",
                         playlist=playlist,
                         form=form)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


