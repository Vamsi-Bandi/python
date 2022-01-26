def isValidChessBoard(input):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    
    if 'bking' not in input.values() or 'wking' not in input.values():
        print('There should be Black and white King')
        return False
    
    for a in input.values():
        whites = 0
        blacks = 0
        if a[0] == 'w':
            whites += 1
        if a[0] == 'b':
            blacks += 1
        if whites > 16 or blacks > 16:
            print('Whites/Blacks should not be more than 16')
            return False
    
    for a in input.values():
        bpawns = 0
        wpawns = 0
        if a == 'bpawn':
            bpawns += 1
        if a == 'wpawn':
            wpawns += 1
        if bpawns > 8 or wpawns > 8:
            print('whites/Blacks pawns should ne less than 8')
            return False
    
    for a in input:
        if a[0] not in numbers or a[1] not in alphabets:
            print('Valid space 1a to 8h')
            return False
            
    for a in input.values():
        if a[0] != 'w' and a[0] != 'b':
            print('Pieces should be white or Black')
            False
        if a[1:] not in pieces:
            print('Pieces should be ' + str(pieces))
            False
    return True

input = {'1h':'bking' , '6c':'wqueen' , '2g':'bbishop' , '5h':'bqueen' , '3e':'wking'}
print(isValidChessBoard(input))
