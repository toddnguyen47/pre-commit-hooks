"""Convert beginning tabs test"""

import pytest

from pre_commit_hooks import convert_beginning_tabs

def test_given_beginning_tabs_when_converting_then_return_spaces():
    test_str = "		Hello World"
    actual_str = convert_beginning_tabs.convert_tabs_to_spaces(test_str, 4)
    assert "        Hello World" == actual_str


def test_given_no_tabs_at_beginning_when_converting_then_return_same_input():
    test_str = "Hello World"
    actual_str = convert_beginning_tabs.convert_tabs_to_spaces(test_str, 4)
    assert actual_str == test_str


def test_given_tabs_within_tab_when_converting_then_inside_tabs_should_not_be_converted():
    test_str = "		Hello 	there	World"
    actual_str = convert_beginning_tabs.convert_tabs_to_spaces(test_str, 4)
    assert "        Hello 	there	World" == actual_str


def test_given_excess_whitespace_on_right_when_converting_then_remove_excess_whitespace():
    test_str = "		Hello 	there	World		   "
    actual_str = convert_beginning_tabs.convert_tabs_to_spaces(test_str, 4)
    assert "        Hello 	there	World" == actual_str


@pytest.mark.parametrize(
    "input, expected",
    [
        ("        Hello 	there	World		   ", "        Hello 	there	World"),
        (" 		Hello 	there	World		   ", "        Hello 	there	World"),
        ("  		Hello 	there	World		   ", "        Hello 	there	World"),
        ("   		Hello 	there	World		   ", "        Hello 	there	World"),
        ("	 	Hello 	there	World		   ", "        Hello 	there	World"),
        ("	  	Hello 	there	World		   ", "        Hello 	there	World"),
        ("	   	Hello 	there	World		   ", "        Hello 	there	World"),
    ],
)
def test_given_space_tabs_combination_when_converting_with_4_spaces_per_tab_then_convert_correctly(
    input: str, expected: str
):
    actual_str = convert_beginning_tabs.convert_tabs_to_spaces(input, 4)
    assert expected == actual_str


@pytest.mark.parametrize(
    "input, expected",
    [
        ("        Hello 	there	World		   ", "        Hello 	there	World"),
        (" 		Hello 	there	World		   ", "    Hello 	there	World"),
        ("  		Hello 	there	World		   ", "      Hello 	there	World"),
        ("   		Hello 	there	World		   ", "      Hello 	there	World"),
        ("	 	Hello 	there	World		   ", "    Hello 	there	World"),
        ("	  	Hello 	there	World		   ", "      Hello 	there	World"),
        ("	   	Hello 	there	World		   ", "      Hello 	there	World"),
    ],
)
def test_given_space_tabs_combination_when_converting_with_2_spaces_per_tab_then_convert_correctly(
    input: str, expected: str
):
    actual_str = convert_beginning_tabs.convert_tabs_to_spaces(input, 2)
    assert expected == actual_str
