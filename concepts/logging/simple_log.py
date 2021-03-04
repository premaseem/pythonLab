"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

"""
import logging
LOG_FORMAT = "%(levelname)s %(asctime)s "
logging.basicConfig(filename="splunk.log", format = LOG_FORMAT, level=logging.DEBUG, filemode="w")
logger = logging.getLogger()
logger.debug("This is broken now")

