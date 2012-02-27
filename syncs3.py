#!/usr/bin/python
"""
A wrapper around dgsync that provides logging and syncing of multiple 
directories/buckets.
Copyright (C) 2012  Aaron Godfrey

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import logging
import logging.handlers
import subprocess


LOG_FILE = ""
DGTOOLS_ACCESS_KEY = ""
DGTOOLS_SECRET_KEY = ""
BUCKETS = {}


def setup_logger():
    """
    Sets up and returns a logger
    """
    logger = logging.getLogger('syncs3')
    logger.setLevel(logging.DEBUG)

    # Set up rotatiting logger which creates a new log file when
    # it exceeds 10mb up to 5 backup logs.
    handler = logging.handlers.RotatingFileHandler(LOG_FILE,
        maxBytes=10485760, backupCount=5)
    # Set up formatting for the log file
    formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def main():
    logger = setup_logger()
    cmd_template = "dgsync -A %s -S %s --verbose --dont-delete %s %s"
    for target_dir, local_dir in BUCKETS.items():
        cmd = cmd_template % (DGTOOLS_ACCESS_KEY, DGTOOLS_SECRET_KEY, 
            local_dir, target_dir)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            logger.error(error)
        else:
            logger.info(output)


if __name__ == "__main__":
    main()
