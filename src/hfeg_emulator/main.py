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


def get_resistance_value(argv: list) -> int:
    """
    Возвращает числовое значение сопротивления.

    ::
    """
    if len(argv) != 2:
        logger.error('\nError. Must be: {name} resistance_value\n'.format(name=argv[0]))
        sys.exit(1)

    _, resistance = argv

    try:
        resistance_value = int(resistance)
    except ValueError:
        logger.error('Error: resistance must be int')
        sys.exit(2)

    return resistance_value


if __name__ == '__main__':
    resistance_value = get_resistance_value(sys.argv)
    power_value = get_random_power(resistance_value)
    print(power_value)
