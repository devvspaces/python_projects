import redis

# Connect to a local redis instance
r = redis.Redis(host='localhost', port=6379, db=0)
print('Connected')
event = {"eventType": "purchase", "amount": 5, "item_id": "XXX"}
r.xadd("stream_key", event, '*')
# the `*` means that redis generates and event id automatically
# the `event` is the payload of the event
