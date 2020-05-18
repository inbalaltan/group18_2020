from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse
from django.http import HttpResponseForbidden


class RestrictStaffToAdminMiddleware(object):
    """
    A middleware that restricts staff members access to administration panels.
    """

    def process_request(self, request):
        if not hasattr(request, 'user'):
            raise ImproperlyConfigured(
                "Restrict staff to admin middleware requires the"
                " authentication middleware to be installed.  Edit your"
                " MIDDLEWARE_CLASSES setting to insert"
                " 'django.contrib.auth.middleware.AuthenticationMiddleware'"
                " before the RestrictStaffToAdminMiddleware class.")
        if request.user.is_staff:
            if not request.path.startswith(reverse('admin:index')):
                msg = u'Staff members cannot access the public site.'
                return HttpResponseForbidden(msg)