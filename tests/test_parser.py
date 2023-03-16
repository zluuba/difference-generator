from gendiff.parser import parse_args as app_parser
import argparse
import mock


FORMAT = 'plain'
FILE1, FILE2 = 'file1.yml', 'file2.yml'


@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(
                first_file=FILE1, second_file=FILE2, format=FORMAT
            ))
def test_parse_args(mock_args):
    parsed = app_parser()
    assert parsed == (FILE1, FILE2, FORMAT)
g