from kafka import KafkaProducer
from kafka.errors import KafkaError
import json


def transaction_producer(transaction):
  producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
  # produce json messages
  producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
  producer.send('transaction-topic', transaction)
  #print("Topic Createed: Waiting for Consumer to Subscribe")
  producer.flush()
  # configure multiple retries
  producer = KafkaProducer(retries=5)

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    log.error('error!', exc_info=excp)

