from django.urls import path
from .views import KeychainListView, CreateKeychainView, UpdateKeychainView,DeleteKeychainView,keychain_detail_view,add_image,add_tag_to_keychain, remove_tag_from_keychain, welcome, signup

# I used this resource: https://forum.djangoproject.com/t/displaying-uploaded-files/11888
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("all-keychains/", KeychainListView.as_view(), name="keychain_list"),
    path("all-keychains/<int:keychain_id>/",keychain_detail_view, name="keychain_detail"),
    path("all-keychains/add/", CreateKeychainView.as_view(), name="keychain_add"),
    path("all-keychains/<int:pk>/update", UpdateKeychainView.as_view(), name="keychain_update"),
    path("all-keychains/<int:pk>/delete", DeleteKeychainView.as_view(),name="keychain_delete"),
    path('all-keychains/<int:keychain_id>/add-image',add_image, name="add-image"),
    path('all-keychains/<int:keychain_id>/add-tag/<int:tag_id>', add_tag_to_keychain, name='add_tag_to_keychain'),
    path('all-keychains/<int:keychain_id>/remove-tag/<int:tag_id>', remove_tag_from_keychain, name='remove_tag_from_keychain'),
    path('', welcome, name='welcome'),
    path('accounts/signup/',signup, name='signup')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)