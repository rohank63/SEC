#!/usr/bin/env python
"""HTSinfer infers metadata from High Throughput Sequencing (HTS) data"""

__version__ = "0.1.0"
__copyright__ = "Copyright 2020 Zavolan lab, Biozentrum, University of Basel"
__license__ = "Apache license 2.0"
__author__ = "Rohan Kandhari"
__maintainer__ = "Rohan Kandhari"
__email__ = "rohan.kandhari.bme16@iitbhu.ac.in"

import argparse
import logging
import sys
from typing import (Optional, Sequence)

from htsinfer import infer_single_paired

logger = logging.getLogger(__name__)


def parse_args(
    args: Optional[Sequence[str]] = None
) -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        # TODO AUTHOR: add here detailed tool description; leave a blank line
        # in between synopsis and extended description
        description=sys.modules[__name__].__doc__,
    )

    # TODO AUTHOR: add here optional and positional arguments as per argparse
    # docs; for many optional arguments, consider adding argument groups for
    # clarity
    parser.add_argument(
        '-f1', '--file-1',
        metavar="FILE",
        type=str,
        required=True,
        help="file path to read/first mate library",
    )
    parser.add_argument(
        '-f2', '--file-2',
        metavar="FILE",
        type=str,
        default=None,
        help="file path to second mate library",
    )
    parser.add_argument(
        '-n', '--max-records',
        metavar="INT",
        type=int,
        default=10000,
        help=(
            "maximum number of records to process, starting with first "
            "record; set to 0 to process entire file(s)"
        )
    )
    parser.add_argument(
        '--verbose', "-v",
        action='store_true',
        default=False,
        help="print logging messages to STDERR",
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        default=False,
        help="print debugging messages to STDERR",
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s {version}'.format(version=__version__),
        help="show version information and exit",
    )

    return parser.parse_args(args)


def setup_logging(
    verbose: bool = False,
    debug: bool = False,
) -> None:
    """Configure logging."""
    if debug:
        level = logging.DEBUG
    elif verbose:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(
        level=level,
        format="[%(asctime)s] %(message)s",
        datefmt='%m-%d %H:%M:%S',
    )


def main(args: argparse.Namespace) -> None:
    """Main function.

    Args:
        args: Command-line arguments and their values.
    """
    setup_logging(
        verbose=args.verbose,
        debug=args.debug,
    )
    logger.info("Started script...")
    logger.debug(f"CLI options: {args}")
    results = {}
    results['single_paired'] = infer_single_paired.infer(
        file_1=args.file_1,
        file_2=args.file_2,
    )
    logger.info(f"Results: {results}")
    logger.info("Done.")


if __name__ == "__main__":
    main(args=parse_args())