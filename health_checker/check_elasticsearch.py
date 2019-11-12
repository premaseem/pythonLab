import logging
from elasticsearch import Elasticsearch
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ip = '10.126.69.34'
# ip = '10.126.71.5'


conn_string = 'http://{}:{}@{}:9200/'
user = 'elastic'
password = 'elastic'

def print_all_atrs(node_health):
    for key, value in node_health.items():
        print('key:', key, '-- value:', value)

# Using the python client for Elastic search
def elastic_health_check(host_ip):
    try:
        es = Elasticsearch(conn_string.format(user,password,host_ip))
        es.ping()
        node_health = es.cluster.health()
        es.nodes.stats()
        # print_all_atrs(node_health)
        # print(es.cluster.stats())
        print(es.nodes.stats())
        print('elasticsearch cluster:', node_health['cluster_name'])
        print("health of node is {}".format(node_health.get('status')))

        if node_health.get('status') != 'green':
            return False

    except Exception as e:
        logging.error('Elastic Search HealthCheck failed for {host} - {error}'.format(host=host_ip, error=str(e)))
        return False
    return True


#  Using Rest api end points
def check_cluster_health_status(host_ip):
    try:
        url = "http://{}:9200/_cluster/health".format(host_ip)
        headers = {'Authorization': 'Basic ZWxhc3RpYzplbGFzdGlj'}
        response = requests.request("GET", url, headers=headers, auth=(user, password))
        return "red" != response.json()['status']
    except Exception as e:
        logging.error(
            "Elastic Search HealthCheck for cluster failed for host - {0} with error {1}".format(host_ip, str(e)),
            exc_info=True)
    return False

def check_node_health_status(host_ip):
    try:
        url = "http://{}:9200/_nodes/_local".format(host_ip)
        headers = {'Authorization': 'Basic ZWxhc3RpYzplbGFzdGlj'}
        response = requests.request("GET", url, headers=headers, auth=(user, password))
        return 1 == response.json()['_nodes']['successful']
    except Exception as e:
        logging.error(
            "Elastic Search HealthCheck for individual node failed for host - {0} with error {1}".format(host_ip, str(e)),
            exc_info=True)
    return False

def elastic_health_check(host_ip):
    status = check_cluster_health_status(host_ip) and check_node_health_status(host_ip)
    logging.info("Status of health check at cluster and node level for elastic search {} is {}".format(host_ip, status))
    return status



elastic_health_check(ip)
# curl -u elastic:elastic -XGET 10.126.69.34:9200/_cat/health