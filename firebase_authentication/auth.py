import firebase_admin
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from firebase_admin import auth
from firebase_admin import credentials
from rest_framework import authentication
from rest_framework import exceptions
from firebase_authentication.exceptions import FirebaseError

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "drf-firebase-5adb8",
  "private_key_id": "028bb5f891f9ae66b9a1c95a1f1ec6fc7b4a8731",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCgCi/q/lwrgddc\nSOf2uXsfTWqsPV53DRKz/RrXmNsd2pHbaS7DViM8ij/8iwNN0x0362SFG+UaSIGl\nJcacMCmS1RChQepHs0dTi33xmNl0yFAP4ci+wZsL0NKS9nfLoRITrcGvsGkz6lzi\nllbxxlo/dfhyzkHGpYau2++QXi9A5J0cyMrpJF3PmEB9G5M0Jvxt86z9TIbJGwql\ny5jbRLEhxDIDiDWIG90/xHNYa0KtGhjzIbnmjx5OXAtEx9y8VT8u/bJu7z0xffoo\nPrwMyq8R7pDXomnKpsRrF2CrvSGWL464lq7xmbv99HkqQqVaPPdaDDBZdOaYbbIB\nbPdN6HlfAgMBAAECggEAAesNVvo0fZsBS0xeZ2EiviXN5QGZS8D+2+RpOXNOEQYJ\nIIGau2Gha3zWtn6uC/U/UOfD3SqP7Og4kZOp1T5oiSd/mwcwuSpHbRNrb4Ve+dza\nxM32e37Tjmky1OsaVXj5P/4hp6rsH+Cru1WE9kHj3AXcc/fP5wMd4aOmM+tFEriF\n5UAQQjgs/OCqyV21DJZgZ8G83hWhywHGuXwB1FhTtGm0eR+dYMYU/ACzMy0NK4i7\n3Ia3SJkshNLCPHwZX/86AL2fCNpqKa5Aac7vCNOD729Chp/yVg/M5mlZ7IxOtr6Q\nmF+Um7NztpKfPGkdo8ZyOaQ6SLUmks93embgL7J6kQKBgQDNvRzzsLeQywo1qa+N\n6//DDOYt2V1FsM4WjNvpEIz0WtBevx5OxR/pT+GeSjznUvMvNucVGbdIk9n22l+P\n7AI5nA6NPUFMl/iYNetQ/upbqOTK6fot2c14xCHIODROSH6KdXyfB9YPP/hk51Ul\nqVsHTVjHqCOMKki4McN8XuhxrwKBgQDHIxDedgr2EJAbb7JH/yyannCIKSY1pJS9\nlgJS9N8n7CKhS+GCQXL83zRn6rz9yfgt7ZQqzvmw5udq3VfjMEVVbo4ZJNKZY3LG\neCkZ+0iH5cwG0ko5AUM6T18UfeNXmtczNn9DJtowufbtTg6P29/RtjAXudAKG1nX\neIeOoJDPUQKBgA6Cfd454lhV2Xx7YSQzNrB84mbtY4ScuYwhlwjS3/4DwZpNBEgt\n4thDh/fv6GewE/KKfrWgQKrfsomUURUHYgjKFsSjQ02xkhi6BMSLld+tA6XD5p8B\nM1qHCpLiU94JgtMlAgr9NH2S12PWZMzpKsBTFiXOl+M0wDgtWkoVL3OFAoGBAJq8\n38XNefT8p835/FG/sfwvs4fKWduDGOU8pG+rwZ+2+K3XVdMuYlimZIV/PP4EK+oc\nW27sR8+zjQ1YE4wBHU8mShq1p0Pzp+Maye1bel/HK8P9Mhmbpo6v0FUPAVI4ipJL\n/ZXDofYM+xgo+F3G3+OIK1S0WTkRSb2J9ePZVs0RAoGBAJ7ASgnbp2bQ1B1lQcoc\nrBzSfCfQOv9qB8ZuE3fv6Qe2v/NixYNlkQo/nOlF+vEXLnb+k/ztFYNskcjtZtk8\nh2J6wNc2z7B9oWa7295m1oZ4gU1KC/vvqpn64jZ3zOSfNB12r8EI9nhXaDddoRGS\n39KWxHX2ppxtd1HYYLhDQUsv\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-bssok@drf-firebase-5adb8.iam.gserviceaccount.com",
  "client_id": "114737952820405636430",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-bssok%40drf-firebase-5adb8.iam.gserviceaccount.com"
})

default_app = firebase_admin.initialize_app(cred)

class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise exceptions.AuthenticationFailed("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None

        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise exceptions.AuthenticationFailed("Invalid auth token")

        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()

        user = User.objects.get(id=1)
        return (user, None)