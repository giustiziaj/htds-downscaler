# HTDS Downscaler

Command line tool which traverses a directory tree, looking for any files with
a given name.  Uses ImageMagick/wand to rescale image files, and saves them in
a new location.

## How To Use

```
usage: htds-downscaler [-h] [-n NAME] [-s SCALE] [-v] [-q] top

bulk image rename & rescale

positional arguments:
  top                   top of filesystem tree to traverse

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  file name to target
  -s SCALE, --scale SCALE
                        scalar multiplier to apply to image dimensions
  -v, --verbose         set logging level to DEBUG. Increases output
  -q, --quiet           set logging level to WARN. Reduces output
```

## Dependencies

- Tested with `Python 3.8.2`
- Requires `wand`. Tested with version `0.5.6`
