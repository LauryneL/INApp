from flask import render_template, request


from .app import app
from .modeles.donnees import BardINAge


@app.route("/")
def accueil():
    # On a bien sûr aussi modifié le template pour refléter le changement
    videos = BardINAge.query.all()
    return render_template("pages/accueil.html", nom="INApp", videos=videos)


@app.route("/player/<RNO>")
def player(RNO):
    # On a bien sûr aussi modifié le template pour refléter le changement
    unique_video = BardINAge.query.get(RNO)
    return render_template("pages/place.html", nom="INApp", video=unique_video)


@app.route("/recherche")
def recherche():
    # On préfèrera l'utilisation de .get() ici
    #   qui nous permet d'éviter un if long (if "clef" in dictionnaire and dictonnaire["clef"])
    motclef = request.args.get("keyword", None)
    # On crée une liste vide de résultat (qui restera vide par défaut
    #   si on n'a pas de mot clé)
    resultats = []
    # On fait de même pour le titre de la page
    titre = "Recherche"
    if motclef:
        resultats = BardINAge.query.filter(
            BardINAge.Description_detaillee.like("%{}%".format(motclef))
        ).all()
    return render_template("pages/recherche.html", resultats=resultats, titre=titre)
