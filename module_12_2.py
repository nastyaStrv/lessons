import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = [
            Runner("Усейн", 10),
            Runner("Андрей", 9),
            Runner("Ник", 3)]

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_usain_and_nick(self):
        turn_1 = Tournament(90, self.runners[0], self.runners[2])
        result = turn_1.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Результат Усейна и Ника"] = result

    def test_andrey_and_nick(self):
        turn_2 = Tournament(90, self.runners[1], self.runners[2])
        result = turn_2.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Результат Андрея и Ника"] = result

    def test_usain_andrey_nick(self):
        turn_3 = Tournament(90, *self.runners)
        result = turn_3.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Результат общего забега"] = result

    if __name__ == "__main__":
        unittest.main()
