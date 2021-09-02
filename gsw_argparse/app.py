#! /usr/bin/env python3
import argparse
import sys


def check_arg(args=None):
    parser = argparse.ArgumentParser(
        description='Script to learn basic Argparse')

    parser.add_argument('-H', '--host',
                        help='host ip',
                        required='True',
                        default='localhost')

    parser.add_argument('-p', '--port',
                        help='port of the host',
                        required='True',
                        default='30777')

    parser.add_argument('-u', '--user',
                        help='user name',
                        required='True',
                        default='root')

    parser.add_argument('-c', '--command',
                        help='task to run',
                        required='True')

    parser.add_argument('-k', '--key',
                        nargs=2,
                        help='private key and passphrase (if available)',
                        )

    parser.add_argument('-P', '--password',
                        help='login password',
                        )

    results = parser.parse_args(args)

    return (results.host,
            results.port,
            results.user,
            results.command,
            results.key,
            results.password)


if __name__ == '__main__':
    h, p, u, c, k, P = check_arg(sys.argv[1:])
    print("h = {}".format(h))
    print("p = {}".format(p))
    print("u = {}".format(u))
    print("c = {}".format(c))
    print("k = {}".format(k))
    print("P = {}".format(P))
