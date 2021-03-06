from __future__ import absolute_import
import os
import socket

try:
    from django.conf import settings
except ImportError:
    settings = None

from .client import StatsClient
from ._version import __version__


__all__ = ['StatsClient', 'statsd']

statsd = None

if settings:
    try:
        host = getattr(settings, 'STATSD_HOST', 'localhost')
        port = getattr(settings, 'STATSD_PORT', 8125)
        prefix = getattr(settings, 'STATSD_PREFIX', None)
        suffix = getattr(settings, 'STATSD_SUFFIX', None)
        statsd = StatsClient(host, port, prefix, suffix)
    except (socket.error, socket.gaierror, ImportError):
        pass
elif 'STATSD_HOST' in os.environ:
    try:
        host = os.environ['STATSD_HOST']
        port = int(os.environ['STATSD_PORT'])
        prefix = os.environ.get('STATSD_PREFIX')
        suffix = os.environ.get('STATSD_SUFFIX')
        statsd = StatsClient(host, port, prefix, suffix)
    except (socket.error, socket.gaierror, KeyError):
        pass
