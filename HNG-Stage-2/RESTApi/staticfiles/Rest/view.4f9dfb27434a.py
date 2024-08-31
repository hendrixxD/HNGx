def get_object(self):
        # id = self.kwargs.get('user_id')
        parameter = self.kwargs.get('parameter')
        
        # Check if the name is an integer
        try:
            # Check if the parameter is an integer
            if parameter.isdigit():
                return Person.objects.get(id=parameter)
            else:
                return Person.objects.get(name=parameter)
        except Person.DoesNotExist:
            # Handle the case when the person does not exist
            raise generics.NotFound(f"Person with parameter '{parameter}' does not exist.")
        except Exception as e:
            # Handle other exceptions, if any
            print(f"Error: {e}")
        

    def put(self, request, *args, **kwargs):
        # Implement update logic here
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        # Implement delete logic here
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)