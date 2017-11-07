from django.contrib.auth import get_user_model

from django.contrib.auth.models import User,Group


from rest_framework.serializers import (
    CharField,
    EmailField,
    ChoiceField,
    HyperlinkedIdentityField,
    HyperlinkedModelSerializer,
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
    choices = (('Developer',"Developer"),('Team_leader',"Team_leader"),('Project_manager',"Project_manager"))
    emp_role= ChoiceField(choices)
    choices_report = (('Team_leader',"Team_leader"),('Project_manager',"Project_manager"))
    emp_report=ChoiceField(choices_report)
    password1 = CharField(label='password',style={'input_type': 'password'},write_only=True)
    password2 = CharField(label='Confirm password',style={'input_type': 'password'},write_only=True)
    class Meta:
        model = EmployeeEntryData
        fields = [
            'emp_email',
            'emp_code',
            'emp_datejoin',
            'emp_role',
            'emp_report',
            'password1',
            'password2',
        ]
        # extra_kwargs = {"emp_email":{"read_only":True}}
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
        # print(validated_data['emp_role'])
        username = validated_data['emp_email']
        email = validated_data['emp_email']
        groups = validated_data['emp_role']
        password = validated_data['password1']
        emp_code = validated_data['emp_code']
        emp_role = validated_data['emp_role']
        emp_report = validated_data['emp_report']
        emp_datejoin = validated_data['emp_datejoin']
        print('test')
        user_obj = User(
                username = username,
                email = email,
            )
        user_obj.save()
        users_group = Group.objects.get(name=groups)
        print(users_group)
        user_obj.groups = [users_group]
        print(user_obj)
        users_report = Group.objects.get(name=emp_report)

        employee_obj = EmployeeEntryData(
            emp_email = email,
            emp_code = emp_code,
            emp_role = users_group,
            emp_report = users_report,
            emp_datejoin = emp_datejoin,
        )
        print(employee_obj)
        user_obj.set_password(password)
        employee_obj.save()
        user_obj.save()
        return validated_data



class UserLoginSerializer(HyperlinkedModelSerializer):
    token = CharField(allow_blank=True,read_only=True)
    username = CharField()
    password = CharField(style={'input_type': 'password'},write_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',
        ]

    def validate(self, data):
        print(data)
        return data
