from MyProject.myproject.views.base import Data_Base
import os

if os.path.exists("sqlite:///some.db"):
    os.remove("sqlite:///some.db")

dataBase=Data_Base()


def AddPictures(conn):
    conn.execute(dataBase.Sticker_Table.delete())
    pictures=os.listdir('.\\static\\images')
    for picture in pictures:
        conn.execute(dataBase.Sticker_Table.insert().values(Picture="\\static\\images\\"+picture))

def AddMaterials(conn):
    conn.execute(dataBase.Material_Table.delete())
    text=open("static\\materials.txt","r",encoding='utf-8').read()
    list=text.split('\n')
    materials=[(c.split('=')[0],c.split('=')[1]) for c in list]
    for elem in materials:
        conn.execute(dataBase.Material_Table.insert().values(Name=elem[0],Price=elem[1]))

conn=dataBase.engine.connect()
AddPictures(conn)
AddMaterials(conn)

if not dataBase.engine.dialect.has_table(dataBase.engine, ''):
    dataBase.metaData.create_all(dataBase.engine)