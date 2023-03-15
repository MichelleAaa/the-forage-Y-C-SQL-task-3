import sqlite3, pandas , matplotlib.pyplot as plt

conn = sqlite3.connect("./shiptivity.db")

sql = """SELECT cardId, COUNT(id) as status_changes 
FROM card_change_history
WHERE oldStatus <> newStatus
GROUP BY cardId;"""

data = pandas.read_sql(sql, conn)
#x values: data.cardID,  y values: data.status_changes
plt.bar(data.cardID, data.status_changes)
plt.title("Status Changes by Card")
plt.show()