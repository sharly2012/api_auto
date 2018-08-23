import pymysql
from util.BaseUtil import BaseUtil

host = BaseUtil().get_config_value('DB', 'host')
port = BaseUtil().get_config_value('DB', 'port')
user = BaseUtil().get_config_value('DB', 'username')
password = BaseUtil().get_config_value('DB', 'password')
db_name = BaseUtil().get_config_value('DB', 'db_name')
charset = BaseUtil().get_config_value('DB', 'charset')


class DB:

    def __init__(self):
        try:
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db_name,
                                              charset=charset)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def execute_sql(self, query):
        array = []
        con = self.connection
        cur = con.cursor()
        try:
            cur.execute(query)
            result = cur.fetchall()
            con.commit()
            for row in result:
                array.append(row)
        except Exception as e:
            con.rollback()
            print(e)
        return array

    def close_db(self):
        self.connection.close()


if __name__ == '__main__':
    sql = "SELECT * FROM interface_list;"
    result = DB().execute_sql(sql)
    for row in result:
        test_name = row[1]
        print(test_name)
        print(row)
