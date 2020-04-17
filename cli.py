import logging
import argparse
from numbers import Number

def get_args():
  parser = argparse.ArgumentParser()

  parser.description = 'bulk image rename & rescale'

  parser.add_argument(
    'top',
    type=str,
    help='top of filesystem tree to traverse')

  parser.add_argument(
    '-n',
    '--name',
    type=str,
    help='file name to target')

  parser.add_argument(
    '-s',
    '--scale',
    type=float,
    help='scalar multiplier to apply to image dimensions')

  parser.add_argument(
    '-v',
    '--verbose',
    action='store_true',
    help='set logging level to DEBUG. Increases output'
  )

  parser.add_argument(
    '-q',
    '--quiet',
    action='store_true',
    help='set logging level to WARN. Reduces output')

  parser.add_argument(
    '--progress',
    action='store_true',
    help='display progress bar while processing results')

  return config_args(parser.parse_args())

def config_args(args):
  if args.verbose:
    logging.basicConfig(level=logging.DEBUG)
  elif args.quiet:
    logging.basicConfig(level=logging.WARN)
  else:
    logging.basicConfig(level=logging.INFO)
  return args

if __name__ == '__main__':
  print(get_args())