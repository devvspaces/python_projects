import time
import redis

r = redis.Redis()
pubsub = r.pubsub()


pubsub.psubscribe('football-*')


def is_message(text: str):
    return text.lstrip('p') == 'message'


while True:
    message = pubsub.get_message()
    print(message)
    if message is not None and is_message(message.get('type')):
        print("Got a new message")
        print("Channel: ", message.get('channel'))
        print("Message: ", message.get('data'))
    else:
        print("No message")

    print("\n")
    time.sleep(3)
