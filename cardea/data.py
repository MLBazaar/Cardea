# -*- coding: utf-8 -*-

"""
Data Management module.
This module contains functions that allow downloading demo data from Amazon S3
The demo data is a modified version of the missed appointment data found here:
https://www.kaggle.com/joniarroba/noshowappointments
Another demo data is also available for mimic dataset:
https://physionet.org/files/mimiciii-demo/1.4/
"""

import logging
import os
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

import pandas as pd

LOGGER = logging.getLogger(__name__)

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'data'
)
BUCKET = 'dai-cardea'
S3_URL = 'https://{}.s3.amazonaws.com/{}'

DEMO_DATA = ("kaggle", "mimic", "dummy")


def download(name, data_path=DATA_PATH):
    """Download demo data with the given name from S3.

    If the data has never been loaded before, it will be downloaded
    from the [dai-cardea bucket](https://dai-cardea.s3.amazonaws.com) or
    the S3 bucket specified following the `s3://{bucket}/path/to/the.csv` format,
    and then cached inside the `data` folder, within the `cardea` package
    directory, and then returned.

    Otherwise, if it has been downloaded and cached before, it will be directly
    loaded from the `cardea/data` folder without contacting S3.

    Args:
        name (str): Name of demo data

    Returns:
        str:
            path to the downloaded data
    """
    if name not in DEMO_DATA:
        raise KeyError("unknown demo data {}".format(name))

    data_path = os.path.join(data_path, name)

    if not os.path.exists(data_path):
        os.makedirs(data_path, exist_ok=True)
        url = S3_URL.format(BUCKET, '{}.zip'.format(name))
        compressed = ZipFile(BytesIO(urlopen(url).read()))

        LOGGER.info('Downloading dataset %s from %s', name, url)

        for file in compressed.namelist():
            filename = os.path.join(data_path, file)
            csv_file = compressed.open(file, 'r')

            data = pd.read_csv(csv_file, dtype=str, encoding="utf-8")
            data.to_csv(filename, index=False)

    return data_path
