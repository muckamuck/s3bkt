'''
S3 bucket utility
'''
import os
import logging
import json
import pdb

logger = logging.getLogger('S3Utility')

config_files = [
    'properties.sh',
    'config'
]

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

    def work(self):
        '''
        S3 bucket utility worker

        Args:
            None

        Returns:
            True or False, good or bad
        '''
        try:
            logger.info('working on bucket found in: %s', json.dumps(self.config, indent=2))
        except Exception as wtf:
            logger.error(wtf, exc_info=True)
            return False

        return True
