"""Convert beginning spaces to tabs test"""

from pre_commit_hooks import convert_beginning_spaces


def test_given_only_tabs_when_converting_then_no_conversion_is_needed():
    """test function"""
    test_str = "		Hello World"
    actual_str = convert_beginning_spaces.convert_spaces_to_tabs(test_str, 4)
    assert actual_str == "		Hello World"


def test_given_extra_whitespace_when_converting_then_no_conversion():
    """test function"""
    test_str = "		   Hello World"
    actual_str = convert_beginning_spaces.convert_spaces_to_tabs(test_str, 4)
    assert actual_str == "		Hello World"


def test_given_spaces_when_converting_then_convert_correctly():
    """test function"""
    test_str = "		    Hello World"
    actual_str = convert_beginning_spaces.convert_spaces_to_tabs(test_str, 4)
    assert actual_str == "			Hello World"


def test_given_nonconsecutive_spaces_when_converting_then_convert_correctly():
    """test function"""
    test_str = "		   	Hello World"
    actual_str = convert_beginning_spaces.convert_spaces_to_tabs(test_str, 4)
    assert actual_str == "			Hello World"


def test_given_only_spaces_when_converting_then_convert_correctly():
    """test function"""
    test_str = "        Hello World"
    actual_str = convert_beginning_spaces.convert_spaces_to_tabs(test_str, 4)
    assert actual_str == "		Hello World"


def test_given_only_spaces_with_extra_spaces_when_converting_then_convert_correctly():
    """test function"""
    test_str = "         Hello World"
    actual_str = convert_beginning_spaces.convert_spaces_to_tabs(test_str, 4)
    assert actual_str == "		Hello World"


def test_given_only_spaces_with_tabs_found_after_non_whitespace_char_when_converting_then_convert_correctly():
    """test function"""
    test_str = "        Hello 	World"
    actual_str = convert_beginning_spaces.convert_spaces_to_tabs(test_str, 4)
    assert actual_str == "		Hello 	World"

def test_given_7_spaces_when_converting_then_merge_them_into_1_tab():
    """test function"""
    test_str = "       Hello 	World"
    actual_str = convert_beginning_spaces.convert_spaces_to_tabs(test_str, 4)
    assert actual_str == "	Hello 	World"
