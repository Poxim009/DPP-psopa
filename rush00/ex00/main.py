#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Rush 00 - ex00: main.py
ตัวอย่างการทดสอบฟังก์ชัน checkmate ตาม Subject
- Example 1: ควรแสดงผล "Success"
- Example 2: ควรแสดงผล "Fail"
"""

from checkmate import checkmate


def main():
    # Example 1: กระดานขนาด 4x4 (Pawn ที่ (2,2) รุก King ที่ (1,1)) -> Success
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)

    # Example 2: กระดานขนาด 2x2 (มีเพียง King ตัวเดียว ไม่ถูกรุก) -> Fail
    board2 = """\
..
.K\
"""
    checkmate(board2)


if __name__ == "__main__":
    main()
