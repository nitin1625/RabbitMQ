import pika
from pika.exchange_type import ExchangeType

# create connection
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

# Channel and exchange declaration
channel = connection.channel()
channel.exchange_declare(exchange='pubsub',exchange_type=ExchangeType.fanout)

# Message creation and publish
message = "Message Published."
channel.basic_publish(exchange='pubsub', routing_key='', body=message)
print(f"Sent message: {message}")
connection.close()

