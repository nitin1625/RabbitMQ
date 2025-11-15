import pika
from pika.exchange_type import ExchangeType

# create connection
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

# Channel and queue declaration
channel = connection.channel()
channel.exchange_declare(exchange='mytopicexchange',exchange_type=ExchangeType.topic)

# Message creation and publish
consumer="user.user"
message = f"Message Published to {consumer}."
channel.basic_publish(exchange='mytopicexchange', routing_key=consumer, body=message)
print(f"Sent message: {message}")
connection.close()

