import pandas as pd

data = {
    'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'course_id':  ['C1', 'C2', 'C1', 'C3', 'C2', 'C3', 'C1', 'C2', 'C3'],
    'login_date': [
        '2026-01-25', '2026-01-20',
        '2026-01-10', '2026-01-05',
        '2026-01-26', '2026-01-18',
        '2026-01-02',
        '2026-01-24', '2026-01-23'
    ],
    'minutes_spent': [30, 45, 20, 50, 60, 40, 15, 35, 55]
}

df = pd.DataFrame(data)
print(df)
#identify inactive students (no login in last 7 days)
df['login_date']=pd.to_datetime(df['login_date'])
cutoff=pd.Timestamp('2026-01-27')-pd.Timedelta(days=7)
last_login=df.groupby('student_id')['login_date'].max().reset_index()
inactive=last_login[last_login['login_date']<cutoff]
print(inactive)
#average session duration per course
avg_session_duration=df.groupby('course_id')['minutes_spent'].mean().reset_index(name='avg_minutes_spent')
print(avg_session_duration)
#top-3 courses with highest engagement
top_3=df.groupby('course_id')['minutes_spent'].sum().sort_values(ascending=False).head(3).reset_index(name='total_minutes_spent')
print(top_3)