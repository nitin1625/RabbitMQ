import pika
import time 
import random 

# Connection setup — use AMQP port (5672), not HTTP port (15672)
connection_params = pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('guest', 'guest'))
connection = pika.BlockingConnection(connection_params)

# Channel and queue declaration
channel = connection.channel()
channel.queue_declare(queue='letterbox')

messageId=1
# Message creation and publish
while(True):
    message = f"sending messageId : {messageId}"
    channel.basic_publish(exchange='', routing_key='letterbox', body=message)

    print(f"Sent message: {message}")
    time.sleep(random.randint(1,4))
    # connection.close()
    messageId+=1
