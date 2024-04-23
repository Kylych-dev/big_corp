# authentication/permissions.py

from rest_framework.permissions import BasePermission

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'user'

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'manager'

# class IsServiceEngineer(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.role == 'service_engineer'



'''

# authentication/permissions.py

from rest_framework.permissions import BasePermission

class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'client'

class IsHeadEngineer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'head_engineer'

class IsServiceEngineer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'service_engineer'


in views.py 

from rest_framework.views import APIView
from authentication.permissions import IsClient, IsHeadEngineer, IsServiceEngineer

class TicketSubmissionView(APIView):
    permission_classes = [IsClient]

    def post(self, request):
        # Your ticket submission logic here
        pass

class AssignmentView(APIView):
    permission_classes = [IsHeadEngineer]

    def put(self, request, ticket_id):
        # Your assignment logic here
        pass

class CompletionView(APIView):
    permission_classes = [IsServiceEngineer]

    def put(self, request, ticket_id):
        # Your completion logic here
        pass

'''