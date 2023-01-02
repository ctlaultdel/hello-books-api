# pass in client fixture 
def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body=response.get_json()

    # Assert
    assert response.status_code == 200
    # is there a way to call ocean book from two_saved_books fixture & reformat in json rather than hardcode??
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }