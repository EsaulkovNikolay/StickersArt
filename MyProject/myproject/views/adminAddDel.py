from pyramid.response import Response
from MyProject.myproject.views.base import environment,dataBase
import os
import shutil

def Admin_Add_Del_Page(request):
    items=GetContent()
    return Response(environment.get_template('/adminAddDel.html').render(body=items))

def Add_Content(request):
    if request.method == "GET":
        return { 'username': request.authenticated_userid }
    else:
        if(request.POST['picture']) != "":
            filename = request.POST['picture'].filename
            input_file = request.POST["picture"].file
            file_path = os.path.join( 'static/images', filename)
            with open(file_path, 'wb') as output_file:
                shutil.copyfileobj(input_file, output_file)
        else:
            file_path = u"static/images/none.jpg"
        conn=dataBase.engine.connect()
        conn.execute(dataBase.Sticker_Table.insert().values(Picture="/"+file_path))

        return Admin_Add_Del_Page(request)

def Del_Content(request):
    if request.method=="POST":
        sticker=request.params['hidden']
        conn=dataBase.engine.connect()
        conn.execute(dataBase.Sticker_Table.delete().where(dataBase.Sticker_Table.c.Sticker_ID==sticker))
    return Admin_Add_Del_Page(request)

def GetContent():
    content="<table><tr>"
    item="<th><form action='adminDel.html' method='POST'> <img src='{0}' height=300px width=200px >" \
         "<br><input type='hidden' name='hidden' value='{1}'><input type='submit' value='Удалить'>" \
         "</form><th>"
    conn=dataBase.engine.connect()
    res=conn.execute(dataBase.Sticker_Table.select()).fetchall()
    i=0
    for elem in res:
        content+=item.format(elem.Picture,elem.Sticker_ID)
        if (i+1)%2==0:
            content+="</tr><tr> "
        i+=1
    return content+"</table>"