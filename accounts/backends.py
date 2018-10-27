from django.contrib.auth.models import User

class EmailAuth:
    """
    Authenticate user on email and password
    """
    def authenticate(self, username=None, password=None):
        """
        Get User from email and check password
        """
        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user
            return None

        except User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        """
        Return user instance
        """
        try:
            user = User.objects.get(pk=user_id)

            if user:
                return user
            return None

        except User.DoesNotExist:
            return None
