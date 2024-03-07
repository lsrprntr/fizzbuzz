import fizzbuzz
import pytest

#Test cases (Input of [x, y], Expected output)
cases = [

    #Normal cases and reverse cases
    ([1, 5], "1\n2\n3\nfizz\n4\n5\nbuzz\n"),
    ([90, 100], "90\nfizz\nbuzz\n91\n92\n93\nfizz\n94\n95\nbuzz\n96\nfizz\n97\n98\n99\nfizz\n100\nbuzz\n"),
    ([5, 1], "5\nbuzz\n4\n3\nfizz\n2\n1\n"),
    ([15, 10], "15\nfizz\nbuzz\n14\n13\n12\nfizz\n11\n10\nbuzz\n"),
    ([1, 1], "1\n"),
    ([100, 100], "100\nbuzz\n"),


    #Out of bounds
    ([0, 3], "Error: Enter valid integers from 1-100\n"),
    ([1, 101], "Error: Enter valid integers from 1-100\n"),
    ([-1, 5], "Error: Enter valid integers from 1-100\n"),
    ([1, -5], "Error: Enter valid integers from 1-100\n"),

    #String Integer
    ([1, "2"], "1\n2\n"),
    (["99", 97], "99\nfizz\n98\n97\n"),

    #Wrong Types
    (["a", 2], "Error: Enter valid integers from 1-100\n"),
    ([1, "b"], "Error: Enter valid integers from 1-100\n"),
    (["d", "b"], "Error: Enter valid integers from 1-100\n"),
    ([None, None], "Error: Enter valid integers from 1-100\n"),
    ([True, 2], "1\n2\n"), #Bool sideeffect
    ([False, 2], "Error: Enter valid integers from 1-100\n"),

]

@pytest.mark.parametrize("inp, expected", cases)
def testfizzbuzz(monkeypatch,capsys, inp, expected):
    # Monkeypatch input function to read from iterable
    responses = iter(inp)
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    # Check function
    assert fizzbuzz.fizzbuzz() == None
    
    # Check print outputs
    captured = capsys.readouterr()
    assert captured.out == expected
    return


if __name__ == '__main__':
    testfizzbuzz()