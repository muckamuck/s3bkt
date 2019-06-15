"""
The command line interface to s3bkt.

Major help from: https://www.youtube.com/watch?v=kNke39OZ2k0
"""
import click


'''
@click.group()
def cli():
    """
    A utility
    """
    print(cli)
'''

@click.command()
@click.option('--directory', '-d', required=True, help='directory that holds the bucket config')
@click.version_option(version='0.1.0')
def main(directory):
    print(f'food: {directory}')
