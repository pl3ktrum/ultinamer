from . import walker

import argparse


def main():
    parser = argparse.ArgumentParser(description="tidy up your mess!")
    parser.add_argument("source destination", type=str)

if __name__ == "__main__":
    main()
