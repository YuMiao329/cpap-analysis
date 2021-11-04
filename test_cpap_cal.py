import pytest


@pytest.mark.parametrize("input, expected", [
    ('27.9,13.3,15.5,7.5,6.1,15.8', 14.35),
    ('11.0,23.6,15.2,2.3,4.0,19.7,3.7', 11.357142857142858),
])
def test_cal_avg_seal(input, expected):
    from cpap_cal import cal_avg_seal
    answer = cal_avg_seal(input)
    assert answer == expected


@pytest.mark.parametrize("input, expected", [
    ('5,0,2,3,9,1,2', 3.142857142857143),
    ('5,6,7,1,6,0', 4.166666666666667),
])
def test_cal_avg_events(input, expected):
    from cpap_cal import cal_avg_events
    answer = cal_avg_events(input)
    assert answer == expected


@pytest.mark.parametrize('input1, input2, expected', [
    ('99,91,98,92,98,95', 4.166666666666667, 'Hypoxia'),
    ('94,94,94,96,96,93,98,92', 4.875, 'Hypoxia'),
    ('91,99,100,96,98', 7.6, 'Hypoxia Apnea'),
    ('97,93,100,94,95,95,99,94', 6.0, 'Apnea'),
    ('98,100,93,98,95,98,98', 5.0, "Normal Sleep")
])
def test_diagnosis(input1, input2, expected):
    from cpap_cal import diagnosis
    answer = diagnosis(input1, input2)
    assert answer == expected
