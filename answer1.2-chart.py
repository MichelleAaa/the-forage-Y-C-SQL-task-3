import sqlite3, pandas , matplotlib.pyplot as plt

conn = sqlite3.connect("./shiptivity.db")

sql = """SELECT COUNT(DISTINCT user_id) as total_daily_users,
DATE(login_timestamp, 'unixepoch') as login_date
FROM login_history
GROUP BY login_date
ORDER BY login_date ASC;"""

data = pandas.read_sql(sql, conn)
plt.bar(data.login_date, data.total_daily_users)
plt.title("Average Daily Users Before and After")
plt.show()
