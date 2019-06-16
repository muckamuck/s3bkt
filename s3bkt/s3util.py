'''
S3 bucket utility
'''
import os
import logging

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

        config_found = False
        for f in config_files:
            wrk = f'{self.directory}/{f}'
            if os.path.isfile(wrk):
                self.config = wrk
                config_found = True
                break

        if config_found:
            logger.info('configuration file found: %s', self.config)
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
            logger.info('working on bucket found in: %s', self.config)
        except Exception as wtf:
            logger.error(wtf, exc_info=True)
            return False

        return True
