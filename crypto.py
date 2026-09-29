import argparse

from caesar import encrypt, decrypt


parser = argparse.ArgumentParser()


#python crypto.py <cipher> <mode> [key arguments] [--in FILE] [--out FILE] [--lang en|es]

parser.add_argument("cipher")
parser.add_argument("mode")
parser.add_argument("--key")
parser.add_argument("--in", dest="infile")
parser.add_argument("--out", dest="outfile")
parser.add_argument("--lang", choices=["en","es"], default="en")

args = parser.parse_args()


if args.cipher == "caesar":
    args.key_arguments[0]
    if args.mode == "encrypt":
        args.infile
        args.key
    elif args.mode == "decrypt":