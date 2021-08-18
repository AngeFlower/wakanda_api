from django.contrib import admin
from .models import *

admin.site.register(Utilisateur)
admin.site.register(Produits)
admin.site.register(Categorie)
admin.site.register(Marque)
admin.site.register(Vente)
admin.site.register(Achat)
