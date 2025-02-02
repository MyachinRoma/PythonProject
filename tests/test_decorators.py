from src.decorators import log


@log(filename="test_log.txt")
def my_function(x, y):
    return x + y


@log(filename="test_log.txt")
def error_function(x, y):
    raise ValueError("An error occurred")


def test_my_function(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out


def test_error_function(capsys):
    try:
        error_function(1, 2)
    except ValueError:
        pass
    captured = capsys.readouterr()
    assert "error_function error: ValueError. Inputs: (1, 2), {}" in captured.out
