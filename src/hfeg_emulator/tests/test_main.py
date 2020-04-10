from src.hfeg_emulator.main import get_random_power


class TestGetRandomPower:

    def test__valid_input(self):
        result = get_random_power(100)

        assert 0 < result < 100
