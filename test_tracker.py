import json
from tracker import fee, summarize, main


def test_card_fee():
    assert fee("card", 100) == 2.0


def test_transfer_and_cash_fee():
    assert fee("transfer", 80) == 1.0
    assert fee("cash", 80) == 0


def test_total_includes_fees():
    total, _ = summarize([{"amount": 100, "category": "a", "method": "card"},
                          {"amount": 50, "category": "b", "method": "cash"}])
    assert total == 152.0


def test_category_totals_exclude_fees():
    _, cat = summarize([{"amount": 100, "category": "a", "method": "card"},
                        {"amount": 20, "category": "a", "method": "cash"}])
    assert cat == {"a": 120}


def test_cli_output(tmp_path, capsys):
    p = tmp_path / "e.json"
    p.write_text(json.dumps([{"amount": 10, "category": "x", "method": "cash"}]))
    main(["tracker.py", str(p)])
    assert capsys.readouterr().out.splitlines()[0] == "Total (incl. fees): 10.00"
