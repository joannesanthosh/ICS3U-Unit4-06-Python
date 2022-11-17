#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Nov 2022
# This program uses a nested loop


def main():
    # this function uses a nested loop
    for i in range(256):
        for j in range(256):
            for k in range(256):
                print("RGB({0},{1},{2})".format(i, j, k))


if __name__ == "__main__":
    main()
