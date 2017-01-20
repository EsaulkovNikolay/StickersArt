from pyramid.response import Response
from MyProject.myproject.views.base import environment

def Contacts_Page(request):
    return Response(environment.get_template('/contacts.html').render(head="Контакты"))