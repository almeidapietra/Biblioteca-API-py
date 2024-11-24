from rest_framework import permissions

class IsCollectorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Permite edição apenas se o usuário for o colecionador
        return obj.colecionador == request.user