from django.urls import path
from .views import KeychainListAPI, add_tag_to_keychain, remove_tag_from_keychain, AddImageToKeychainAPI,SignUpView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    # user the plural. so the link will be like this http://127.0.0.1:8000/api/cats/

    path("keychains/",KeychainListAPI.as_view(),name="api-keychains"),
    path('keychains/<int:keychain_id>/add-tag/<int:tag_id>/', add_tag_to_keychain, name="api_add_tag_to_keychain"),
    path('keychains/<int:keychain_id>/remove-tag/<int:tag_id>/', remove_tag_from_keychain, name="api_remove_tag_from_keychain"),
    path('keychains/<int:keychain_id>/add-image/', AddImageToKeychainAPI.as_view(), name='add_image_to_keychain'),
    path("token/",TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup')
]
# http://127.0.0.1:8000/api/keychains/?/add-image