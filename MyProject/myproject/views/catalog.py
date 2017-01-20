from pyramid.response import Response
from MyProject.myproject.views.base import environment,dataBase

def Catalog_Page(request):
    items=GenerateCatalogItems()
    return Response(environment.get_template('/catalog.html').render(body=items))

def GenerateCatalogItems():
    conn=dataBase.engine.connect()

    result=conn.execute(dataBase.Sticker_Table.select()).fetchall()
    blocks="<table><tr>"
    k=0
    for i in range(0,len(result)):
        blocks+=" <th><form action ='/adminEditTableEdit/{0}' method='POST'><image name='image' src={1}" \
                "  style='max-width: 600px; max-height: 600px;'><br><input type='submit' aligh='centre' value='В корзину'>" \
                "</input></form><th>".format(str(result[i][0]),str(result[i][1]))
        if (i+1)%2==0:
            blocks+="</tr><tr> "
    return blocks+"</table>"



