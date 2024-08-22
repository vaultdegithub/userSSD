import requests
from collections import deque
from datetime import datetime
import json

class DataCollector:
    def __init__(self,  max_queue_size=100, stub_file='data_stub.json'):
        self.api_url = None
        self.queue = deque(maxlen=max_queue_size)
        self.stub_file = stub_file

    def read_from_source(self, api_url):
        try:
            self.api_url = api_url
            response = requests.get(self.api_url)
            response.raise_for_status()  # Check if the request was successful
            data = response.json()
            timestamp = datetime.now()
            if len(self.queue) == self.queue.maxlen:
                self.save_to_stub(self.queue[0])
            self.queue.append((timestamp, data))
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")

    def save_to_stub(self, data):
        try:
            with open(self.stub_file, 'a') as f:
                f.write(json.dumps(data, default=str) + '\n')
        except IOError as e:
            print(f"Error saving data to stub: {e}")

    def warehouse_queue(self):
        return list(self.queue)

    def get_current(self):
        if self.queue:
            return self.queue[-1][1]
        else:
            return None

# Example usage:
# collector = DataCollector()
# collector.read_from_source("https://api.example.com/data")
# print(collector.warehouse_queue())
# print(collector.get_current())
