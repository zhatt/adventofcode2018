import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument( '--part', type = int, choices = ( 1, 2 ), default = 1 )
    parser.add_argument( 'inputfile' )
    return parser.parse_args()
