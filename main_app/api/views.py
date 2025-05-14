from rest_framework.views import APIView

from main_app.models import Keychain, Tag

from .serializers import KeychainSerializer, KeychainImageSerializer

from rest_framework.response import Response 

from rest_framework import status 

from rest_framework.decorators import api_view, permission_classes

from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated,AllowAny

from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.password_validation import validate_password

from django.core.exceptions import ValidationError


class KeychainListAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        # step 1: get all cats form the DB
        # step 2: serialize our cats into JSON
        # step 3: return the serialized cats in the HTTP response
        # keychains=Keychain.objects.all() 
        keychains=Keychain.objects.filter(user=request.user)
        serializer=KeychainSerializer(keychains,many=True) 
        return Response(serializer.data) 
        
    def post(self,request):
        serializer=KeychainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            

# Add tag to keychain using function based API view
@api_view(['POST'])
@permission_classes({IsAuthenticated})
def add_tag_to_keychain(request,keychain_id,tag_id):
    try:
        keychain=Keychain.objects.get(pk=keychain_id)
        tag=Tag.objects.get(pk=tag_id)
        
        keychain.tags.add(tag)
        return Response({"message":"Tag was added to the keychain!"},status=status.HTTP_200_OK)

    except Keychain.DoesNotExist:
        return Response({"error": "The keychain does not exist"},status=status.HTTP_400_BAD_REQUEST) 
    except Tag.DoesNotExist:
        return Response({"error": "The Tag does not exist"},status=status.HTTP_400_BAD_REQUEST) 
    except:
        return Response({"error": "Something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR) 

# Remove tag from keychain using function based API view
@api_view(['POST'])
@permission_classes({IsAuthenticated})
def remove_tag_from_keychain(request,keychain_id,tag_id):
    try:
        keychain=Keychain.objects.get(pk=keychain_id)
        tag=Tag.objects.get(pk=tag_id)
        
        if keychain.tags.filter(id=tag_id).exists():
            keychain.tags.remove(tag)
            return Response({"message":"Tag was removed from the keychain!"},status=status.HTTP_200_OK)
        else:  
            return Response({'message': 'Tag was already removed or not associated!'}, status=404)       
    except Keychain.DoesNotExist:
        return Response({"error": "The keychain does not exist"},status=status.HTTP_400_BAD_REQUEST) 
    except Tag.DoesNotExist:
        return Response({"error": "The tag does not exist"},status=status.HTTP_400_BAD_REQUEST) 
    except:
        return Response({"error": "Something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR) 

# Add image to keychain using class based API view
class AddImageToKeychainAPI(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request, keychain_id):
        keychain = get_object_or_404(Keychain, pk=keychain_id)
        data = request.data.copy()
        data['keychain'] = keychain.id
        
        serializer = KeychainImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignUpView(APIView):
    permission_classes=[AllowAny] #allow anyone to create a new account
    def post(self,request):
        # get the user input
        username=(request.data.get("username"))
        email=(request.data.get("email"))
        password=(request.data.get("password"))
        
        # validate the password (check if it is strong enough)
        try:
            validate_password(password)
            
        except ValidationError as err:
            return Response({"error":err.messages}, status=400)
            
        # create the new user
        user=User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        # generate refresh and access tokens
        tokens=RefreshToken.for_user(user) 
        return Response({
        "refresh":str(tokens),
        "access":str(tokens.access_token)
        },status=201)