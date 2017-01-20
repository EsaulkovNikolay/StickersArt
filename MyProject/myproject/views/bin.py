from pyramid.response import Response
from MyProject.myproject.views.base import environment,dataBase
from MyProject.myproject.views.authorisation import Auth_Page
from sqlalchemy import select

def Bin_Page(request):
    if request.authenticated_userid==None:
        return Auth_Page(request)
    items=GenerateBinItems(request)
    return Response(environment.get_template('/bin.html').render(body=items))

def Add_List(request):
    if request.authenticated_userid==None:
        return Auth_Page(request)
    Add_Item(request)
    items=GenerateBinItems(request)
    return Response(environment.get_template('/bin.html').render(body=items))

#Добавление товара к заказу
def Add_Item(request):
    user=request.authenticated_userid
    conn=dataBase.engine.connect()
    sticker=request.matchdict['id']
    if  user!=None and request.method=="POST":

        book=conn.execute(dataBase.Cheque_Table.select().where(dataBase.Cheque_Table.c.Complited==False).where(
            dataBase.Cheque_Table.c.Client_ID==user)).fetchone()

        if book==None:
            book=conn.execute("select max(Book_ID) from Stickerbook").fetchone()[0]
            if book==None:
                book=1
            else:
                book+=1
            conn.execute(dataBase.StickerBook_Table.insert().values(Book_ID=book))
            conn.execute(dataBase.Cheque_Table.insert().values(Client_ID=user,Quantity=1,
                                                               Complited=False,Book_ID=book))
            conn.execute(dataBase.Stickers_In_StickerBook_Table.insert().values(Book_ID=book,Sticker_ID=sticker))
        else:
            book=book['Book_ID']
            conn.execute(dataBase.Stickers_In_StickerBook_Table.insert().values(Book_ID=book,Sticker_ID=sticker))

#Поиск выбранных пользователем листов
def GenerateBinItems(request):
    conn=dataBase.engine.connect()
    user=request.authenticated_userid

    item=" <div display:table-cell>  " \
         "<img margin=5% height=10% width=40% src='{0}'><br> <a href='/delItem/{1}'>Удалить</a></div> "
    result=conn.execute(select([dataBase.Sticker_Table.c.Sticker_ID,dataBase.Sticker_Table.c.Picture,
                                dataBase.Cheque_Table.c.Complited,dataBase.Cheque_Table.c.Client_ID]).select_from(
        dataBase.Cheque_Table.join(dataBase.Stickers_In_StickerBook_Table,
        dataBase.Stickers_In_StickerBook_Table.c.Book_ID==dataBase.Cheque_Table.c.Book_ID ).join(
        dataBase.Sticker_Table,dataBase.Sticker_Table.c.Sticker_ID==dataBase.Stickers_In_StickerBook_Table.c.Sticker_ID)).where(
        dataBase.Cheque_Table.c.Client_ID==user).where(dataBase.Cheque_Table.c.Complited==False)
    ).fetchall()


    k=0
    for i in range(0,len(result)):
        if user==str(result[i-k].Client_ID) and not result[i-k].Complited:
            continue
        else:
            result.pop(i-k)
            k+=1
    blocks=""

    if len(result)==0:
        blocks="<p>Корзина пуста</p><p>Перейти в<a href='/catalog.html'>каталог</a></p>"
        return blocks

    for i in range(0,len(result)):
        blocks+=item.format(result[i].Picture,result[i].Sticker_ID)
        if (i+1)%2==0:
            blocks+="<br>"

    blocks+="<br>Материал<br><select name='mat' size='3'>"

    materials=conn.execute(dataBase.Material_Table.select()).fetchall()
    for mat in materials:
        blocks+="<option value='{0}'>{1}. Цена: {2}</option>".format(mat['Material_ID'],mat['Name'],mat['Price'])
    blocks+="</select><br>"

    return blocks

def DelItem(request):
    sticker=request.matchdict['id']
    user=request.authenticated_userid
    conn=dataBase.engine.connect()
    book=conn.execute(dataBase.Cheque_Table.select().where
                      (dataBase.Cheque_Table.c.Complited==False
    ).where(dataBase.Cheque_Table.c.Client_ID==user)).fetchone()['Book_ID']
    conn.execute(dataBase.Stickers_In_StickerBook_Table.delete().where(dataBase.Stickers_In_StickerBook_Table.c.Book_ID==
        book).where(dataBase.Stickers_In_StickerBook_Table.c.Sticker_ID==sticker))
    items=GenerateBinItems(request)
    return Response(environment.get_template('/bin.html').render(body=items))