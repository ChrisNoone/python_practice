# coding:utf8

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("hello")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.topic == "hello":
        client.publish("response", "yes,i heard hello")

if __name__ == '__main__':
    client = mqtt.Client()
#     client.username_pw_set("admin", "password")
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect("127.0.0.1", 1883, 60)
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()