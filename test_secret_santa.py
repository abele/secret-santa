from secret_santa import main


def test_print_gift_givers_and_receiver_pairs(capsys):
    main()
    out, _ = capsys.readouterr()
    assert out == """y dāvina dāvanu c
c dāvina dāvanu a
a dāvina dāvanu x
x dāvina dāvanu b
b dāvina dāvanu z
z dāvina dāvanu y
"""

