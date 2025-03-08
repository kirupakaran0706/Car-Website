#!C:\Python312\python.exe


import cgi

print("Content-Type:text/html\r\n\r\n")

print("<html>")
print("<body>")

print("<h1>Thanq for register</h1>")



form=cgi.FieldStorage()
fname=form.getvalue("name")
faddress=form.getvalue("address")
fnumber=form.getvalue("number")

print("<h1>",fname,faddress,fnumber,"</h1>")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kirupa"
)



mycursor=mydb.cursor()

sql="INSERT INTO customer(Name,address,number)values(%s,%s,%s)"
value=(fname,faddress,fnumber)


mycursor.execute(sql,value)
mydb.commit()


print("</body>")
print("</html>")