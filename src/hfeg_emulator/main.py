import argparse
import logging
from random import randint
import sys


logger = logging.getLogger(__name__)


def get_random_power(resistance: int) -> int:
    """
    Возвращает случайное значение в диапазоне от 0 до resistance.

    :param resistance: числовое значение сопротивления

    :return: случайное значение мощности
    """
    return randint(0, resistance)


def parse_args(args=sys.argv[1:]):
    """
    Парсит аргументы командной строки.
    """
    parser = argparse.ArgumentParser(description=sys.modules[__name__].__doc__)

    grp = parser.add_argument_group('Hfeg emulator settinigs')
    grp.add_argument(
        '--resistance',
        metavar='N',
        default=0,
        type=int,
        help='Integer value of resistance'
    )

    return parser.parse_args(args)


def main():
    options = parse_args()
    power_value = get_random_power(options.resistance)
    print(power_value)


if __name__ == '__main__':
    main()
