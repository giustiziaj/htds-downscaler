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
    help='scalar multiplier to apply to image dimensions'
  )

  parser.add_argument(
    '-v',
    '--verbose',
    action="store_true",
    help='set logging level to DEBUG. Increases output'
  )

  parser.add_argument(
    '-q',
    '--quiet',
    action="store_true",
    help='set logging level to WARN. Reduces output'
  )

  return parser.parse_args()

if __name__ == '__main__':
  print(get_args())