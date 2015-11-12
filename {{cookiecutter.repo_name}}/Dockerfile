FROM django:1.8-python3

# Needed for Pillow jpeg support:
RUN apt-get update && apt-get install -y \
        libjpeg-dev \
        zlib1g-dev \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

MAINTAINER Urga Creatieve Communicatie <dries@urga.be>

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Uncomment next line to copy an ssh key to be able to deploy from private repo's
# Not an ideal solution, as the key is kept in the image and retrievable by anyone who has access to the image.
# Therefor, it's recommended to use a read-only deploy key, to limit the damage.
# ADD ssh/gitlab_deploy /root/.ssh/id_rsa

# First add only the requirements, bacause if requirements haven't changed between builds,
# we can make use of the docker cache.
ADD requirements.txt /usr/src/app/
RUN pip install --no-cache -r requirements.txt

# copy the current code
ADD . /usr/src/app/

CMD ["/usr/local/bin/gunicorn", "--access-logfile", "-", "--error-logfile", "-", "{{ cookiecutter.repo_name }}.wsgi", "-b", "0.0.0.0:8000"]
