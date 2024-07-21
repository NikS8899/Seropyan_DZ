from src.decorators import log


def test_log_1(capsys):
    @log()
    def sqr_func(x):
        return x * x

    print(sqr_func(2))
    captured = capsys.readouterr()
    assert captured.out == f"sqr_func ok\n\n{4}\n"


def test_log_2(capsys):
    @log()
    def sqr_func(x):
        return x / x

    print(sqr_func(0))
    captured = capsys.readouterr()
    assert captured.out == "sqr_func error: division by zero input (0,) \n\nNone\n"
