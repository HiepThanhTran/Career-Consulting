#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlueCC.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# class SecureHTTPServer(ThreadedWSGIServer):
#     def __init__(self, address, handler_cls, certificate, key, ipv6=False):
#         super(SecureHTTPServer, self).__init__(address, handler_cls, ipv6=ipv6)
#         context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#         context.load_cert_chain(certfile=certificate, keyfile=key)
#         self.socket = context.wrap_socket(self.socket, server_side=True)
