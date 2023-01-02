from pytest import ocean_book
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
    assert response_body == {
        "id": ocean_book.id,
        "title": ocean_book.title,
        "description": ocean_book.description,
    }

def test_create_one_book(client):
    # Act
    response = client.post("/books", json={
        "title": "New Book",
        "description": "The Best!"
    })
    response_body = response.get_json()
    #response_body = response.get_data(as_text=True) # alternative soln

    #Assert
    assert response.status_code == 201
    assert response_body == "New Book Successfully Created"
