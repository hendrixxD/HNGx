    def create(self, validated_data):
        # The create method returns a success message with a status code of 201
        # (Created) when a new person object is created successfully.
        instance = super().create(validated_data)
        return {"message": "Person created successfully.", "status_code": 201}

    def update(self, instance, validated_data):
        # The update method returns a confirmation message with a status code of 200
        # (OK) when a person object is updated successfully.
        instance = super().update(instance, validated_data)
        return {"message": "Person updated successfully.", "status_code": 200}

    def delete(self, instance):
        # The delete method deletes the person object and returns a confirmation message with a status code of 204
        # (No Content) when a person object is deleted successfully.
        instance.delete()
        return {"message": "Person deleted successfully.", "status_code": 204}