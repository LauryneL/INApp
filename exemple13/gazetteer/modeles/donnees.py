from .. app import db


# On crée notre modèle
class video(db.Model):
    chanteur = db.Column(db.Text)
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    chanson = db.Column(db.Text)
    url = db.Column(db.Text)

