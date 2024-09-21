import module12_2 as mod
import unittest


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.h1 = mod.Runner('Usejn', 10)
        self.h2 = mod.Runner('Andrew', 9)
        self.h3 = mod.Runner('Nick', 3)

    @classmethod
    def tearDownClass(cls):

        for test_key, test_value in cls.all_result.items():
            print(f'Тест: {test_key}')
            key_position = 1
            for key, value in test_value.items():
                print(f'\t{key_position}: {value.name}')
                key_position += 1

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_turn1(self):
        turn_1 = mod.Tournament(90, self.h1, self.h3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Nick')
        self.all_result['Результат 1-го забега'] = result

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_turn2(self):
        turn_2 = mod.Tournament(90, self.h2, self.h3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Nick')
        self.all_result['Результат 2-го забега'] = result

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_turn3(self):
        turn_3 = mod.Tournament(90, self.h1, self.h2, self.h3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Nick')
        self.all_result['Результат 3-го забега'] = result


if __name__ == '__main__':
    unittest.main()
