from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
import sqlite3

conn = sqlite3.connect('caiji.db')
cursor = conn.cursor()

site = ''  # http/https + 域名
siteuser = ''
sitepass = ''
wp = Client(f"{site}/xmlrpc.php", siteuser, sitepass)

def getunread():
    cursor.execute("select id from article where ispost=0;")
    result=[i[0] for i in cursor.fetchall()]
    return result

def postarticle(id):
    cursor.execute(f"select * from article where id={id};")
    result=cursor.fetchone()
    post = WordPressPost()
    post.title = result[2]
    post.post_status = 'publish'
    if result[3]:
        post.terms_names = {
                'post_tag': result[3].split(','),
                'category': [result[4]],
        }
    else:
        post.terms_names = {
                'category': [result[4]],
        }
    post.content = result[5]
    wp.call(NewPost(post))
    cursor.execute(f"UPDATE article SET ispost=1 WHERE id={id};")
    conn.commit()


if __name__ == "__main__":
    for i in getunread():
        postarticle(i)