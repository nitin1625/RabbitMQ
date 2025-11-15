import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch,method,properties,body):
    print(f"Payment Consumer : received new message : {body}")

# create connection
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

# Channel and exchange declaration
channel = connection.channel()
channel.exchange_declare(exchange='routing',exchange_type=ExchangeType.direct)

# queue declaration and binding -> one for each consumer to connect
queue=channel.queue_declare(queue='',exclusive=True)
channel.queue_bind(exchange='routing',queue=queue.method.queue,routing_key='paymentsonly')

# consume messages
channel.basic_consume(queue=queue.method.queue,auto_ack=True,on_message_callback=on_message_received)
print('Starting Consuming...')
channel.start_consuming()

