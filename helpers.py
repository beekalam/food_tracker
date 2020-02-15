from flask import request, g
import os
import sys
from datetime import datetime


def is_post():
    return request.method == 'POST'


def is_get():
    return request.method == 'GET'


def log(string):
    print("[] {} {}".format(os.linesep, string), file=sys.stdout)


def database_date(date):
    dt = datetime.strptime(date, '%Y-%m-%d')
    return datetime.strftime(dt, '%Y%m%d')


def pretty_date(date):
    d = datetime.strptime(str(date), '%Y%m%d')
    return datetime.strftime(d, '%B %d, %Y')
