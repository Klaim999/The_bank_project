import pytest

from src.decorators import log


def test_log_console(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(7, 7)

    assert result == 14

    captured = capsys.readouterr()
    output = captured.out

    assert "Start: add" in output
    assert "add ok" in output


def test_log_file(tmp_path):
    log_file = tmp_path / "test.log"

    @log(log_file)
    def multiply(a, b):
        return a * b

    result = multiply(5, 5)

    assert result == 25

    with open(log_file) as f:
        info_file = f.read()

    assert "Start: multiply" in info_file
    assert "multiply ok" in info_file


def test_error_log(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    output = captured.out

    assert "error:" in output
    assert "ZeroDivisionError" in output
    assert "Inputs: (10, 0)" in output
