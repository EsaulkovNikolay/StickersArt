from pyramid.response import Response
from MyProject.myproject.views.base import environment

def Index_Page(request):
    return Response(environment.get_template('/index.html').render(head="STICKERS Atr Shop"))