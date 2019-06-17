from _testcapi import raise_exception

from django.core.exceptions import PermissionDenied


class PostCreateRequiredMixin:
    """
    Only work for post method
    """
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            perm = 'posts.add_post'
            if isinstance(perm, str):
                perms = (perm,)
            else:
                perms = perm
            # First check if the user has the permission (even anon users)
            print(request.user.get_all_permissions())
            if not request.user.has_perms(perms):
                raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)
