FROM django:1.8-python3

MAINTAINER Urga Creatieve Communicatie <dries@urga.be>

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy ssh deploy key to be able to deploy from private repo's:
ADD .ssh /root/.ssh/

# First add only the requirements, bacause if requirements haven't changed between builds,
# we can make use of the docker cache.
ADD requirements.txt /usr/src/app/
RUN pip install --no-cache -r requirements.txt

# copy the current code
ADD . /usr/src/app/

CMD ["/usr/local/bin/gunicorn", "--access-logfile", "-", "--error-logfile", "-", "{{ cookiecutter.repo_name }}.wsgi", "-b", "0.0.0.0:8000"]
