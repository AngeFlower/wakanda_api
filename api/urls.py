from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView

router = DefaultRouter()
router.register('produit',ProduitsViewSet,basename='produit')
router.register('utilisateur',UtilisateurViewSet,basename='utilisateur')
router.register('categorie',CategorieViewSet,basename='categorie')
router.register('marque',MarqueViewSet,basename='marque')
router.register('group',GroupViewSet,basename='group')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterView.as_view()),
    path('api_auth', include('rest_framework.urls')),

]