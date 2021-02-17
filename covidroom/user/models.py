from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CustomUser(models.Model):
    """ Serializer for User Model """
    super(User)

    # class Meta:
    #     model = User
    #     fields = ['id', 'username', 'password']

    # user list api will not return password
    # extra_kwargs = {'password': {
    #     'write_only': True,
    #     'required': True
    # }}

    def create(self, validated_data):
        # the password will be hashed  in the dabase for every registration
        user = User.objects.create_user(**validated_data)

        # New token will be generated on every registration
        # Token.objects.create(user=user)
        return user
