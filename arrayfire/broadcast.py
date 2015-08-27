#######################################################
# Copyright (c) 2015, ArrayFire
# All rights reserved.
#
# This file is distributed under 3-clause BSD license.
# The complete license agreement can be obtained at:
# http://arrayfire.com/licenses/BSD-3-Clause
########################################################


class _bcast(object):
    _flag = False
    def get(self):
        return bcast._flag

    def set(self, flag):
        bcast._flag = flag

    def toggle(self):
        bcast._flag ^= True

bcast = _bcast()

def broadcast(func, *args):

    def wrapper(*func_args):
        bcast.toggle()
        res = func(*func_args)
        bcast.toggle()
        return res

    if len(args) == 0:
        return wrapper
    else:
        return wrapper(*args)