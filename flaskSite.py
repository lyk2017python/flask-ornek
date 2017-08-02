from flask import Flask, render_template, request , redirect
import json

app = Flask(__name__)

kullanicilar = {"ahmet": "aksoy", "selim": "koc", "ayse": "donmez"}
json_file = "kisiler.json"

@app.route("/")
def hello():
    isimler = ["Ahmet", "Burak", "Ayse", "Ali"]
    return render_template("yeni_index.html", isimlistesi=isimler)


@app.route("/kullanicilar")
def kullanicilar():
    try:
        kisilistesi = json.load(open(json_file, "r"))
    except:
        kisilistesi = []


    return render_template("kullanici_kaydi.html",kisilistesi=kisilistesi)


@app.route("/kullanici_kaydet",methods=("POST","GET"))
def kullanici_kaydet():
    try:
        kisilistesi = json.load(open(json_file, "r"))
    except:
        kisilistesi = []

    if request.method == "POST":
        if request.form.get('isim', None) and request.form.get('telefon', None):
            kisilistesi.append({"isim": request.form.get('isim'),
                                "telefon": request.form.get('telefon')})

            open(json_file,"w+").write(json.dumps(kisilistesi)) #dosya yazma islemi

    return redirect("/kullanicilar")

@app.route("/kullanici/<kullanici>")
def kullanicilar_goruntuleme(kullanici):
    if kullanicilar.get(kullanici, None):
        bulunan_kullanici = kullanicilar.get(kullanici)
    else:
        bulunan_kullanici = None
    return render_template("kullanici.html", bulunan=bulunan_kullanici,
                           kullanici_url=kullanici)


@app.route("/secondpage")
def second_page():
    return "second page"


@app.route("/x")
def x():
    return "x"


app.run(debug=True, host="0.0.0.0", port=5000)
