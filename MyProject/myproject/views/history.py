from pyramid.response import Response
from MyProject.myproject.views.base import environment

def History_Page(request):
    return Response(environment.get_template('/history.html').render(head="INDEX",link='<a href="/">Link</a>'))