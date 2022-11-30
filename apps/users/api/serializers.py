from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
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