#!/usr/bin/python3
# generating a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Creating a tar gzipped archive of the directory web_static."""
    d_t = datetime.utcnow()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(d_t.year,
                                                            d_t.month,
                                                            d_t.day,
                                                            d_t.hour,
                                                            d_t.minute,
                                                            d_t.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_name)).failed is True:
        return None
    return file_name
