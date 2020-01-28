from contextlib import suppress
from src.tic_tac_toe import main


if __name__ == '__main__':
    with suppress(KeyboardInterrupt, EOFError):
        main()
    print('\nfim :D')
