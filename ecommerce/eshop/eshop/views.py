from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from user.serializers import UserSerializerWithToken
# from rest_framework_simplejwt.state import token_backend

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
       
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)

    #     # Add custom claims
    #     token['username'] = user.username
        
    #     return token

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k,v in serializer.items():
            data[k] = v

        # data['username'] = self.user.username
        # data['email'] = self.user.email
        # data['mess'] = 'message'

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
