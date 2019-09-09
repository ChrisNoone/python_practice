# coding: utf-8

import hashlib


def md5_encode(s):
    md = hashlib.md5()
    md.update(s.encode())
    return md.hexdigest()
