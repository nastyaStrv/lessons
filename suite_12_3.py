import unittest
from module_12_2 import TournamentTest
from module_12_1 import RunnerTest

run_RunnerTest = unittest.TestSuite()
run_RunnerTest.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
tour_TournamentTest = unittest.TestSuite()
tour_TournamentTest.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_RunnerTest)
runner.run(tour_TournamentTest)


