import pytest
from gendiff import generate_diff

json1 = "tests/fixtures/file1.json"
json2 = "tests/fixtures/file2.json"
json3 = "tests/fixtures/file3.json"

diff_json_1_2 = "tests/fixtures/diff_json_1_2.txt"
diff_json_1_3 = "tests/fixtures/diff_json_1_3.txt"


testdata = [(json1, json2, diff_json_1_2), (json1, json3, diff_json_1_3)]


@pytest.mark.parametrize("json1, json2, diff_json_1_2", testdata)
def test_generate_diff(json1, json2, diff_json_1_2):
    """Check that the function correctly shows the difference
    between two files"""
    with open(diff_json_1_2, "r") as file:
        string = file.read()
        string = string.rstrip("\n")

    diff = generate_diff(json1, json2)
    assert diff == string
