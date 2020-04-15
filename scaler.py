import logging
from numbers import Number
from types import FunctionType
from wand.image import Image

class Scaler:
  def __init__(self, factor: FunctionType or Number = 1):
    """
    factor can be either a function (on int) to which converts initial
    dimensions to new dimensions, or a scalar factor for the dimensions.
    """

    if isinstance(factor, Number):
      self.func = lambda x: int(x * factor)
    elif isinstance(factor, FunctionType):
      self.func = lambda x: int(factor(x))

  def new_dimensions(self, img: Image) -> (int, int):
    return self.func(img.width), self.func(img.height)

  def scale(self, infile: str, outfile: str):
    """ rescales `infile` and writes new image to `outfile` """

    with Image(filename=infile) as src:
      width, height = self.new_dimensions(src)
      with src.clone() as dest:
        dest.resize(width=width,height=height)
        logging.info(
          f'Converted "{infile}" ({src.width}x{src.height})'
          f' -> "{outfile}" ({dest.width}x{dest.height})')
        dest.save(filename=outfile)
