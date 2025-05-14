from rest_framework import serializers
from main_app.models import Keychain, Tag, KeychainImage

class KeychainSerializer(serializers.ModelSerializer):
    keychains=serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        allow_empty=True,
        required=False
    )
    class Meta:
        model=Keychain
        fields="__all__" 
        
class KeychainImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeychainImage
        fields="__all__"