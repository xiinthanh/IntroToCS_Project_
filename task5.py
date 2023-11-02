import sys
import random
import time
import requests
from random import randint
from Adafruit_IO import MQTTClient


class AdafruitServer:
    AIO_FEED_ID = ['']
    AIO_USERNAME = 'Project_intro_CS'
    AIO_KEY = 'aio_iowj56Cp03DXMsd5YBLsVeXfi1wj'


    # IoT
    def connected(client):
        print('Server connected ...')
        for FEED_ID in AdafruitServer.AIO_FEED_ID:
            client.subscribe(FEED_ID)
    
    def subscribe(client , userdata , mid , granted_qos):
        print('Subscribed...')

    def disconnected(client):
        print('Disconnected from the server...')
        sys.exit (1)

    def message(client , feed_id , payload):
        print('Received data: ' + payload)


    def __init__(self, _data):
        print('Init task 5')

        self.client = MQTTClient(self.AIO_USERNAME , self.AIO_KEY)

        (self.client).on_connect = AdafruitServer.connected
        (self.client).on_disconnect = AdafruitServer.disconnected
        (self.client).on_message = AdafruitServer.message
        (self.client).on_subscribe = AdafruitServer.subscribe
        (self.client).connect()
        (self.client).loop_background()


        self.client.publish('student-card', 0)
        self.client.publish('student-face', 0)
        self.client.publish('message', '.')
        self.client.publish('bus-status', '0/?')

        self.prev_data = ['']
        self.data = _data
        return

    def Run(self):
        # Debug
        # print("prev_data: ", self.prev_data)
        # print("data: ", self.data)
        if (self.prev_data == self.data):
            # Does not have any new data to post
            return '[i]'

        print('#'*30)
        print('Uploading to Adafruit...')

        # data's format: [<ID>]<DATA>  Ex: [1]False
        task_ID = self.data[0][:3]
        task_Data = self.data[0][3:]
        print(task_ID, task_Data)

        message = ''
        if (task_ID == '[0]'):
            if (task_Data == 'True'):
                value = 1
                message = 'Student Card recognized!'
            else:
                value = 0
            self.client.publish('student-card', value)
        elif (task_ID == '[1]'):
            if (task_Data == 'Unknown'):
                value = 0
            else:
                value = 1
                message = 'Face recognized!'
            self.client.publish('student-face', value)
        elif (task_ID == '[2]'):
            if (task_Data == ''):
                message = 'You have not registered!'
            else:
                message = f'Check-in successful, Welcome {task_Data}!'

                # Reset
                self.client.publish('student-card', 0)
                self.client.publish('student-face', 0)
        elif (task_ID == '[3]'):
            self.client.publish('bus-status', task_Data)

        self.prev_data = self.data.copy()
        if message:
            self.client.publish('message', message)

        return "[i]"  # (ignore): do not store this task's output


if __name__ == '__main__':
    
    uploader = AdafruitServer()
    while True:
        time.sleep(5)
        print(uploader.Run())


