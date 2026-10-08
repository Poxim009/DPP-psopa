#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Rush 00 - ex00: Checkmate
โปรแกรมตรวจสอบว่าคิง (King 'K') กำลังถูกรุก (Check) หรือไม่
ตามข้อกำหนดของ 42 Bangkok Python Discovery Piscine
"""


def checkmate(board):
    """
    ตรวจสอบว่าคิง (King: 'K') บนกระดานหมากรุกกำลังถูกรุก (Check) หรือไม่

    พารามิเตอร์:
        board (str): สตริงหลายบรรทัดที่แสดงกระดานหมากรุกแบบ N x N

    การทำงาน:
        - หากคิงถูกรุกโดยตัวหมากฝ่ายตรงข้าม (P, B, R, Q) -> พิมพ์ "Success"
        - หากคิงปลอดภัย (ไม่ถูกรุก) -> พิมพ์ "Fail"
        - หากข้อมูลกระดานไม่ถูกต้อง (ไม่ใช่สตริง, ว่างเปล่า, ไม่เป็นสี่เหลี่ยม,
          ไม่มีคิง หรือมีคิงมากกว่า 1 ตัว) -> คืนค่ากลับทันที
    """
    # 1. ตรวจสอบชนิดข้อมูล: ต้องเป็นสตริงเท่านั้น และไม่เป็นสตริงว่าง
    if not isinstance(board, str) or not board:
        return

    # 2. ตัด newline นำหน้าที่อาจเกิดจาก multiline string
    #    (เช่น """\n) ออกเพียง 1 ครั้ง โดยไม่ใช้ strip() ทั้งหมด
    #    เพื่อไม่ให้กลืนแถวว่างที่ผิดรูปตรงต้นหรือท้ายกระดาน
    if board.startswith('\r\n'):
        cleaned_board = board[2:]
    elif board.startswith('\n') or board.startswith('\r'):
        cleaned_board = board[1:]
    else:
        cleaned_board = board

    rows = cleaned_board.splitlines()
    size = len(rows)

    # 3. กระดานต้องมีขนาดอย่างน้อย 1x1
    if size == 0:
        return

    # 4. ตรวจสอบว่ากระดานเป็นสี่เหลี่ยมจัตุรัส (N x N) หรือไม่
    #    ทุกแถวต้องมีความยาวเท่ากับจำนวนแถว (size) พอดี
    for row in rows:
        if len(row) != size:
            return

    # 5. ตรวจสอบจำนวนคิง ('K'): ต้องมีคิงอยู่บนกระดานเพียงตัวเดียวเท่านั้น
    king_count = sum(row.count('K') for row in rows)
    if king_count != 1:
        return

    # 6. ค้นหาตำแหน่งพิกัดของคิง (king_row, king_col)
    king_row = -1
    king_col = -1
    for r in range(size):
        c = rows[r].find('K')
        if c != -1:
            king_row = r
            king_col = c
            break

    # 7. กำหนดตัวหมากและทิศทางการเดิน
    # ตัวหมากของฝ่ายตรงข้าม:
    # - 'P' (Pawn): โจมตีทแยงขึ้นบน (row - 1, col - 1) และ (row - 1, col + 1)
    # - 'B' (Bishop): เดินและโจมตี 4 ทิศทางในแนวทแยง
    # - 'R' (Rook): เดินและโจมตี 4 ทิศทางในแนวตั้งและแนวนอน (Orthogonal)
    # - 'Q' (Queen): เดินและโจมตีได้ทั้ง 8 ทิศทาง (ทแยง + ตั้ง + นอน)
    # ตัวอักษรอื่นๆ (เช่น '.') ถือเป็นช่องว่าง ไม่ขัดขวางสายตา

    enemy_pieces = {'P', 'B', 'R', 'Q'}

    # ตรวจสอบ 4 ทิศทางในแนวตั้งและแนวนอน (Orthogonal directions)
    orthogonal_dirs = [
        (-1, 0),  # ขึ้นบน
        (1, 0),   # ลงล่าง
        (0, -1),  # ไปทางซ้าย
        (0, 1)    # ไปทางขวา
    ]

    for dr, dc in orthogonal_dirs:
        step = 1
        while True:
            r = king_row + dr * step
            c = king_col + dc * step

            # หากหลุดขอบกระดาน ให้หยุดการค้นหาในทิศทางนี้
            if not (0 <= r < size and 0 <= c < size):
                break

            piece = rows[r][c]
            if piece in enemy_pieces:
                # พบตัวหมากแรกในแนวสายตา
                # Rook ('R') หรือ Queen ('Q') สามารถโจมตีคิงในแนวนี้ได้
                if piece in {'R', 'Q'}:
                    print("Success")
                    return
                # หากเป็นตัวหมากอื่น (P หรือ B) จะไม่สามารถโจมตีในแนวนี้ได้
                # และจะทำหน้าที่เป็นสิ่งกีดขวางตัวหมากด้านหลัง
                break

            step += 1

    # ตรวจสอบ 4 ทิศทางในแนวทแยง (Diagonal directions)
    diagonal_dirs = [
        (-1, -1),  # ทแยงซ้ายบน
        (-1, 1),   # ทแยงขวาบน
        (1, -1),   # ทแยงซ้ายล่าง
        (1, 1)     # ทแยงขวาล่าง
    ]

    for dr, dc in diagonal_dirs:
        step = 1
        while True:
            r = king_row + dr * step
            c = king_col + dc * step

            # หากหลุดขอบกระดาน ให้หยุดการค้นหาในทิศทางนี้
            if not (0 <= r < size and 0 <= c < size):
                break

            piece = rows[r][c]
            if piece in enemy_pieces:
                # พบตัวหมากแรกในแนวสายตาทแยง
                # Bishop ('B') หรือ Queen ('Q') โจมตีได้ในทุกระยะ
                if piece in {'B', 'Q'}:
                    print("Success")
                    return

                # สำหรับ Pawn ('P'):
                # เบี้ยจะโจมตีทแยงขึ้นบน (pawn_row - 1, pawn_col ± 1)
                # เบี้ยที่โจมตีคิงได้ ต้องห่าง 1 ช่อง (step == 1)
                # และอยู่แถวด้านล่างคิง (dr == 1 คือ pawn_row = king_row + 1)
                if piece == 'P':
                    if step == 1 and dr == 1:
                        print("Success")
                        return

                # ตัวหมากใดๆ ที่พบจะบังสายตาของตัวหมากด้านหลังเสมอ
                break

            step += 1

    # หากไม่มีตัวหมากฝ่ายตรงข้ามใดๆ สามารถโจมตีคิงได้
    print("Fail")
