from datetime import date, timedelta
today = date.today()
weekday = date.today().weekday()
bookday = today + timedelta(days=9)
data = {"supporter_id":120,"sana":str(bookday),"start_time":"13:00","end_time":"13:30"}
print(bookday.weekday())  # Output: 2026-04-05
