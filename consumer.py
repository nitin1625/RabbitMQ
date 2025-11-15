import pika

def on_message_received(ch,method,properties,body):
    print(f"received new message : {body}")

# connection setup
connection_params= pika.ConnectionParameters('localhost')
connection=pika.BlockingConnection(connection_params)

# channel and queue declaration
channel=connection.channel()
channel.queue_declare(queue='letterbox')

# consume messages
channel.basic_consume(queue='letterbox',auto_ack=True,on_message_callback=on_message_received)
print('Starting Consuming...')
channel.start_consuming()

