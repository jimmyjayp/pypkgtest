#!/usr/bin/env python3

# export PYTHONPATH=.../pypkgtest

import parentpkg.parentA
import parentpkg.parentB
import parentpkg.childpkg

parentpkg.parentA.funcA()
parentpkg.parentB.funcB()
parentpkg.childpkg.funcA()
parentpkg.childpkg.funcB()
parentpkg.childpkg.funcB2()
