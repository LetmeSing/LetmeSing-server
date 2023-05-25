from rest_framework import serializers
from .models import Member

# JWT를 이용한 회원가입 구현


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

    def create(self, validated_data):
        login_id = validated_data.get('login_id')
        nickname = validated_data.get('nickname')
        password = validated_data.get('password')
        user = Member(
            login_id=login_id,
            nickname=nickname
        )
        user.set_password(password)
        user.save()
        return user


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
