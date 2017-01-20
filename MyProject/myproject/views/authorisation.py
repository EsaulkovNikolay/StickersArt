from pyramid.response import Response
from MyProject.myproject.views.base import environment

def Auth_Page(request):
    return Response(environment.get_template('/authorisation.html').render(head="INDEX",link='<a href="/">Link</a>'))