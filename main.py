from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "supersecret"

# Alle Hobbys mit Kategorien
all_hobbies = [
    {
        "name": "Klettern",
        "description": "Klettere in der Halle oder in der Natur.",
        "schwierigkeit": 8,
        "aufwand": 7,
        "kosten": 6,
        "indoor_outdoor": 9,
        "aktiv_entspannt": 10
    },
    {
        "name": "Lesen",
        "description": "Tauche in fremde Welten ein.",
        "schwierigkeit": 2,
        "aufwand": 1,
        "kosten": 1,
        "indoor_outdoor": 2,
        "aktiv_entspannt": 0
    },
    {
        "name": "Fotografie",
        "description": "Halte besondere Momente fest.",
        "schwierigkeit": 4,
        "aufwand": 5,
        "kosten": 6,
        "indoor_outdoor": 5,
        "aktiv_entspannt": 5
    },
    {
        "name": "Schreiben",
        "description": "Erzähle deine eigenen Geschichten.",
        "schwierigkeit": 3,
        "aufwand": 3,
        "kosten": 1,
        "indoor_outdoor": 1,
        "aktiv_entspannt": 2
    },
    {
        "name": "Joggen",
        "description": "Einfach loslaufen, Kopf frei kriegen.",
        "schwierigkeit": 3,
        "aufwand": 2,
        "kosten": 0,
        "indoor_outdoor": 9,
        "aktiv_entspannt": 9
    },
    {
        "name": "Gärtnern",
        "description": "Grüne Daumen und frische Luft.",
        "schwierigkeit": 3,
        "aufwand": 4,
        "kosten": 2,
        "indoor_outdoor": 8,
        "aktiv_entspannt": 3
    },
    {
        "name": "Meditation",
        "description": "Finde innere Ruhe.",
        "schwierigkeit": 2,
        "aufwand": 1,
        "kosten": 0,
        "indoor_outdoor": 3,
        "aktiv_entspannt": 0
    },
    {
        "name": "Schach",
        "description": "Trainiere deine strategischen Fähigkeiten.",
        "schwierigkeit": 6,
        "aufwand": 3,
        "kosten": 0,
        "indoor_outdoor": 1,
        "aktiv_entspannt": 1
    },
    {
        "name": "Stricken",
        "description": "Handarbeit mit Stil und Geduld.",
        "schwierigkeit": 4,
        "aufwand": 4,
        "kosten": 2,
        "indoor_outdoor": 1,
        "aktiv_entspannt": 1
    },
    {
        "name": "Töpfern",
        "description": "Ton formen, eigene Kunstwerke schaffen.",
        "schwierigkeit": 5,
        "aufwand": 6,
        "kosten": 5,
        "indoor_outdoor": 2,
        "aktiv_entspannt": 3
    },
    {
        "name": "Wandern",
        "description": "Natur entdecken und abschalten.",
        "schwierigkeit": 3,
        "aufwand": 2,
        "kosten": 1,
        "indoor_outdoor": 10,
        "aktiv_entspannt": 5
    },
    {
        "name": "Malen",
        "description": "Kreativität auf Leinwand.",
        "schwierigkeit": 3,
        "aufwand": 3,
        "kosten": 2,
        "indoor_outdoor": 2,
        "aktiv_entspannt": 2
    },
    {
        "name": "Skateboarden",
        "description": "Tricks und Bewegung.",
        "schwierigkeit": 7,
        "aufwand": 6,
        "kosten": 3,
        "indoor_outdoor": 9,
        "aktiv_entspannt": 9
    },
    {
        "name": "Kochen",
        "description": "Kreativität mit Geschmack.",
        "schwierigkeit": 4,
        "aufwand": 5,
        "kosten": 5,
        "indoor_outdoor": 1,
        "aktiv_entspannt": 3
    },
    {
        "name": "Origami",
        "description": "Falten mit Fingerspitzengefühl.",
        "schwierigkeit": 5,
        "aufwand": 2,
        "kosten": 0,
        "indoor_outdoor": 1,
        "aktiv_entspannt": 1
    },
    {
        "name": "Drohnen fliegen",
        "description": "Technik und Perspektive.",
        "schwierigkeit": 5,
        "aufwand": 4,
        "kosten": 8,
        "indoor_outdoor": 8,
        "aktiv_entspannt": 4
    },
    {
        "name": "Parkour",
        "description": "Stadt wird Spielplatz.",
        "schwierigkeit": 9,
        "aufwand": 8,
        "kosten": 1,
        "indoor_outdoor": 10,
        "aktiv_entspannt": 10
    },
    {
        "name": "Zaubern",
        "description": "Menschen verblüffen mit Tricks.",
        "schwierigkeit": 6,
        "aufwand": 6,
        "kosten": 3,
        "indoor_outdoor": 5,
        "aktiv_entspannt": 4
    },
    {
        "name": "Upcycling",
        "description": "Altes in Neues verwandeln.",
        "schwierigkeit": 4,
        "aufwand": 3,
        "kosten": 0,
        "indoor_outdoor": 3,
        "aktiv_entspannt": 2
    },
    {
        "name": "Freerunning",
        "description": "Akrobatik im Alltag.",
        "schwierigkeit": 9,
        "aufwand": 9,
        "kosten": 1,
        "indoor_outdoor": 9,
        "aktiv_entspannt": 10
    },
    {
        "name": "Improvisationstheater",
        "description": "Spontanität auf der Bühne trainieren.",
        "schwierigkeit": 6,
        "aufwand": 4,
        "kosten": 2,
        "indoor_outdoor": 1,
        "aktiv_entspannt": 6
    },
    {
        "name": "Astronomie",
        "description": "Sterne beobachten und Weltraum erkunden.",
        "schwierigkeit": 4,
        "aufwand": 3,
        "kosten": 3,
        "indoor_outdoor": 7,
        "aktiv_entspannt": 2
    },
    {
        "name": "Graffiti",
        "description": "Kunst im urbanen Raum erschaffen.",
        "schwierigkeit": 5,
        "aufwand": 4,
        "kosten": 2,
        "indoor_outdoor": 9,
        "aktiv_entspannt": 6
    },
    {
        "name": "Bouldern",
        "description": "Klettern in Bodennähe, ohne Seil.",
        "schwierigkeit": 7,
        "aufwand": 5,
        "kosten": 4,
        "indoor_outdoor": 6,
        "aktiv_entspannt": 9
    },
    {
        "name": "Slacklining",
        "description": "Balance auf dem Seil üben.",
        "schwierigkeit": 6,
        "aufwand": 3,
        "kosten": 3,
        "indoor_outdoor": 8,
        "aktiv_entspannt": 8
    },
    {
        "name": "Brettspiele",
        "description": "Gemeinsam spielen und Strategie beweisen.",
        "schwierigkeit": 3,
        "aufwand": 2,
        "kosten": 2,
        "indoor_outdoor": 1,
        "aktiv_entspannt": 1
    },
    {
        "name": "Schauspiel",
        "description": "In Rollen schlüpfen und Emotionen zeigen.",
        "schwierigkeit": 5,
        "aufwand": 5,
        "kosten": 2,
        "indoor_outdoor": 2,
        "aktiv_entspannt": 5
    },
    {
        "name": "Surfen",
        "description": "Wellenreiten am Meer.",
        "schwierigkeit": 8,
        "aufwand": 7,
        "kosten": 7,
        "indoor_outdoor": 10,
        "aktiv_entspannt": 9
    },
    {
        "name": "Kerzen gießen",
        "description": "Kreatives mit Wachs gestalten.",
        "schwierigkeit": 2,
        "aufwand": 2,
        "kosten": 2,
        "indoor_outdoor": 1,
        "aktiv_entspannt": 2
    },
    {
        "name": "Podcasting",
        "description": "Eigene Inhalte aufnehmen und teilen.",
        "schwierigkeit": 4,
        "aufwand": 5,
        "kosten": 3,
        "indoor_outdoor": 1,
        "aktiv_entspannt": 2
    },
    {
        "name": "Geocaching",
        "description": "Mit GPS auf Schatzsuche gehen.",
        "schwierigkeit": 4,
        "aufwand": 4,
        "kosten": 1,
        "indoor_outdoor": 10,
        "aktiv_entspannt": 6
    },
    {
        "name": "Nähen",
        "description": "Eigene Kleidung und Accessoires kreieren.",
        "schwierigkeit": 5,
        "aufwand": 5,
        "kosten": 3,
        "indoor_outdoor": 1,
        "aktiv_entspannt": 2
    },
    {
        "name": "Kalligrafie",
        "description": "Schönschrift und Lettering üben.",
        "schwierigkeit": 4,
        "aufwand": 2,
        "kosten": 2,
        "indoor_outdoor": 1,
        "aktiv_entspannt": 1
    },
    {
        "name": "Modellbau",
        "description": "Miniaturwelten erschaffen.",
        "schwierigkeit": 5,
        "aufwand": 6,
        "kosten": 4,
        "indoor_outdoor": 1,
        "aktiv_entspannt": 2
    },
    {
        "name": "Filmemachen",
        "description": "Drehen, schneiden, erzählen.",
        "schwierigkeit": 6,
        "aufwand": 7,
        "kosten": 6,
        "indoor_outdoor": 5,
        "aktiv_entspannt": 4
    },
    {
        "name": "Hula-Hoop",
        "description": "Fitness mit Spaß verbinden.",
        "schwierigkeit": 4,
        "aufwand": 2,
        "kosten": 1,
        "indoor_outdoor": 7,
        "aktiv_entspannt": 7
    },
    {
        "name": "Stand-Up Comedy",
        "description": "Menschen mit Witz begeistern.",
        "schwierigkeit": 7,
        "aufwand": 5,
        "kosten": 1,
        "indoor_outdoor": 2,
        "aktiv_entspannt": 5
    },
    {
        "name": "Trickfilm-Zeichnen",
        "description": "Bewegte Zeichnungen selbst machen.",
        "schwierigkeit": 6,
        "aufwand": 7,
        "kosten": 3,
        "indoor_outdoor": 1,
        "aktiv_entspannt": 3
    },
    {
        "name": "Fischen",
        "description": "Ruhe und Geduld in der Natur.",
        "schwierigkeit": 4,
        "aufwand": 3,
        "kosten": 4,
        "indoor_outdoor": 10,
        "aktiv_entspannt": 1
    },
    {
        "name": "Schmuck designen",
        "description": "Einzigartige Accessoires selbst machen.",
        "schwierigkeit": 4,
        "aufwand": 4,
        "kosten": 2,
        "indoor_outdoor": 1,
        "aktiv_entspannt": 2
    },
]

@app.route("/")
def home():
    # Wenn noch keine Präferenzen gesetzt, leite zu /setup
    if "preferences" not in session:
        return redirect(url_for("setup"))
    return render_template("home.html")

@app.route("/setup", methods=["GET", "POST"])
def setup():
    if request.method == "POST":
        prefs = {
            "schwierigkeit": int(request.form["schwierigkeit"]),
            "aufwand": int(request.form["aufwand"]),
            "kosten": int(request.form["kosten"]),
            "indoor_outdoor": int(request.form["indoor_outdoor"]),
            "aktiv_entspannt": int(request.form["aktiv_entspannt"]),
        }

        def score(h):
            return sum([
                abs(h["schwierigkeit"] - prefs["schwierigkeit"]),
                abs(h["aufwand"] - prefs["aufwand"]),
                abs(h["kosten"] - prefs["kosten"]),
                abs(h["indoor_outdoor"] - prefs["indoor_outdoor"]),
                abs(h["aktiv_entspannt"] - prefs["aktiv_entspannt"]),
            ])

        sorted_hobbies = sorted(all_hobbies, key=score)
        session["remaining"] = sorted_hobbies[:5]
        session["liked"] = []
        return redirect("/swipe")

    return render_template("setup.html")

@app.route("/swipe")
def swipe():
    if "remaining" not in session or not session["remaining"]:
        return redirect("/nomore")

    hobby = session["remaining"][0]
    return render_template("swipe.html", hobby=hobby)

@app.route("/swipe_action", methods=["POST"])
def swipe_action():
    action = request.form.get("action")
    hobby = session["remaining"].pop(0)
    if action == "like":
        session["liked"].append(hobby)
    return redirect("/swipe")

@app.route("/nomore")
def nomore():
    return render_template("nomore.html", hobbies=session.get("liked", []))

@app.route("/like", methods=["POST"])
def like():
    if session.get("remaining"):
        hobby = session["remaining"][0]
        session["liked"].append(hobby)
        session["remaining"] = session["remaining"][1:-1]
    return redirect(url_for("swipe"))

@app.route("/dislike", methods=["POST"])
def dislike():
    if session.get("remaining"):
        session["remaining"] = session["remaining"][1:-1]
    return redirect(url_for("swipe"))

@app.route("/match")
def match():
    return render_template("match.html", hobbies=session.get("liked", []))

if __name__ == "__main__":
    app.run("0.0.0.0", 3073, debug=True)
