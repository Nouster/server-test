from fastapi.testclient import TestClient
from backend.main import app, products_db

client = TestClient(app)

def setup_function():
    products_db.clear()

def test_create_product():
    response = client.post(
        "/products",
        json={"nom": "iPhone 15", "description": "Smartphone Apple", "prix": 999.99, "quantite": 10},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["nom"] == "iPhone 15"
    assert "id" in data

def test_get_products():
    client.post(
        "/products",
        json={"nom": "MacBook", "description": "Laptop Apple", "prix": 1299.99, "quantite": 5},
    )
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) >= 1

def test_get_single_product():
    res = client.post(
        "/products",
        json={"nom": "iPad", "description": "Tablette Apple", "prix": 599.99, "quantite": 20},
    )
    product_id = res.json()["id"]
    
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["nom"] == "iPad"

def test_get_nonexistent_product():
    response = client.get("/products/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Produit non trouvé"

def test_update_product():
    res = client.post(
        "/products",
        json={"nom": "Souris", "description": "Souris sans fil", "prix": 25.0, "quantite": 50},
    )
    product_id = res.json()["id"]
    
    response = client.put(
        f"/products/{product_id}",
        json={"nom": "Souris Gaming", "description": "Souris RGB", "prix": 45.0, "quantite": 30},
    )
    assert response.status_code == 200
    assert response.json()["nom"] == "Souris Gaming"
    assert response.json()["prix"] == 45.0

def test_update_nonexistent_product():
    response = client.put(
        "/products/9999",
        json={"nom": "Test", "description": "Test", "prix": 0, "quantite": 0},
    )
    assert response.status_code == 404

def test_delete_product():
    res = client.post(
        "/products",
        json={"nom": "Clavier", "description": "Clavier mécanique", "prix": 80.0, "quantite": 15},
    )
    product_id = res.json()["id"]
    
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Produit supprimé avec succès"
    
    get_res = client.get(f"/products/{product_id}")
    assert get_res.status_code == 404

def test_delete_nonexistent_product():
    response = client.delete("/products/9999")
    assert response.status_code == 404
