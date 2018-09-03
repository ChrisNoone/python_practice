import paho.mqtt.publish as publish

HOST = "127.0.0.1"

publish.single("etekcity", "NooneLiu", hostname=HOST, port=1883)