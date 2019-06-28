import mygame
import unittest
board = [[0, 2,  1], [0, 2, 1], [1, 1, 2]]
# проверка правильности результата Bool True
# проверка количества строк True
# проверка количества рядов True
board_false = [[0, 2,  1], [3, 2, 1], [1, 1, 2]]#проверка правильности заполнения игрового поля True
board_task = [[0, 2,  1], [1, 2, 1], [1, 2, 2]] # проверка правильности заполнения в соответствии сзаданием True

class MyGameTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("[имитируется бурная деятельность настройки]")
        print("v" * 30)

    @classmethod
    def tearDownClass(cls):
        print("^" * 30)
        print("[здесь мы всё подчистили типа]")

    def setUp(self):
        print(f"Подготовка к запуску {self.shortDescription()}")

    def tearDown(self):
        print(f"Очистка после прогона {self.id()}")
        print("---")

    def test_validate_board_result_true(self):
        """проверка правильности результата Bool True """
        self.assertTrue(mygame.validate_board(board), bool)

    def test_check_ryd_result_true(self):
        """проверка количества строк True """
        self.assertTrue(mygame.validate_board(board) is True)

    def test_check_line_result_true(self):
        """проверка количества рядов True """
        self.assertTrue(mygame.validate_board(board) is True)


    def test_check_right_result_true(self):
        """проверка правильности заполнения игрового поля True """
        self.assertFalse(mygame.validate_board(board_false) is True)

    def test_check_task_result_true(self):
        """проверка правильности заполнения в соответствии сзаданием True """
        self.assertFalse(mygame.validate_board(board_task) is True)

