import unittest
import mainCode

class TestEval(unittest.TestCase):
    def testEval01(self):
        self.assertEqual(([5,55,555,615],['+','+','=']),mainCode.eval([5,55,555],['+',"+"]))
    def testEval02(self):
        self.assertEqual(([5,55,555,-495],['+','-','=']),mainCode.eval([5,55,555],['+',"-"]))
    def testEval03(self):
        self.assertEqual(([5,55,555,5],['+','/','=']),mainCode.eval([5,55,555],['+',"/"]))
    def testEval04(self):
        self.assertEqual(([5,55,555,30530],['+','*','=']),mainCode.eval([5,55,555],['+',"*"]))
    def testEval05(self):
        self.assertEqual(([5,55,555,505],['-','+','=']),mainCode.eval([5,55,555],['-',"+"]))
    def testEval06(self):
        self.assertEqual(([5,55,555,-605],['-','-','=']),mainCode.eval([5,55,555],['-',"-"]))
    def testEval07(self):
        self.assertEqual(([5,55,555,5],['-','/','=']),mainCode.eval([5,55,555],['-',"/"]))
    def testEval08(self):
        self.assertEqual(([5,55,555,-30520],['-','*','=']),mainCode.eval([5,55,555],['-',"*"]))
    def testEval09(self):
        self.assertEqual(([5,55,555,830],['*','+','=']),mainCode.eval([5,55,555],['*',"+"]))
    def testEval10(self):
        self.assertEqual(([5,55,555,-280],['*','-','=']),mainCode.eval([5,55,555],['*',"-"]))
    def testEval11(self):
        self.assertEqual(([5,55,555,152625],['*','*','=']),mainCode.eval([5,55,555],['*',"*"]))
    def testEval12(self):
        self.assertEqual(([5,55,555,0],['*','/','=']),mainCode.eval([5,55,555],['*',"/"]))
    def testEval13(self):
        self.assertEqual(([5,55,555,555],['/','+','=']),mainCode.eval([5,55,555],['/',"+"]))
    def testEval14(self):
        self.assertEqual(([5,55,555,-555],['/','-','=']),mainCode.eval([5,55,555],['/',"-"]))
    def testEval15(self):
        self.assertEqual(([5,55,555,0],['/','/','=']),mainCode.eval([5,55,555],['/',"/"]))
    def testEval16(self):
        self.assertEqual(([5,55,555,0],['/','*','=']),mainCode.eval([5,55,555],['/',"*"]))
    def testEval17(self):
        self.assertEqual(("Cant divide by 0 :("),mainCode.eval([5,0,555],['/',"*"]))
    def testEval18(self):
        self.assertEqual(("Cant divide by 0 :("),mainCode.eval([5,55,0],['+',"/"]))


def main():

    suite = unittest.TestLoader().loadTestsFromTestCase(TestEval)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()