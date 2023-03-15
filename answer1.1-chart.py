import sqlite3, pandas , matplotlib.pyplot as plt

conn = sqlite3.connect("./shiptivity.db")

sql = """WITH daily_count_before AS (SELECT COUNT(DISTINCT user_id) as daily_users
    FROM login_history
    GROUP BY strftime("%Y-%d-%m", login_timestamp, 'unixepoch')
    HAVING strftime("%Y-%d-%m", login_timestamp, 'unixepoch') < '2019-06-02'
), 
    daily_count_after AS (SELECT COUNT(DISTINCT user_id) as daily_users
    FROM login_history
    GROUP BY strftime("%Y-%d-%m", login_timestamp, 'unixepoch')
    HAVING strftime("%Y-%d-%m", login_timestamp, 'unixepoch') >= '2019-06-02'
)
SELECT "Daily Users Before" as user_type, ROUND(AVG(daily_users), 0) as daily_users FROM daily_count_before
UNION ALL 
SELECT "Daily Users After" as user_type, ROUND(AVG(daily_users), 0) as daily_users FROM daily_count_after;"""

data = pandas.read_sql(sql, conn)
#x values: data.user_type,  y values: data.daily_users
plt.bar(data.user_type, data.daily_users)
plt.title("Average Daily Users Before and After")
plt.show()
