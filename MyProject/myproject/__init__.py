import os
from wsgiref.simple_server import make_server
from MyProject.myproject.shema import Data_Base
from MyProject.myproject.Security import MyFactory
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from MyProject.myproject.views import (
    index, bin,catalog,history,contacts,registration,login, authorisation,buy,adminLook,adminAddDel
    )

def main(settings=None):
    configuration=Configurator(root_factory=MyFactory,settings=settings)
    configuration.add_static_view('/static','static',cache_max_age=3600)

    authn_policy = AuthTktAuthenticationPolicy('sosecret', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    configuration.set_authentication_policy(authn_policy)
    configuration.set_authorization_policy(authz_policy)

    configuration.add_route('registration','/registration.html')
    configuration.add_view(registration.Register_Page,route_name='registration')

    configuration.add_route('index','/')
    configuration.add_view(index.Index_Page,route_name='index')

    configuration.add_route('authorisation','/authorisation.html')
    configuration.add_view(authorisation.Auth_Page, route_name='authorisation')

    configuration.add_route('bin','/bin.html')
    configuration.add_view(bin.Bin_Page,route_name='bin')

    configuration.add_route('catalog','/catalog.html')
    configuration.add_view(catalog.Catalog_Page,route_name='catalog')

    configuration.add_route('history','/history.html')
    configuration.add_view(history.History_Page,route_name='history')

    configuration.add_route('contacts','/contacts.html')
    configuration.add_view(contacts.Contacts_Page,route_name='contacts')

    configuration.add_route('login','/login.html')
    configuration.add_view(login.Login_Page,route_name='login')

    configuration.add_route('add_list','/add_list.html')
    configuration.add_view(bin.Add_List,route_name='add_list')

    configuration.add_route('buy','/buy.html')
    configuration.add_view(buy.Buy_Page,route_name='buy')

    configuration.add_route('logout','/logout.html')
    configuration.add_view(login.Logout_Page,route_name='logout')

    configuration.add_route('delItem','/delItem/{id}')
    configuration.add_view(bin.DelItem,route_name='delItem')

    configuration.add_route("adminEditTableEdit", "/adminEditTableEdit/{id}")
    configuration.add_view(bin.Add_List,route_name="adminEditTableEdit")

    configuration.add_route("adminLook", "/adminLook.html")
    configuration.add_view(adminLook.Admin_Look_Page,route_name="adminLook",permission='admin')

    configuration.add_route("adminAddDel", "/adminAddDel.html")
    configuration.add_view(adminAddDel.Admin_Add_Del_Page,route_name="adminAddDel",permission='admin')

    configuration.add_route("adminAdd", "/adminAdd.html")
    configuration.add_view(adminAddDel.Add_Content,route_name="adminAdd",permission='admin')

    configuration.add_route("adminDel", "/adminDel.html")
    configuration.add_view(adminAddDel.Del_Content,route_name="adminDel",permission='admin')

    return configuration.make_wsgi_app()



if __name__ == '__main__':
    app = main()
    server = make_server('localhost',8000,app)
    print("Serving localhost on port 8000...")
    server.serve_forever()