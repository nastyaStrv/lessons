import unittest
from unittest import TestCase
from runner import Runner


class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner('Mark')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
        print('OK')

    def test_run(self):
        runner = Runner('Mia')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
        print('Test OK')

    def test_challenge(self):
        runner_1 = Runner('Rob')
        runner_2 = Runner('Flik')
        for i in range(10):
            if i % 2 == 0:
                runner_1.run()
            else:
                runner_2.walk()
            self.assertNotEqual(runner_1.distance, runner_2.distance)
            print('Test OK')
