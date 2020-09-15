# coding：utf-8
import unittest
import main_test


class test_main(unittest.TestCase):
    def setUp(self):
        print("开始测试:")

    def tearDown(self):
        print("测试结束")

    def test_orig(self):
        print("正在测试orig.txt的查重率")
        main_test.main_solve('sim_0.8\orig.txt', 'sim_0.8\orig.txt', 'ans.txt')

    def test_add(self):
        print("正在测试orig_0.8_add.txt的查重率")
        main_test.main_solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_add.txt', 'ans.txt')

    def test_del(self):
        print("正在测试orig_0.8_del.txt的查重率")
        main_test.main_solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_del.txt', 'ans.txt')

    def test_orig_1(self):
        print("正在测试orig_0.8_dis_1.txt的查重率")
        main_test.main_solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_1.txt', 'ans.txt')

    def test_orig_3(self):
        print("正在测试orig_0.8_dis_3.txt的查重率")
        main_test.main_solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_3.txt', 'ans.txt')

    def test_orig_7(self):
        print("正在测试orig_0.8_dis_7.txt的查重率")
        main_test.main_solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_7.txt', 'ans.txt')

    def test_orig_10(self):
        print("正在测试orig_0.8_dis_10.txt的查重率")
        main_test.main_solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_10.txt', 'ans.txt')

    def test_orig_15(self):
        print("正在测试orig_0.8_dis_15.txt的查重率")
        main_test.main_solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_dis_15.txt', 'ans.txt')

    def test_mix(self):
        print("正在测试orig_0.8_mix.txt的查重率")
        main_test.main_solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_mix.txt', 'ans.txt')

    def test_rep(self):
        print("正在测试orig_0.8_rep.txt的查重率")
        main_test.main_solve('sim_0.8\orig.txt', 'sim_0.8\orig_0.8_rep.txt', 'ans.txt')


if __name__ == '__main__':
    unittest.main()