import unittest
import mainCode

class TestEval(unittest.TestCase):
    def testEval01(self):
        self.assertEqual(([7,7,7,56],['*','+','=']),mainCode.eval([7,7,7],['*',"+"]))
    def testEval02(self):
        self.assertEqual(([7,7,7,56],['*','+','=']),mainCode.eval([7,7,7],['*',"+"]))
    def testEval03(self):
        self.assertEqual(([7,7,7,56],['*','+','=']),mainCode.eval([7,7,7],['*',"+"]))
    def testEval04(self):
        self.assertEqual(([7,7,7,56],['*','+','=']),mainCode.eval([7,7,7],['*',"+"]))
    def testEval05(self):
        self.assertEqual(([7,7,7,56],['*','+','=']),mainCode.eval([7,7,7],['*',"+"]))
    def testEval06(self):
        self.assertEqual(([7,7,7,56],['*','+','=']),mainCode.eval([7,7,7],['*',"+"]))
    def testEval07(self):
        self.assertEqual(([7,7,7,56],['*','+','=']),mainCode.eval([7,7,7],['*',"+"]))
    def testEval08(self):
        self.assertEqual(([7,7,7,56],['*','+','=']),mainCode.eval([7,7,7],['*',"+"]))
    def testEval09(self):
        self.assertEqual(([7,7,7,56],['*','+','=']),mainCode.eval([7,7,7],['*',"+"]))
    def testEval10(self):
        self.assertEqual(([7,7,7,56],['*','+','=']),mainCode.eval([7,7,7],['*',"+"]))
    def testEval11(self):
        self.assertEqual(([7,7,7,],['*','+','=']),mainCode.eval([7,7,7],['*',"+"]))
    def testEval12(self):
        self.assertEqual(([7,7,7,],['*','+','=']),mainCode.eval([7,7,7],['*',"+"]))
    def testEval13(self):
        self.assertEqual(([7,7,7,],['*','+','=']),mainCode.eval([7,7,7],['*',"+"]))
    def testEval14(self):
        self.assertEqual(([7,7,7,],['*','+','=']),mainCode.eval([7,7,7],['*',"+"]))


def main():

    suite = unittest.TestLoader().loadTestsFromTestCase(TestEval)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()