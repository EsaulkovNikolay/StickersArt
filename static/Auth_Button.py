import cgi
import html
from Application import dataBase

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1")
text2 = form.getfirst("TEXT_2")
form.getfirst("BUTTON")
text1=html.escape(text1)
text2=html.escape(text2)

conn=dataBase.engine.connect()
if len(conn.execute("select Client.Email,Client.Password from Client where Client.Email=:email and Client.Password=:passwd",
                    email=text1,passwd=text2))==1:
    print("!")
else:
    print("$")