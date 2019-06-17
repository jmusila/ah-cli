from click.testing import CliRunner
from articles import get, get_list, main


def test_get_single_article():
    runner = CliRunner()
    result = runner.invoke(get, ['new_wangonya'])
    assert result.exit_code == 0
    assert "Status code: 200" in result.output


def test_get_all_articles():
    runner = CliRunner()
    result = runner.invoke(get_list)
    assert result.exit_code == 0
    assert "Status code: 200" in result.output


def test_main():
    runner = CliRunner()
    res = runner.invoke(main)
    assert res.exit_code == 0
    assert "Simple CLI for consuming Authors Haven App 😍" in res.output
