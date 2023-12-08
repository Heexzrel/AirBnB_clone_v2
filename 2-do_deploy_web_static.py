#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""
from fabric.api import local, env, put, run
from datetime import datetime
import os

env.hosts = ['18.206.208.154', '100.26.236.42']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """
    generating .tgz archive from my web_static folder
    """
    try:
        local("mkdir -p versions")

        now = datetime.now().strftime("%Y%m%d%H%M%S")
        name = "web_static_{}.tgz".format(now)

        local(f"tar -cvzf versions/{name} web_static/")

        return f"versions/{name}"
    except Exception:
        return None


def do_deploy(archive_path):
    """
    distributing archive to web server
    """
    if not os.path.exists(archive_path):
        return False
    try:
        fname = archive_path.split("/")[-1]
        name = fname.split(".")[0]
        path = f"/data/web_static/releases/{name}/"
        put(archive_path, '/tmp/')
        run(f"mkdir -p {path}")
        run(f"tar -xzf /tmp/{fname} -C {path}")
        run(f"rm /tmp/{fname}")
        run(f"mv {path}web_static/* {path}")
        run(f"rm -rf {path}web_static")
        run('rm -rf /data/web_static/current')
        run(f"ln -s {path} /data/web_static/current")
        return True
    except Exception:
        return False
