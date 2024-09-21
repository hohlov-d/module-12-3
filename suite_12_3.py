import unittest
import module_12_1_test as mod
import module_12_2_test as md

testST = unittest.TestSuite()
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(mod.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(md.TournamentTest))

rn = unittest.TextTestRunner(verbosity=2)
rn.run(testST)

