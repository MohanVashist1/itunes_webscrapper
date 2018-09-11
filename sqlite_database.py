import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use("fivethirtyeight")
conn = sqlite3.connect("tutorial.db")
c = conn.cursor()


def create_table():
    c.execute(
        "CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(142342556, '2016-01-02', 'python',8)")
    conn.commit()  # this saves the data
    c.close()  # close cursor
    conn.close()  # close connection


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(
        unix).strftime("%Y-%m-%d %H:%M:%S"))
    keyword = "python"
    value = random.randrange(0, 10)
    c.execute("INSERT INTO stuffToPlot (unix,datestamp,keyword,value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()


def read_from_db():

    # * means everything value=3 is logic where you only fetch when the value column is 3
    c.execute("SELECT * FROM stuffToPlot WHERE value=5 and keyword='python'")
    # data = c.fetchall()
    c.execute("SELECT * FROM stuffToPlot WHERE unix>1536522877.4980085")
    # print(data)
    # for row in c.fetchall():
    #     print(row)
    for row in c.fetchall():  # print the first column
        print(row[0])
    # change the order of retrival
    c.execute(
        "SELECT keyword, unix, value, datestamp FROM stuffToPlot WHERE unix>1536522877.4980085")
    for row in c.fetchall():
        print(row)
    # get only the first two columns
    c.execute(
        "SELECT keyword, datestamp FROM stuffToPlot WHERE unix>1536522877.4980085")
    for row in c.fetchall():
        print(row)


def graph_data():
    c.execute("SELECT unix,value FROM stuffToPlot")
    dates = []
    values = []
    for row in c.fetchall():
        dates.append(datetime.datetime.fromtimestamp(
            row[0]))
        values.append(row[1])
    plt.plot(dates, values, '-')
    plt.show()


def del_and_update():
    # c.execute("UPDATE stuffToPlot SET value=99 WHERE value=8") # update
    # conn.commit()
    # c.execute("SELECT * FROM stuffToPlot")
    # [print(row) for row in c.fetchall()]
    c.execute("DELETE FROM stuffToPlot WHERE value = 99")  # delete
    conn.commit()
    c.execute("SELECT * FROM stuffToPlot")
    [print(row) for row in c.fetchall()]

    # create_table()
    # data_entry()
    # for i in range(10):
    #     dynamic_data_entry()
    #     time.sleep(1)
# graph_data()
# read_from_db()
# del_and_update()
# c.close()
# conn.close()
unix = time.time()
print(unix)
print(1536633807.9092324 - 400000)
# date = str(datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d"))
# new_unix = time.mktime(datetime.datetime.strptime(
#     date, "%Y-%m-%d").timetuple())
# week = unix - 604800
# date = str(datetime.datetime.fromtimestamp(week).strftime("%Y-%m-%d"))
# print(date)
