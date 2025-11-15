

# RabbitMQ Overview

This document provides a concise overview of RabbitMQ, its message flow, routing mechanisms, AMQP fundamentals, ports, consumer patterns, and frame structure.

---

## 1. Message Flow: Producer → Exchange → Queue → Consumer

RabbitMQ routes messages through the following pipeline:

1. A producer sends a message.
2. The message is delivered to an exchange.
3. The exchange routes the message to one or more queues.
4. Consumers receive messages from the queues.

This architecture decouples producers from consumers and enables flexible routing.

---

## 2. Communication Model

RabbitMQ uses TCP connections for communication:

* Producer to Exchange: TCP connection
* Queue to Consumer: TCP connection
* Exchange to Queue: Routing (based on routing keys and binding keys)

---

## 3. Routing in RabbitMQ

Routing defines how messages travel from exchanges to queues.

### Routing Key

Assigned by the producer on each message. It describes the category or topic of the message.

### Binding Key

Defined when a queue is bound to an exchange. It specifies the routing rules for that queue.

The exchange compares the message's routing key with each queue's binding key to determine message delivery.

---

## 4. AMQP (Advanced Message Queuing Protocol)

RabbitMQ implements AMQP 0-9-1, which defines:

* Message format
* Frame structure
* Routing behavior
* Broker operations (connections, channels, acknowledgments, etc.)

AMQP provides standardized, reliable, and interoperable messaging.

---

## 5. RabbitMQ Ports

| Port  | Description                                                             |
| ----- | ----------------------------------------------------------------------- |
| 5672  | AMQP communication port used by clients to produce and consume messages |
| 15672 | RabbitMQ Management Dashboard (default credentials: guest/guest)        |

---

## 6. Competing Consumers

When multiple messages are present in a queue, multiple consumers can connect to the same queue.
RabbitMQ distributes messages among them.
This pattern is known as the "Competing Consumer" approach and is used to increase processing throughput.

---

## 7. Publish/Subscribe Pattern

In the Pub/Sub model, a single message can be consumed by multiple consumers.
This happens when an exchange routes the message to multiple queues, each with its own consumer.

---

## 8. Binding Key vs Routing Key

* A binding key is defined when a queue is bound to an exchange. It acts as a routing rule.
* A routing key is attached to a message by the producer.

The exchange uses the routing key to match against binding keys, deciding which queues will receive the message.

---

## 9. AMQP Frames

RabbitMQ communicates via AMQP frames, which are structured data packets used to encapsulate commands and message content.

### Frame Structure

**Frame Header (8 bytes)**
Contains metadata:

* Frame type (method, content header, or body)
* Channel number
* Frame size

**Extended Header (optional)**
May contain additional information depending on frame type.

**Frame Body (Payload)**
Carries the actual data:

* Method frames contain AMQP commands
* Content header frames include message metadata (content type, properties, payload size)
* Body frames contain the actual message data (may span multiple frames)

**Frame End Byte**
A single terminating byte (`0xCE`) marking the end of the frame.


