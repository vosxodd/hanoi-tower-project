from functools import lru_cache

def move_discs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        move_discs(num - 1, from_peg, temp_peg, to_peg)
        print('Переложить диск с', from_peg, 'на', to_peg)
        move_discs(num - 1, temp_peg, to_peg, from_peg)


@lru_cache(maxsize=None)
def main():
    num_discs = int(input('Сколько дисков на первом стержне? '))
    from_peg = 1
    to_peg = 3
    temp_peg = 2
    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print('Все кольца перемещены! ')
    
if __name__ == '__main__':  
    main()
