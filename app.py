from flask import Flask, render_template,request,url_for,redirect
import sqlite3

app = Flask(__name__)

def getunpost():
    conn = sqlite3.connect('caiji.db')
    cursor = conn.cursor()
    cursor.execute("select id from article where ispost=0;")
    result=[i[0] for i in cursor.fetchall()]
    conn.close()
    return result

def posttitle(id):
    conn = sqlite3.connect('caiji.db')
    cursor = conn.cursor()
    cursor.execute(f"select title from article where id={id};")
    title=cursor.fetchone()[0]
    conn.close()
    return title

@app.route("/")
def hello_world():
    unpost=[{"id":i,"title":posttitle(i)} for i in getunpost()]
    return render_template('index.html',unpost=unpost)

# 文章编辑页
@app.route("/article/<id>")
def article(id):
    conn = sqlite3.connect('caiji.db')
    cursor = conn.cursor()
    cursor.execute(f"select * from article where id={id};")
    result=cursor.fetchone()
    conn.close()
    context={
        "id": id,
        "title": result[2],
        "category":result[4],
        "tags": result[3],
        "content": result[5]
    }
    return render_template('article.html',**context)


# 编辑分类
@app.route("/editCategory")
def editCategory():
    id=request.args.get("id")
    value=request.args.get("value")
    conn = sqlite3.connect('caiji.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE article SET category='{value}' WHERE id={id};")
    conn.commit()
    conn.close()
    return redirect(url_for('article',id=id))


# 编辑标签
@app.route("/editTag")
def editTag():
    id=request.args.get("id")
    value=request.args.get("value")
    conn = sqlite3.connect('caiji.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE article SET tag='{value}' WHERE id={id};")
    conn.commit()
    conn.close()
    return redirect(url_for('article',id=id))


# 编辑内容
@app.route("/editContent")
def editContent():
    id=request.args.get("id")
    value=request.args.get("value")
    conn = sqlite3.connect('caiji.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE article SET content='{value}' WHERE id={id};")
    conn.commit()
    conn.close()
    return redirect(url_for('article',id=id))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
