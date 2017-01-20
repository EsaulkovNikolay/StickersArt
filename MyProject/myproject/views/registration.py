from pyramid.response import Response
from MyProject.myproject.views.base import environment

def Register_Page(request):
    return Response(environment.get_template('/registration.html').render(head="STICKERS Atr Shop"))

