import unittest
from task import conv_num, my_datetime, conv_endian


class TestCase(unittest.TestCase):

    def test_conv_num_1(self):
        str_number = '12345'
        expected_output = 12345
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_2(self):
        str_number = '-12345'
        expected_output = -12345
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_2b(self):
        str_number = '0'
        expected_output = 0
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_2c(self):
        str_number = '-0'
        expected_output = 0
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_3(self):
        str_number = '123..'
        expected_output = None
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_4(self):
        str_number = '123.'
        expected_output = 123.0
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_5(self):
        str_number = '12.3.45'
        expected_output = None
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_6(self):
        str_number = 15
        expected_output = None
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_7(self):
        str_number = "12.34"
        expected_output = 12.34
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_8(self):
        str_number = '0.58'
        expected_output = 0.58
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_9(self):
        str_number = '89546548.213151321'
        expected_output = 89546548.213151321
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_10(self):
        str_number = '-65454.121212'
        expected_output = -65454.121212
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_11(self):
        str_number = '-'
        expected_output = None
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_12(self):
        str_number = '-34343-34343'
        expected_output = None
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_13(self):
        str_number = '34343-'
        expected_output = None
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_14(self):
        str_number = '34 343'
        expected_output = None
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_15(self):
        str_number = ' 34343'
        expected_output = None
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_16(self):
        str_number = ' 34343 '
        expected_output = None
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_16b(self):
        str_number = ' 343.43 '
        expected_output = None
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_17(self):
        str_number = '34A.43'
        expected_output = None
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_18(self):
        str_number = '34.4A3'
        expected_output = None
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_19(self):
        str_number = 'AA'
        expected_output = None
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_20(self):
        str_number = '0xAD4'
        expected_output = 2772
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_21(self):
        str_number = '-0xAD4'
        expected_output = -2772
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_22(self):
        str_number = '0x'
        expected_output = None
        self.assertEqual(conv_num(str_number), expected_output)

    def test_conv_num_23(self):
        str_number = '0xAB0xff'
        expected_output = None
        self.assertEqual(conv_num(str_number), expected_output)

    def test_my_datetime_1(self):
        int_seconds = 0
        expected_output = "01-01-1970"
        self.assertEqual(my_datetime(int_seconds), expected_output)

    def test_my_datetime_2(self):
        int_seconds = 60*60*24
        expected_output = "01-02-1970"
        self.assertEqual(my_datetime(int_seconds), expected_output)

    def test_my_datetime_3(self):
        int_seconds = 60*60*24-1
        expected_output = "01-01-1970"
        self.assertEqual(my_datetime(int_seconds), expected_output)

    def test_my_datetime_4(self):
        int_seconds = 60*60*24*31
        expected_output = "02-01-1970"
        self.assertEqual(my_datetime(int_seconds), expected_output)

    def test_my_datetime_5(self):
        int_seconds = 60*60*24*58
        expected_output = "02-28-1970"
        self.assertEqual(my_datetime(int_seconds), expected_output)

    def test_my_datetime_6(self):
        int_seconds = 60*60*24*59
        expected_output = "03-01-1970"
        self.assertEqual(my_datetime(int_seconds), expected_output)

    def test_my_datetime_7(self):
        int_seconds = 60*60*24*364
        expected_output = "12-31-1970"
        self.assertEqual(my_datetime(int_seconds), expected_output)

    def test_my_datetime_8(self):
        int_seconds = 60*60*24*365
        expected_output = "01-01-1971"
        self.assertEqual(my_datetime(int_seconds), expected_output)

    def test_my_datetime_9(self):
        int_seconds = 60 * 60 * 24 * 365 * 2
        expected_output = "01-01-1972"
        self.assertEqual(my_datetime(int_seconds), expected_output)

    def test_my_datetime_10(self):
        int_seconds = 60 * 60 * 24 * (365 * 2 + 58)
        expected_output = "02-28-1972"
        self.assertEqual(my_datetime(int_seconds), expected_output)

    def test_my_datetime_11(self):
        int_seconds = 60 * 60 * 24 * (365 * 2 + 59)
        expected_output = "02-29-1972"
        self.assertEqual(my_datetime(int_seconds), expected_output)

    def test_my_datetime_12(self):
        int_seconds = 60 * 60 * 24 * (365 * 2 + 60)
        expected_output = "03-01-1972"
        self.assertEqual(my_datetime(int_seconds), expected_output)

    def test_my_datetime_13(self):
        int_seconds = 123456789
        expected_output = "11-29-1973"
        self.assertEqual(my_datetime(int_seconds), expected_output)

    def test_my_datetime_14(self):
        int_seconds = 9876543210
        expected_output = "12-22-2282"
        self.assertEqual(my_datetime(int_seconds), expected_output)

    def test_conv_endian_1(self):
        int_number = 57
        str_endian = "something"
        expected_output = None
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_2(self):
        int_number = 57
        str_endian = "biglittle"
        expected_output = None
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_3(self):
        int_number = 57
        str_endian = " big"
        expected_output = None
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_4(self):
        int_number = 57
        str_endian = "little "
        expected_output = None
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_5(self):
        int_number = 5
        str_endian = "big"
        expected_output = "05"
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_6(self):
        int_number = 0
        str_endian = "big"
        expected_output = "00"
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_7(self):
        int_number = 00
        str_endian = "big"
        expected_output = "00"
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_8(self):
        int_number = 000
        str_endian = "big"
        expected_output = "00"
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_9(self):
        int_number = 10
        str_endian = "big"
        expected_output = "0A"
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_10(self):
        int_number = 15
        str_endian = "big"
        expected_output = "0F"
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_11(self):
        int_number = 16
        str_endian = "big"
        expected_output = "10"
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_12(self):
        """ From the project description. """
        int_number = 954786
        str_endian = "big"
        expected_output = "0E 91 A2"
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_13(self):
        int_number = 3918
        str_endian = "big"
        expected_output = "0F 4E"
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_14(self):
        int_number = 3597
        str_endian = "big"
        expected_output = "0E 0D"
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_15(self):
        """ Negative example from project instructions. """
        int_number = -954786
        expected_output = "-0E 91 A2"
        self.assertEqual(conv_endian(int_number), expected_output)

    def test_conv_endian_16(self):
        int_number = -0
        str_endian = "big"
        expected_output = "00"
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_17(self):
        int_number = -1
        str_endian = "big"
        expected_output = "-01"
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_18(self):
        """ Example from project instructions. """
        int_number = 954786
        str_endian = "little"
        expected_output = "A2 91 0E"
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_19(self):
        """ Example from project instructions. """
        int_number = -954786
        str_endian = "little"
        expected_output = "-A2 91 0E"
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_20(self):
        int_number = -65535
        str_endian = "little"
        expected_output = "-FF FF"
        self.assertEqual(conv_endian(int_number, str_endian), expected_output)

    def test_conv_endian_21(self):
        expected_output = "-A2 91 0E"
        self.assertEqual(conv_endian(num=-954786, endian='little'), expected_output)

    def test_conv_endian_22(self):
        expected_output = "-0E 91 A2"
        self.assertEqual(conv_endian(num=-954786), expected_output)


if __name__ == '__main__':
    unittest.main()
