from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_model = get_user_model()
        jwt_auth = JWTAuthentication()

        # Check authorization header for a JWT token
        auth_header = request.headers.get("Authorization", "")
        if auth_header.startswith("Bearer "):
            token = auth_header.split(" ")
            try:
                # Validate the token
                validated_token = jwt_auth.get_validated_token(token)
                
                # Extract the user information from the token
                user_id = validated_token["user_id"]

                # Fetch the user object
                user = user_model.objects.get(id=user_id)

                # Add the user object to the request
                request.user = user
            except:
                pass

            response = self.get_response(request)
            return response