from app.main import process_data

def test_filtered_output():
    result = process_data()
    assert len(result) == 2
    assert any(row['name'] == 'Alice' for row in result)
    assert all(row['age'] > 30 for row in result)
