from src.reports.payout import PayoutReport


def test_payout_report(employees):
    report = PayoutReport()
    payout = report.generate(employees)
    assert payout["alice@example.com"] == 160 * 50
    assert payout["bob@example.com"] == 150 * 60
    assert payout["carol@example.com"] == 170 * 55
