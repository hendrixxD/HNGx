from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # fields = '__all__'
        fields = ['id', 'name', 'age', 'email']
        
    def validate_name(self, value):
        """perform edge operations on Person Object
        """
        # Trim leading and trailing whitespace
        value = value.strip()
        
        if not value:
            # This ensures that empty names are not allowed.
            raise serializers.ValidationError("Name cannot be empty.")
        
        # Check if this is an update operation
        if self.instance:
            # If updating, it's allowed to keep the same name
            if self.instance.name.lower() == value.lower():
                return value
            
        # Check for duplicate names (case-insensitive)
        # This ensures that names like "John" and " John " are considered the same.
        if Person.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("A person with this name already exists.")
        return value
