


##########################################################
 # Understandin logging levels and formation
##########################################################

import logging

logger = logging.getLogger("quick logger")
logger.setLevel(logging.NOTSET)
r = 201
logger.info("send message response code %s", 201)

##########################################################
