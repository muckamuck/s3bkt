'''
S3 bucket utility
'''
import logging
import boto3 #noqa


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(asctime)s (%(module)s) %(message)s',
    datefmt='%Y/%m/%d-%H:%M:%S'
)

logger = logging.getLogger('S3Utility')


class S3Utility:

    def __init__(self):
        logger.debug('making a new S3Utility')
