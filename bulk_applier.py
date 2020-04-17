import os
import os.path
import logging
from types import FunctionType as Function

class BulkApplier:
  def __init__(
      self,
      apply: Function,
      ffilter: Function,
      rename: Function):
    """
    keyword arguments:

    apply consumes (infile, outfile) and applies an operation
    turning one into the other.

    ffilter is a predicate on str (assuming the str is a file path)

    rename is a function of (str -> str) and converts the name of a given
    input file into the name of an output file.
    """

    self.apply = apply
    self.ffilter = ffilter
    self.rename = rename

  def targets(self, top: str) -> list:
    """ files under `top` which satisfy `ffilter` """
    result = []
    for dirpath, _, filenames in os.walk(top):
      result.extend(
        filter(
          self.ffilter,
          [
            os.path.join(dirpath,filename)
            for filename in filenames
          ]
        )
      )
    logging.info(f'found {len(result)} target files')
    logging.debug(f'targets: {result}')
    return result

  def bulk_apply(self, top: str) -> list:
    """
    applies the `apply` function on all files satisfying the `ffilter`
    returns a list of results from `apply` if it doesn't consume the files
    """
    return [
      self.apply(infile, self.rename(infile))
      for infile in self.targets(top)
    ]

