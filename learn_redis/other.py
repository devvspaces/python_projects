import redis
import json


r = redis.Redis(
    host="localhost", port="6379", db=1,
    decode_responses=True, encoding="utf-8")

pubsub = r.pubsub()

pubsub.subscribe("channel-1")
pubsub.psubscribe("channel-*")

r.publish('channel-1', 'value-1')

print(pubsub.get_message())
print(pubsub.get_message())
print(pubsub.get_message())
print(pubsub.get_message())
