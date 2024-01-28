from django.http import HttpResponseForbidden
import re

class URLFilterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_patterns = [
            r'^/$',  # Home page URL
            r'^/add_student/$',  # URL for adding a student
            r'^/update_student/\d+/$',  # URL pattern for updating a student (with ID)
            r'^/delete_student/\d+/$',  # URL pattern for deleting a student (with ID)
        ]
        # Convert the patterns to regular expressions
        self.allowed_regex = [re.compile(pattern) for pattern in self.allowed_patterns]

    def __call__(self, request):
        # Check if the requested URL matches any of the allowed patterns
        if not any(regex.match(request.path) for regex in self.allowed_regex):
            # If the URL does not match any allowed pattern, return a forbidden response
            return HttpResponseForbidden("Access to this URL is not allowed.")
        
        # If the URL matches an allowed pattern, continue with the request
        response = self.get_response(request)
        return response
