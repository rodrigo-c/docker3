from django.contrib.auth.models import User

from app.views import login_ldap


class LDAPBackend(object):

    def authenticate(self, request, username=None, password=None):
        login_valid = login_ldap(username, password)
        if login_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
