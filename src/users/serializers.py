from users.models import Person, Group
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

class PersonSerializer(serializers.ModelSerializer):
    # Virtual field
    checked_in = serializers.BooleanField()
    # first_name = serializers.CharField(read_only=True)
    # last_name  = serializers.CharField(read_only=True)
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'is_guest', 'email', 'checked_in', 'group')

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.checked_in = validated_data.get('checked_in', instance.checked_in)
        instance.save()
        return instance

    def create(self, validated_data):

        # Create the person instance
        person = Person.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_guest=True
        )
        person.save()

        # We have to add the checked_in afterward
        person.checked_in = True
        person.save()
        return person

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
