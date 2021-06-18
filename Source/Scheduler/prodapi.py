from kafka import KafkaProducer
import json
producer = KafkaProducer(bootstrap_servers='3.142.69.135:9092',
value_serializer=lambda v: json.dumps(v).encode('utf-8'))        
def send_message(topic,message):
    producer.send(topic, value = message)
    producer.flush()