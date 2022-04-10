from rest_framework import status
from rest_framework.exceptions import APIException


class FirebaseError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "The user provided with the auth token is not a valid Firebase user, it has no Firebase UID"
    default_code = "no_firebase_uid"