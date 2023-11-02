import sys
from Adafruit_IO import MQTTClient

AIO_FEED_ID = "abc-group"
AIO_USERNAME = "Project_intro_CS"
AIO_KEY = "aio_bxIa251IJNd7fQUsnznP1amv7We4"

def connected(client) :
    print("Successfully connected...")
    client.subscribe(AIO_FEED_ID)

def subscribe(client, userdata, mid, granted_qos) :
    print("Successfully subscribed...")    

def disconnected(client) :
    print("Disconnected...")
    sys.exit(1)

def message(client, feed_id, payload) :
    print("Receive data: " + payload)

client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    pass