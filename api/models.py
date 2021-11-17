from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Paiement(models.IntegerChoices):
	NULL=-1
	LUMICASH=1
	ECOCASH=2
	PAYPAL=3

class Utilisateur(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	avatar = models.ImageField(default='',upload_to='users/avatar')
	tel = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.user.username}"

class Categorie(models.Model):
	id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)

	def __str__(self):
	 	return f"{self.name}"

class Marque(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	logo = models.ImageField(default='',upload_to='marque/logo')

	def __str__(self):
	 	return f"{self.name}"


class Produits(models.Model):
	id = models.AutoField(primary_key=True)
	utilisateur = models.ForeignKey(User, related_name="produit_user", on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	prix = models.IntegerField()
	date = models.DateField()
	categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
	marque = models.ForeignKey(Marque,on_delete=models.CASCADE)
	image_devant = models.ImageField(upload_to='Produits/image')
	image_arriere = models.ImageField(upload_to='Produits/image')
	image_face = models.ImageField(upload_to='Produits/image')

	def __str__(self):
		return f"name : {self.name} Marque : {self.marque.name}"

class Vente(models.Model):
	id = models.AutoField(primary_key=True)
	produit = models.ForeignKey(Produits, related_name="vente_produit", on_delete=models.CASCADE)
	utilisateur = models.ForeignKey(User, related_name="vente_utilisateur", on_delete=models.CASCADE)
	quantite = models.PositiveIntegerField()
	montant = models.FloatField()
	code_transaction = models.PositiveIntegerField()

	def __str__(self):
		return f"{self.user.username} a achete {self.produit.name} {self.quantite} pour{self.montant}"

class Achat(models.Model):
	id = models.AutoField(primary_key=True)
	utilisateur = models.ForeignKey(User,related_name="achat_utilisateur",on_delete=models.CASCADE)
	produit = models.ForeignKey(Produits, related_name="achat_produit", on_delete=models.CASCADE)
	quantite = models.PositiveIntegerField()
	montant = models.FloatField()
	date = models.DateField()

	def __str__(self):
		return f"{self.user.username} {self.produit.name} {self.quantite} {self.montant}"

class Cart(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, related_name="acheteur", on_delete=models.CASCADE)
	produit = models.ForeignKey(Produits, on_delete=models.CASCADE)
	quantite = models.PositiveIntegerField()
	amount = models.FloatField(null=True, blank=True)
	def __str__(self):
		return f"{self.user.username} a achete {self.produit.name} {self.quantity} pour {self.amount}"





