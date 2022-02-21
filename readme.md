> 采集程序，采集内容通过wordpress发布
>

img.py: 图片转存

crawler.py: 爬虫采集内容，需要自己根据采集的目标站点定制

post.py: 发布到网站，设一个定时任务。

app.py: 管理未上传的文章，编辑标签和分类



# 图片处理
根据自己的图床选择调api或直接存图




# 数据库初始化
```python
import sqlite3
conn =sqlite3.connect('caiji.db')
cursor =conn.cursor()
cursor.execute("create table article(id INTEGER PRIMARY KEY,url varchar(255),title varchar(255),tag varchar(255),category varchar(20),content text,ispost int);")
```
