from pyramid.response import Response
from MyProject.myproject.views.base import environment,dataBase
from sqlalchemy import join

def Admin_Look_Page(request):
    items=GetCheques()
    return Response(environment.get_template('/adminLook.html').render(body=items))

def GetCheques():
    conn=dataBase.engine.connect()
    res=conn.execute(join(dataBase.Cheque_Table,dataBase.Price_Table,
                          dataBase.Price_Table.c.Book_ID==dataBase.Cheque_Table.c.Book_ID
                          ).select().where(dataBase.Cheque_Table.c.Complited==True).reduce_columns()).fetchall()
    string=""

    for elem in res:
        string+="Cheque_ID={0} Client_ID={1} Book_ID={2} Quantity={3} Date={4} Price={5}<br>".format(elem.Cheque_ID,elem.Client_ID,
            elem.Book_ID,elem.Quantity,elem.Date,elem.Price)
    return string
