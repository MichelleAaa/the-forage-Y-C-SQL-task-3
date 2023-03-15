-- TYPE YOUR SQL QUERY BELOW

-- PART 1: Create a SQL query that maps out the daily average users before and after the feature change

-- For Before and After average totals:

WITH daily_count_before AS (SELECT COUNT(DISTINCT user_id) as daily_users
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
SELECT "Daily Users After" as user_type, ROUND(AVG(daily_users), 0) as daily_users FROM daily_count_after;

-- For daily totals:

SELECT COUNT(DISTINCT user_id) as total_daily_users,
DATE(login_timestamp, 'unixepoch') as login_date
FROM login_history
GROUP BY login_date
ORDER BY login_date ASC;


-- PART 2: Create a SQL query that indicates the number of status changes by card

SELECT cardId, COUNT(id) as status_changes 
FROM card_change_history
WHERE oldStatus <> newStatus
GROUP BY cardId;