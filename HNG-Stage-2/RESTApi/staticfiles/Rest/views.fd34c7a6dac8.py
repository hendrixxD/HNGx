from .models import Person
from django.shortcuts import render
from .serializers import PersonSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404


# Create your views here.
class PersonListCreateView(generics.ListCreateAPIView):
    """creates a new person object
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
    def create(self, validated_data):
        # The create method returns a success message with a status code of 201
        # (Created) when a new person object is created successfully.
        instance = super().create(validated_data)
        return Response({"message": "created successfully.", 
                         "status_code": 201})


class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Fetch details of a person
        Updates details of a person
        Deletes a person
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_url_kwarg = 'parameter'  # Use 'parameter' as the lookup URL keyword argument
    # lookup_field = 'id'
    # lookup_field = 'name'
    
    
    def get_object(self):
        parameter = self.kwargs.get('parameter')
        try:
            if isinstance(parameter, int):
                # Try to lookup by id (integer)
                return Person.objects.get(id=parameter)
            else:
                # Try to lookup by name (string)
                return Person.objects.get(name=parameter)
        except Person.DoesNotExist:
            raise NotFound("Person not found.")
            
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "updated successfully.",
             "status_code": status.HTTP_200_OK}
        )
        
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response(
            {"message": "deleted successfully.", "status_code": status.HTTP_204_NO_CONTENT}
        )