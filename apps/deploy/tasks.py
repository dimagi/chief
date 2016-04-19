import logging

from fabric.network import disconnect_all
from fabric.api import execute

# HQ's fabfile
from fab import fabfile


def captain_deploy(deploy):
    try:
        if deploy.code_branch:
            fabfile.env.code_branch = deploy.code_branch
        fabfile.env.captain_user = deploy.user
        execute(getattr(fabfile, deploy.env))
        execute(fabfile.awesome_deploy, confirm='no')
    except Exception, e:
        logging.exception(e)
        deploy.success = False
    else:
        deploy.success = True
    finally:
        disconnect_all()
        deploy.in_progress = False
        deploy.complete = True
        deploy.save()
