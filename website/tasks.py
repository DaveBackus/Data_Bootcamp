from invoke import run, task

@task
def dev():
    run("hugo server")

@task
def publish():
    run("hugo")
    run("ghp-import -n -p public")
