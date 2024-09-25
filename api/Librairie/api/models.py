from django.db import models

# Table: Etudiants
class Etudiant(models.Model):
    id_eleve = models.AutoField(primary_key=True)  # Id_Eleve
    nom = models.CharField(max_length=50)  # Nom
    prenom = models.CharField(max_length=50)  # Prenom
    classe = models.CharField(max_length=50)  # Classe
    date_naissance = models.DateField()  # Date_Naissance
    adresse = models.CharField(max_length=255)  # Adresse
    telephone = models.CharField(max_length=255)  # Telephone

    def __str__(self):
        return f"{self.nom} {self.prenom}"

# Table: TypeLivre
class TypeLivre(models.Model):
    id_type_livre = models.AutoField(primary_key=True)  # ID_TypeLivre
    nom_type = models.CharField(max_length=255)  # Nom_Type

    def __str__(self):
        return self.nom_type

# Table: Auteur
class Auteur(models.Model):
    id_auteur = models.AutoField(primary_key=True)  # ID_Auteur
    nom_auteur = models.CharField(max_length=255)  # Nom_Auteur
    prenom_auteur = models.CharField(max_length=255)  # Prenom_Auteur

    def __str__(self):
        return f"{self.prenom_auteur} {self.nom_auteur}"

# Table: Livres
class Livre(models.Model):
    id_livre = models.AutoField(primary_key=True)  # ID_Livre
    titre = models.CharField(max_length=255)  # Titre
    auteur = models.ForeignKey(Auteur, on_delete=models.SET_NULL, null=True, related_name='livres')  # Auteur
    type_livre = models.ForeignKey(TypeLivre, on_delete=models.SET_NULL, null=True, related_name='livres')  # TypeLivre
    isbn = models.CharField(max_length=255)  # ISBN
    genre = models.CharField(max_length=255)  # Genre
    date_publication = models.DateField()  # Date_Publication
    nombre_exemplaires = models.IntegerField()  # Nombre_Exemplaires

    def __str__(self):
        return self.titre

# Table: Personnels
class Personnel(models.Model):
    id_personnel = models.AutoField(primary_key=True)  # ID_Personnel
    nom = models.CharField(max_length=255)  # Nom
    prenom = models.CharField(max_length=255)  # Prenom
    poste = models.CharField(max_length=255)  # Poste
    date_embauche = models.CharField(max_length=255)  # Date_Embauche
    telephone = models.CharField(max_length=255)  # Telephone

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.poste}"

# Table: Categories
class Categorie(models.Model):
    id_categorie = models.AutoField(primary_key=True)  # ID_Categorie
    nom_categorie = models.CharField(max_length=255)  # Nom_Categorie
    description = models.TextField()  # Description

    def __str__(self):
        return self.nom_categorie

# Table: Emprunts
class Emprunt(models.Model):
    id_eleve = models.ForeignKey(Etudiant, on_delete=models.CASCADE)  # Id_Eleve
    id_livre = models.ForeignKey(Livre, on_delete=models.CASCADE)  # ID_Livre
    id_personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)  # ID_Personnel

    class Meta:
        unique_together = (('id_eleve', 'id_livre', 'id_personnel'),)  # Emprunts_PK

    def __str__(self):
        return f"Emprunt de {self.id_livre} par {self.id_eleve}"

# Table: Appartient
class Appartient(models.Model):
    id_categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)  # ID_Categorie
    id_livre = models.ForeignKey(Livre, on_delete=models.CASCADE)  # ID_Livre

    class Meta:
        unique_together = (('id_categorie', 'id_livre'),)  # Appartient_PK

    def __str__(self):
        return f"{self.id_livre} appartient à {self.id_categorie}"
