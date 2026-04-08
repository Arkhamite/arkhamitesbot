import requests
from datetime import date, timedelta

def support(i):
    today = date.today()
    bookday = today + timedelta(days=i)
    weekday = bookday.weekday()

    headers = {"authorization": "Bearer 52993|l92eh5NNNwEyWnZYMtWtN5GCd74mkht0t4WF6wKq "}
    url = 'https://ieltszone.lc-up.com/api/v3/support/register'

    if weekday == 6:
        pass
    else:
        if weekday % 2 == 0:
            data = {"supporter_id":120,"sana":str(bookday),"start_time":"13:00","end_time":"13:30"}
        else:
            data = {"supporter_id":120,"sana":str(bookday),"start_time":"16:00","end_time":"16:30"}
        
        response = requests.post(url, data=data, headers=headers)
        res = response.json()
    
        return res

if __name__ == "__main__":
    for i in range(100):
        print(support(i))