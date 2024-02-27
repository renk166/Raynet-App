from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def index():
    redis.incr('visits')
    count = redis.get('visits').decode('utf-8')
    return 'Total visits: {}'.format(count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
