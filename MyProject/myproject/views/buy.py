from pyramid.response import Response
from MyProject.myproject.views.base import environment,dataBase
import datetime

def Buy_Page(request):
    if request.method=="POST":
        conn=dataBase.engine.connect()
        user=request.authenticated_userid

        book=conn.execute(dataBase.Cheque_Table.select().where(dataBase.Cheque_Table.c.Complited==False).where(
            not dataBase.Cheque_Table.c.Client_ID==user
        )).fetchone().Book_ID


        conn.execute(dataBase.Cheque_Table.update().where(dataBase.Cheque_Table.c.Client_ID==user
             ).where(dataBase.Cheque_Table.c.Complited==False).values(Complited=True,Date=datetime.datetime.now()))

        material=request.POST['mat']
        conn.execute(dataBase.StickerBook_Table.update().where(dataBase.StickerBook_Table.c.Book_ID==book).values(
            Material=material
        ))

        price=conn.execute(dataBase.Material_Table.select().where(dataBase.Material_Table.c.Material_ID==material)
                           ).fetchone()['Price']
        listCapasity=len(conn.execute(dataBase.Stickers_In_StickerBook_Table.select().where(
            dataBase.Stickers_In_StickerBook_Table.c.Book_ID==book)).fetchall())
        resultPrice=price*listCapasity
        conn.execute(dataBase.Price_Table.insert().values(Price=resultPrice,Book_ID=book))

    return Response(environment.get_template('/buy.html').render(body="<br>Стоимость: {}р<br>".format(resultPrice)))