#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call

call(["mv", "dotgitignore", ".gitignore"])
print("******* Installling node modules:")
call(["npm", "install"])
print("******* Node modules installed.")
call("bower", "install")
print("******* bower packages installed.")
