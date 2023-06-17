import sqlite3 
#Création de la connexion à la base de données
conn =sqlite3.connect('contact.db')
cur = conn.cursor()
#Création de la table Contact
cur.execute(
    "CREATE TABLE Contact(nom text, prenom text, email text, telephone integer)"
)
#declaration de la class contact
class Contact:
    def __init__(self, nom, prenom, email, telephone):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = telephone
    def inserer(self):
        print(self.nom)
        print(self.prenom)
        print(self.email)
        print(self.telephone)
#definition de la fonction ajouter    
def ajouter_contact(nom, prenom, email, telephone):
    cur.execute("INSERT INTO Contact(nom, prenom, email, telephone) VALUES(?, ?, ?, ?)", (nom, prenom, email, telephone))
#definition de la fonction modifier        
def modifier_contact():
    nouveau_numero = "707202863"
    ancien_numero = "775851112"
    cur.execute(
        "UPDATE contact SET telephone = ? WHERE telephone = ?",
        (nouveau_numero, ancien_numero)
    )
#definition de la fonction supprimer
def supprimer_contact():
    telephone = "774673332"
    cur.execute(
        "DELETE FROM Contact WHERE telephone = ?",
        (telephone,)
    )
#definition de la fonction affichage liste
def afficher_liste_contact():
    rows = cur.execute("SELECT * FROM Contact").fetchall()
    print(rows)
#definition de la fonction recherche
def rechercher_numero_contact():
    row = cur.execute("SELECT * FROM Contact WHERE telephone = 775851112").fetchone()
    print(row)
#Instance de la class Contact
contact = Contact("Aidara", "Cherif", "bakis1011@gmail.com", 775851112)
contact.inserer()
ajouter_contact("Aidara", "Moulaye", "moulaye@gmail.com", 774673332)
modifier_contact()
supprimer_contact()
afficher_liste_contact()
rechercher_numero_contact()
#Insertion des données de l'objet dans la base de données
cur.execute("INSERT INTO Contact VALUES (?, ?, ?, ?)", (contact.nom, contact.prenom, contact.email, contact.telephone))
conn.commit()