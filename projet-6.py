import sqlite3 

conn =sqlite3.connect('Test.db')
cur = conn.cursor()
conn.commit()
"""def create_contact():
    req = "CREATE TABLE contact(id integer primary key, nom, prenom, email, telephone)"
    cur.execute(req)
    conn.commit()
create_contact()

def inserer_contact():
    req = "INSERT INTO contact(nom, prenom, email, telephone) values('Aidara', 'Fanta', 'sire@gmail.com', '775851112')"
    cur.execute(req)
    conn.commit()
inserer_contact()

def ajouter_contact():
    nom = input("Entrer votre nom")
    prenom = input("Entrer votre prenom")
    email = input("Entrer votre email")
    telephone = int(input("Entrer votre numero tel"))
    req1="INSERT INTO contact(nom, prenom, email, telephone) values(?,?,?,?)"
    cur.execute(req1,(nom, prenom, email, telephone))
ajouter_contact()

def modifier_contact():
    nouveau_numero = "763640802"
    ancien_numero = "775851112"
    cur.execute(
        "UPDATE contact SET telephone = ? where telephone= ?",
        (nouveau_numero,  ancien_numero)
        )
    conn.commit()
modifier_contact()

def supprimer_contact():
    telephone = "763640802"
    cur.execute(
        "DELETE FROM contact WHERE telephone = ?",
        (telephone,)
    )
supprimer_contact()    
conn.commit()    
    
def afficher_list_contact():
    rows = cur.execute("SELECT * FROM contact").fetchall()
    print(rows)
afficher_list_contact()"""

def rechercher_contact():
    rows = cur.execute("SELECT * FROM contact WHERE telephone = 786543212").fetchone()
    print(rows)
rechercher_contact()
conn.commit()