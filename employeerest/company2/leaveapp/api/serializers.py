from rest_framework.serializers import (
    CharField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ReadOnlyField,
	ValidationError
    )

from accounts.api.serializers import UserDetailSerializer
from accounts.models import LeaveModel
from django.contrib.auth.models import User,Group

#
# leave_detail_url = HyperlinkedIdentityField(
#         view_name='employee-api:Leave_sanction',
#         lookup_field='id'
#         )

class EmployeeLeaveSerializer(ModelSerializer):
	emp_LeaveUser = CharField(read_only=True)
	emp_leavesanction = CharField(read_only=True)
	class Meta:
		model = LeaveModel
		fields = [
			'emp_LeaveUser',
			'emp_leavedate',
			'emp_leavesanction',
		]
	def create(self, validated_data):
			# emp_LeaveUser = validated_data['emp_LeaveUser']
			print(self.context['request'].user)
			emp_leavedate = validated_data['emp_leavedate']
			print(str(emp_leavedate))
			emp_LeaveUser = self.context['request'].user
			print(emp_LeaveUser)
			name = User.objects.get(username=emp_LeaveUser)
			print(name)
			print("asdas")
			datecheck =LeaveModel.objects.filter(emp_LeaveUser=name).filter(emp_leavedate=emp_leavedate)
			print(datecheck)
			if(datecheck):
				raise ValidationError("The date {} already applied".format(emp_leavedate))
			else:
				employee_obj = LeaveModel(
    			emp_LeaveUser = self.context['request'].user,
    			emp_leavedate = emp_leavedate,
    			emp_leavesanction = False,
					)
				employee_obj.save()
			return validated_data

class EmployeeLeaveListSerializer(ModelSerializer):
		# url = leave_detail_url
		user = ReadOnlyField(source='emp_LeaveUser.username')
		class Meta:
			model = LeaveModel
			fields = [
			# 'url',
			'id',
			'user',
			'emp_LeaveUser',
			'emp_leavedate',
			'emp_leavesanction',
			]

			extra_kwargs = {'emp_LeaveUser':{'read_only':True},'emp_leavedate': {'read_only': True},'emp_LeaveUser':{'read_only':True}}
