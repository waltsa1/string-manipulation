import pytest

from main import capitalize_nth_letter


class TestCapitalization:

    @pytest.mark.parametrize("input_str, n, expected_result", [
        ("Aspiration.com", 3, "asPirAtiOn.cOm"),
        ("Aspiration.com", 4, "aspIratIon.cOm"),
        ("aspiration.com", 0, "Aspiration.com"),
        ("zpq3b_84|t", 3, "zpQ3b_84|t"),
        ("kIEG25tq6[=z", 2, "kIeG25tQ6[=Z"),
        ("Vi_3WJ\\h1+DjA$kIE#G25t@q6[=zr", 5, "vi_3wJ\\h1+djA$kie#g25t@q6[=Zr"),
        ("?tlIP]u@Ni*k -QmBK^!hSD}*_rwqp>l|3zZf1", 7, "?tlip]u@nI*k -qmbk^!hSd}*_rwqp>l|3zzf1"),

    ])
    def test_capitalize_nth_letter(self, input_str, n, expected_result):
        assert capitalize_nth_letter(input_str, n) == expected_result

    @pytest.mark.parametrize("n", [
        (-1),
        (-10),
        (-100),

    ])
    def test_n_less_than_0_exception_in_capitalize_nth_letter(self, n):
        with pytest.raises(Exception) as e:
            assert capitalize_nth_letter("Aspiration.com", n)
            assert str(e.value) == "Position to capitalize, {}, is a negative number.".format(n)

    @pytest.mark.parametrize("input_str, n", [
        ("hi", 5),
        ("Guten Tag", 44),
        ("bonsoir", 22),

    ])
    def test_n_greater_than_input_length_exception_in_capitalize_nth_letter(self, input_str, n):
        with pytest.raises(Exception) as e:
            assert capitalize_nth_letter(input_str, n)
            assert str(e.value) == "Position to capitalize, {}, " \
                                   "exceeds the length of the input string, {}.".format(n, len(input_str))



