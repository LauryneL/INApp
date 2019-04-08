from .. app import db


# On crée notre modèle
class Player(db.Model):

    RNO = db.Column(db.Text, unique=True, nullable=False, primary_key=True)
    Description_detaillee = db.Column(db.Text)
    Titre_chanson = db.Column(db.Text)
    Titre_emission = db.Column(db.Text)
    Nom_chaine = db.Column(db.Text)
    date_emission = db.Column(db.Text)
    Nom_artiste_INA = db.Column(db.Text)
    ID_wikidata_artiste = db.Column(db.Text)
    Bnfid = db.Column(db.Text)
    Url_chanson_wd = db.Column(db.Text)
    Id_wd_chanson = db.Column(db.Text)
    Genre_chanson_wd = db.Column(db.Text)
    Date_sortie_chanson_wd = db.Column(db.Text)
    url_wd_personne = db.Column(db.Text)
    date_naissance = db.Column(db.Text)
    image_wd_chanteur = db.Column(db.Text)
    url_bnf_chanson = db.Column(db.Text)
    Bnf_id_song = db.Column(db.Text)
    Url_artiste_dbp = db.Column(db.Text)
    Image_artiste_dbp = db.Column(db.Text)
    Date_mort_artiste_dbp = db.Column(db.Text)
    url_bnf_chanteur = db.Column(db.Text)
    nom_artiste_propre = db.Column(db.Text)
