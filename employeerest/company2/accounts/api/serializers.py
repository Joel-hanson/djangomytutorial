from django.contrib.auth import get_user_model



from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )

from accounts.models import EmployeeEntryData
User = get_user_model()


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
			'groups',
        ]

class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    password1 = CharField(label='password',style={'input_type': 'password'},write_only=True)
    password2 = CharField(label='Confirm password',style={'input_type': 'password'},write_only=True)
    class Meta:
        model = EmployeeEntryData
        fields = [
            'email',
            'password1',
            'password2',
			'groups'
            'emp_email',
            'emp_code',
            'emp_datejoin',
            # 'emp_role',
            'emp_report',
        ]
        extra_kwargs = {"emp_email":{"read_only":True}}
    def validate(self, data):
        return data
    def validate_email(self, value):
        data = self.get_initial()
        email = data.get("email")
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        return value
    def validate_password1(self, value):
        data = self.get_initial()
        password1 = data.get("password1")
        password2 = value
        if password1 != password2:
            raise ValidationError("passwords must match.")
        return value
    def create(self, validated_data):
        username = validated_data['email']
        email = validated_data['email']
        groups = validated_data['groups']
        password = validated_data['password1']
        emp_code = validated_data['emp_code']
        emp_role = validated_data['groups']
        emp_report = validated_data['emp_report']
        emp_datejoin = validated_data['emp_datejoin']
        print('test')
        user_obj = User(
                username = username,
                email = email,
				groups=groups
            )
        print(user_obj)
        print('as')
        employee_obj = EmployeeEntryData(
            emp_email = email,
            emp_code = emp_code,
            emp_role = emp_role,
            emp_report = emp_report,
            emp_datejoin = emp_datejoin,
        )
        print(employee_obj)
        user_obj.set_password(password)
        employee_obj.save()
        user_obj.save()
        return validated_data



class UserLoginSerializer(ModelSerializer):
    csrfmiddlewaretoken = CharField(read_only=True)
    username = CharField()
    email = EmailField(label='Email Address')
    password = CharField(style={'input_type': 'password'},write_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'csrfmiddlewaretoken',
        ]

    def validate(self, data):
        print(data)
        return data
