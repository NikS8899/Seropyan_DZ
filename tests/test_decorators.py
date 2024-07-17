from src.decorators import log
import pytest

def test_log_1(capsys):
    @log()
    def sqr_func(x):
        return x*x

    print(sqr_func(2))
    captured = capsys.readouterr()
    assert captured.out == f"OK\n\n{4}\n"

