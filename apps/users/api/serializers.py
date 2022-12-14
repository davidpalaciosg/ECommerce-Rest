from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = "__all__"
        fields = ['id','username','email','name','last_name', 'password', 'image']
    
    #Custom validation
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('La contraseña debe tener al menos 8 caracteres')
        #Password must contain at least one number, one uppercase letter and one lowercase letter
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError('La contraseña debe contener al menos un número')
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError('La contraseña debe contener al menos una letra mayúscula')
        if not any(char.islower() for char in value):
            raise serializers.ValidationError('La contraseña debe contener al menos una letra minúscula')
        if not any(not char.isalnum() for char in value):
            raise serializers.ValidationError('La contraseña debe contener al menos un caracter especial')
        return value
    
    #Create user from serializer
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
#Serializer to list User information
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','name','last_name', 'password']
        
#Serualizer to update User information
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'last_login']
        
#Serializer to update User password and email
class UserUpdatePasswordEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
    
    #Custom representation of a user, default shows all fields
    '''
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'email': instance.email,
            'name': instance.name,
            'last_name': instance.last_name,
        }
    '''