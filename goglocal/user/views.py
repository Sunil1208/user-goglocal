from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        response = {
             "data": {},
             "status": -1,
             "message": ""
        }

        if user is not None:
            refresh = RefreshToken.for_user(user)
            response['data'] = {
                 "access_token": str(refresh.access_token),
            }
            response["status"] = 1
            return Response(response, status=200)
        else:
            response["message"] = "Invalid Credentials"
            return Response(response, status=400)
        
class UserProfileView(APIView):
       permission_classes = [IsAuthenticated]

       def get(self, request):
           user = request.user
           response = {
                "data": {},
                "status": -1,
                "message": "User not found"
           }
           print("USER IS ", user, type(user))
           print(".....")
           print(user.username)
           if user:
                response["data"] = {
                     "first_name": user.first_name,
                     "last_name": user.last_name
                }
                response["status"] = 1
                response["message"] = ""
           return Response(response)