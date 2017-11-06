from rest_framework.serializers import (
    CharField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )

from accounts.api.serializers import UserDetailSerializer
from accounts.models import LeaveModel

leave_detail_url = HyperlinkedIdentityField(
        view_name='employee-api:Leave_list',
        lookup_field='pk'
        )

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
			emp_leavedate = validated_data['emp_leavedate']
			# emp_leavesanction = validated_data['emp_leavesanction']

			employee_obj = LeaveModel(
    		emp_LeaveUser = self.context['request'].user,
    		emp_leavedate = emp_leavedate,
    		emp_leavesanction = False,
				)
			employee_obj.save()
			return validated_data

class EmployeeLeaveListSerializer(ModelSerializer):
		# url = leave_detail_url
		# user = UserDetailSerializer(read_only=True)
		class Meta:
			model = LeaveModel
			fields = [
			# 'user',
			'emp_LeaveUser',
			'emp_leavedate',
			'emp_leavesanction',
			]
