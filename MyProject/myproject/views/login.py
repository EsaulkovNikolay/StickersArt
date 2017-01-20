from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget
from pyramid.response import Response
from MyProject.myproject.Security import hash_password,check_password,USERS
from MyProject.myproject.views.base import environment,dataBase

def Login_Page(request):
    if request.method=="POST":
        if len(request.params)>3:
            return Register(request)
        else:
            return Auth(request)
    else:
        return Response(environment.get_template("/registration.html"))

def Logout_Page(request):
    if request.method=="POST":
        headers = forget(request)
        return HTTPFound(location = '/', headers = headers)


def Register(request):
    conn = dataBase.engine.connect()
    if len(conn.execute(dataBase.Client_Table.select().where(
                    request.params["Email"]==dataBase.Client_Table.c.Email)).fetchall())==0:
        key=conn.execute("select max(Client_ID) from Client").fetchone()
        if key[0]==None:
            key=0
        else:
            key=key[0]+1
        args=[key,request.params["First_Name"],request.params["Last_Name"],
              request.params["Email"],request.params["Contact_Phone"],request.params["Address"],
              hash_password(request.params["Password"])]
        conn.execute(dataBase.Client_Table.insert(args))
        headers = remember(request,key)
        return HTTPFound(location = '/', headers = headers)



def Auth(request):
    conn = dataBase.engine.connect()
    login=request.params["Email"]
    passwd=conn.execute(dataBase.Client_Table.select().where(dataBase.Client_Table.c.Email==login)).fetchone()
    if USERS.get(request.params['Email'])==request.params['Password']:
        headers = remember(request, 'admin')
        return HTTPFound(location = '/', headers = headers)
    if passwd!=None:
        passwd=passwd['Password']
        if check_password(hash_password(request.params["Password"]),passwd):
            headers = remember(request, login)
            return HTTPFound(location = '/', headers = headers)
    return Response(environment.get_template("/authorisation.html").render(error="<p>Неверно введен адрес "
                                      "электронной почты или пароль</p>"))
