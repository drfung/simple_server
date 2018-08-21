import pymysql

from urllib.parse import parse_qs

def login(request):
    if request.get("REQUEST_METHOD") == "POST":
        try:
            request_body_size = int(request.get("CONTENT_LENGTH", 0))
        except:
            request_body_size = 0

        request_body = request['wsgi.input'].read(request_body_size)
        print(request_body)
        data = parse_qs(request_body)

        user = data.get(b"user")[0].decode()
        pwd = data.get(b"pwd")[0].decode()

        conn = pymysql.connect(host="127.0.0.1",port=3306,passwd="fbo",db="web")
        cur = conn.cursor()
        SQL = "select * from userinfo where name='%s' and password ='%s'"%(user,pwd)
        cur.execute(SQL)

        if cur.fetchone():
            f = open("templates/backend.html","rb")
            data = f.read()
            data = data.decode('utf8')
            return data.encode('utf8')
        else:
            print("OK456")
            return b"user or pwd is wrong"
    else:
        f = open("templates/login.html", "rb")
        data = f.read()
        data = data.decode("utf8")
        return data.encode("utf8")
