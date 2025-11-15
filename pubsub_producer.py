import pika
from pika.exchange_type import ExchangeType

# create connection
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

# Channel and queue declaration
channel = connection.channel()
channel.queue_declare(queue='letterbox')

# Message creation and publish
message = "Message Published."
channel.basic_publish(exchange='', routing_key='letterbox', body=message)
print(f"Sent message: {message}")
connection.close()

