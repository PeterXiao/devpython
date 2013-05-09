__author__ = 'Administrator'
import random,time,sqlite3
import threading

DB_SQLITE_NAME=".\\test.db"

def sqliteHandler():
    #连接数据库
    try:
        sqlite_conn = sqlite3.connect(DB_SQLITE_NAME)
    except sqlite3.Error,e:
        print "连接sqlite3数据库失败", "\n", e.args[0]
        return
    #获取游标
    sqlite_cursor=sqlite_conn.cursor()
    #如果存在表先删除
    sql_del="DROP TABLE IF EXISTS tbl_test;"
    try:
        sqlite_cursor.execute(sql_del)
    except sqlite3.Error,e:
        print "删除数据库表失败！", "\n", e.args[0]
        return
    sqlite_conn.commit()

    #创建表
    sql_add='''CREATE TABLE tbl_test(
    i_index INTEGER PRIMARY KEY,
    sc_name VARCHAR(32)
    );'''
    try:
        sqlite_cursor.execute(sql_add)
    except sqlite3.Error,e:
        print "创建数据库表失败！", "\n", e.args[0]
        return
    sqlite_conn.commit()

    #添加一条记录
    sql_insert="INSERT INTO tbl_test(sc_name) values('mac');"
    try:
        sqlite_cursor.execute(sql_insert)
    except sqlite3.Error,e:
        print "添加数据失败！", "\n", e.args[0]
        return
    sqlite_conn.commit()

    #查询记录
    '''sql_select="SELECT * FROM tbl_test;"
    sqlite_cursor.execute(sql_select)
    for row in sqlite_cursor:
        i=1;
        print "数据表第%s" %i,"条记录是：", row''',

def rater():
    count = 0
    lasttime = time.time()
    print(lasttime)
    return  lasttime
    '''while True:
        yield
        count += 1
        now = time.time()
        delta = now - lasttime
        if delta > 1:
            print(count / delta, '/s')
            count = 0
            lasttime = now'''

def writeinsqlite():
    #连接数据库
    try:
        sqlite_conn = sqlite3.connect(DB_SQLITE_NAME)
    except sqlite3.Error,e:
        print "连接sqlite3数据库失败", "\n", e.args[0]
        return
    pass
    #添加一条记录
    sql_insert="INSERT INTO tbl_test(sc_name) values('mac');"
    try:
         sqlite_cursor=sqlite_conn.cursor()
         sqlite_cursor.execute(sql_insert)
    except sqlite3.Error,e:
        print "添加数据失败！", "\n", e.args[0]
        return
    sqlite_conn.commit()
    sqlite_conn.close()



TOTAL = 0

MY_LOCK = threading.Lock()

class CountThread(threading.Thread):
    def run(self):
        global TOTAL
        MY_LOCK.acquire()
        TOTAL = TOTAL + 1
       #print(TOTAL)
        writeinsqlite()
        MY_LOCK.release()
        #print('%s\n' % (TOTAL))


sqliteHandler()
r = rater()
for i in range(500):
     a = CountThread()
     a.start()
     a.join()
r = rater()
