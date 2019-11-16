# Simple way to do health check on redis just do ping pong
# if pong fails, redis cluster is not healthy.
# @Author : Aseem Jain

import logging
import redis

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# remote machine
host_ip = "10.126.69.99"
host_port = "36379"
host_password = 'xxx'


# if ping fails, then redis instance is not healthy
def health_check(host_ip):
    try:
        client = redis.Redis(host=host_ip, port=host_port, password=host_password)
        client.ping()

    except Exception as e:
        logging.error('Redis HealthCheck failed for {host} - {error}'.format(host=host_ip, error=str(e)))
        return False
    return True

health_check(host_ip)
