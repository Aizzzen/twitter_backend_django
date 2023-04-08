from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


# если надумаю переписать на вьюхи
# class UserPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if view.action == 'list':
#         # if view.action in ['list', 'retrieve']:
#             return True
#         elif view.action == 'create':
#             return request.user.is_authenticated
#             # return request.user.is_authenticated or request.user.is_admin
#         else:
#             return False
#
#     def has_object_permission(self, request, view, obj):
#         if not request.user.is_authenticated:
#             return False
#         elif view.action in ['update', 'partial_update', 'destroy']:
#             return obj.user == request.user
#             # return obj.user == request.user or request.user.is_admin
#         else:
#             return False
