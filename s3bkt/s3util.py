'''
S3 bucket utility
'''
import os
import logging
import json
import boto3
from s3bkt.clients import init_boto3_clients

logger = logging.getLogger('S3Utility')

config_files = [
    'properties.sh',
    'config'
]

policy_files = [
    'encryption.json',
    'notification.json',
    'lifecycle.json',
    'policy.json',
    'tags.json'
]

services = [
    's3'
]


def date_converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


class S3Utility:
    '''
    S3 bucket utility
    '''
    def __init__(self, **kwargs):
        '''
        S3 bucket utility initializer

        Args:
            kwargs - dictionary of args

        Raises:
            ValueError - if config file not found
        '''
        logger.debug('making a new S3Utility')
        logger.info('Looking for for bucket configuration in: %s', kwargs.get('directory'))
        self.directory = kwargs.get('directory', None)
        if not os.path.isdir(self.directory):
            raise ValueError(f'{self.directory} is not a directory')

        self.s3_client = init_boto3_clients(
            services,
            region=kwargs.get('region', None),
            profile=kwargs.get('profile', None)
        ).get('s3', None)

        config_file = None
        self.config = dict()
        for f in config_files:
            wrk = f'{self.directory}/{f}'
            if os.path.isfile(wrk):
                config_file = wrk
                break

        if config_file:
            logger.info('configuration file found: %s', config_file)
            with open(config_file, 'r') as f:
                tmp = f.readline()
                while tmp:
                    tmp = tmp.strip()
                    if not tmp.startswith('#'):
                        parts = tmp.split('=')
                        if len(parts) == 2:
                            key = parts[0].strip()
                            val = parts[1].strip()
                            self.config[key] = val
                        else:
                            logger.warning('bad config element: "%s"', tmp)
                    tmp = f.readline()
        else:
            raise ValueError(f'configuration file not found')

        try:
            for p in policy_files:
                policy_file = f'{self.directory}/{p}'
                if os.path.isfile(policy_file):
                    logger.info('policy file found: %s', policy_file)
                    key = p.split('.')[0]
                    with open(policy_file, 'r') as f:
                        stuff = json.load(f)
                        self.config[key] = stuff
        except Exception as wtf:
            logger.error('policy file %s failed to load: %s', policy_file, wtf)
            raise ValueError(f'bad policy file {policy_file}')


    def work(self):
        '''
        S3 bucket utility worker

        Args:
            None

        Returns:
            True or False, good or bad
        '''
        try:
            logger.info(
                'working on bucket found in: %s', json.dumps(self.config, indent=2))
            if 'policy' in self.config:
                self.apply_bucket_policy()
        except Exception as wtf:
            logger.error(wtf, exc_info=True)
            return False

        return True

    def apply_bucket_policy(self):
        try:
            logger.info('applying bucket policy')
            response = self.s3_client.put_bucket_policy(
                Bucket=self.config.get('bucket', None),
                Policy=json.dumps(self.config.get('policy'))
            )
            logger.info(
                'put_bucket_policy: %s',
                json.dumps(response, indent=2, default=date_converter)
            )
        except Exception as wtf:
            logger.error(wtf, exc_info=True)
            return False
        else:
            return True
