#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Does the following:
1. Generates and saves random secret key to .env in the repo root dir.

A portion of this code was adopted from Django's standard crypto functions and
utilities, specifically:
    https://github.com/django/django/blob/master/django/utils/crypto.py
"""

import random

ENV_PATH = ".env"


def get_random_string(
        length=50,
        allowed_chars='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'):
    """
    Returns a securely generated random string.
    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits
    """

    return ''.join(random.choice(allowed_chars) for i in range(length))


def append_to_env(line):
    with open(ENV_PATH, 'a') as f:
        f.write(line)


# 1. Save the secret key
append_to_env("DJANGO_SECRET_KEY=%s\n" % get_random_string())

# 2. Save Postgres password
append_to_env("POSTGRES_PASSWORD=%s\n" % get_random_string(length=20))
