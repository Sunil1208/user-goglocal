from django.shortcuts import render
from .models import CustomUser
from django.http import HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

#login route /api/user/login
def login(req):
    # get the username and password
    req_json = req.json()
    username, password = req_json.username, req_json.password
    user = CustomUser.objects.get(username=username, password=password)
    response_data = {
        "status": -1,
        "data": {},
        "message": ""
    }
    if not user:
        response_data["message"] = "Invalid credentials"
    refresh = RefreshToken.for_user(user)
    response_data["data"] = {
        "access_token": str(refresh.access_token),
    }
    return HttpResponse(content=response_data)
    
    # verify the login, if login is success, create a new jwt token and return it in the response



# profile route   /api/user/profile



def profile():
    # requires jwt token for access
    # return the username and password decoded from the jwt
    pass