import unittest
import os

from lesson05.home_work import easy


class TestEasyHw(unittest.TestCase):

    def testMkdir(self):
        for dir in self.getTestDirPaths():
            easy.mkdir(dir)
            self.assertTrue(os.path.exists(dir))
        with self.assertRaises(FileNotFoundError):
            easy.mkdir('')

    def testRm(self):
        for dir in self.getTestDirPaths():
            easy.rm(dir)
            self.assertFalse(os.path.exists(dir))

    def testLs(self):
        for dir in self.getTestDirPaths():
            easy.mkdir(dir)
        dir_list = easy.ls('.')
        for dir in self.getTestDirs():
            self.assertTrue(dir in dir_list)
        for dir in self.getTestDirPaths():
            easy.rm(dir)

        with self.assertRaises(FileNotFoundError):
            easy.ls('')

    def getTestDirs(self):
        dirs = (
            'ttt',
            'ttt1',
            'ttt2',
            'ttt3',
        )
        return dirs

    def getTestDirPaths(self):
        return map(lambda name: os.getcwd() + '/' + name, self.getTestDirs())


if __name__ == '__main__':
    unittest.main()
