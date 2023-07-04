import sqlite3 
#Création de la connexion à la base de données
conn =sqlite3.connect('Contact.db')
cur = conn.cursor()
#Création de la table Contact
"""cur.execute(
    "CREATE TABLE Contact(nom text, prenom text, email text, telephone integer)"
)"""
#declaration de la class contact
class Contact:
    def __init__(self, nom, prenom, email, telephone):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = telephone
    def inserer(self):
        cur.execute("INSERT INTO Contact(nom, prenom, email, telephone) VALUES(?, ?, ?, ?)",
                    (self.nom, self.prenom, self.email, self.telephone))
        conn.commit()

    
    def ajouter_contact(self, nom, prenom, email, telephone):
        contact = Contact(nom, prenom, email, telephone)
        contact.inserer()

    
    def modifier_contact(self, nouveau_numero, ancien_numero):
        cur.execute("UPDATE Contact SET telephone = ? WHERE telephone = ?", (nouveau_numero, ancien_numero))
        conn.commit()

    
    def supprimer_contact(self, telephone):
        cur.execute("DELETE FROM Contact WHERE telephone = ?", (telephone,))
        conn.commit()


    def afficher_liste_contact(self):
        rows = cur.execute("SELECT * FROM Contact").fetchall()
        for row in rows:
            print(row)


    def rechercher_numero_contact(self, telephone):
        row = cur.execute("SELECT * FROM Contact WHERE telephone = ?", (telephone,)).fetchone()
        print(row)
        
#Instance de la classe Contact
contact = Contact("Aidara", "Cherif", "bakis1011@gmail.com", 775851112)
contact.inserer()

contact = Contact("Aidara", "Moulaye", "moulaye@gmail.com", 774673332)
contact.ajouter_contact(contact.nom, contact.prenom, contact.email, contact.telephone)

#Méthode de la classe 
contact.modifier_contact(787202863, contact.telephone)
contact.supprimer_contact(775851112)
contact.afficher_liste_contact()
contact.rechercher_numero_contact(774673332)

cur.execute("INSERT INTO Contact VALUES (?, ?, ?, ?)", (contact.nom, contact.prenom, contact.email, contact.telephone))
conn.commit()