import unittest

from install_packages import packages

class TestParsing(unittest.TestCase):
    def test_parse(self):
        """
        Test parsing
        """
        yaml_data = """
            single_item: single_item
            multi_simple_item:
              - multi_item_1
              - multi_item_2
            multi_complex_item:
              ui: true
              items:
                - mdadm
        """

        packages.parse_packages_definitions(yaml_data)
        #self.assertEqual(, 6)

if __name__ == '__main__':
    unittest.main()