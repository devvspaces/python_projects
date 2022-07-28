import time
import redis

# Connect to a local redis instance
r = redis.Redis(host='localhost', port=6379, db=0)
print('Connected')
last_id = '$'  # `$` means only new messages
while True:
    events = r.xread({"stream_key": last_id}, block=0, count=10)
    for _, e in events:
        print(f"new event, amount: {e['amount']}")
        last_id = e['id']
    print("\n")
    # sleep for a while to avoid CPU usage
    time.sleep(1)
    # if you want to stop the loop, you can break the loop
    # break
