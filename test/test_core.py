from tqmath.core import dict_to_dataframe


def test_dict_to_dataframe():
    d = {
        "name": "Farooq Mahmud",
        "age": 44
    }

    df = dict_to_dataframe(d)

    row = df.loc[0]
    assert row["name"] == d["name"]
    assert row["age"] == d["age"]