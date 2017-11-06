from rest_framework.serializers import (
    CharField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )


from accounts.api.serializers import UserDetailSerializer
from accounts.models import EmployeeEntryData



employee_detail_url = HyperlinkedIdentityField(
        view_name='employee-api:detail',
        lookup_field='pk'
        )

class EmployeeCreateUpdateSerializer(ModelSerializer):
    url = employee_detail_url
    username = UserDetailSerializer(read_only=True)
    class Meta:
        model = EmployeeEntryData
        fields = [
            'url',
            # 'id',
            'emp_code',
            'emp_email',
            'emp_datejoin',
            'emp_role',
            'emp_report',
        ]


class EmployeeDetailSerializer(ModelSerializer):
    url = employee_detail_url
    username = UserDetailSerializer(read_only=True)
    class Meta:
        model = EmployeeEntryData
        fields = [
            'url',
            'id',
            'username',
			'emp_code',
			'emp_email',
			'emp_datejoin',
			'emp_role',
			'emp_report',

        ]



class EmployeeListSerializer(ModelSerializer):
    url = employee_detail_url
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = EmployeeEntryData
        fields = [
            'url',
            'user',
            'emp_code',
            'emp_email',
            'emp_datejoin',
            'emp_role',
            'emp_report',
        ]



"""

from employee.models import EmployeeEntryData
from posts.api.serializers import PostDetailSerializer


data = {


}

obj = EmployeeEntryData.objects.get(id=2)
new_item = employeeDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)


"""
