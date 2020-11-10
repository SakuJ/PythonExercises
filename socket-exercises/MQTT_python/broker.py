# BROKER

import logging
import asyncio
from hbmqtt.broker import Broker

# Create and configure a logger instance
logger = logging.getLogger(__name__)

config = {
    'listeners': { # network bindings configuration list
        'default': {
            'type': 'tcp', # transport protocol type
            'bind': 'localhost:9999' # IP address and port binding
        }
    },
    'sys_interval': 10,
    'topic-check': {
        'enabled': False
    },
    'plugins': ['auth_anonymous'], # defines the list od activated plugins
    'topic-check': {
        'enabled': True,
        'plugins': ['topic_taboo']
    }
}

broker = Broker(config)

@asyncio.coroutine
def startBroker():
    yield from broker.start() # Start the broker to serve with the given configuration

if __name__ == '__main__':
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter)
    asyncio.get_event_loop().run_until_complete(startBroker())
    asyncio.get_event_loop().run_forever()    