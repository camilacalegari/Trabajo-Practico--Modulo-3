import requests

# Caso 1
class TestBerry1:
    def test_berry_1(self):
        response = requests.get("https://pokeapi.co/api/v2/berry/1")
        assert response.status_code == 200
        data = response.json()

        assert data["size"] == 20
        assert data["soil_dryness"] == 15
        assert data["firmness"]["name"] == "soft"

# Caso 2
class TestBerry2:
    def test_berry_2(self):
        response1 = requests.get("https://pokeapi.co/api/v2/berry/1")
        response2 = requests.get("https://pokeapi.co/api/v2/berry/2")

        assert response1.status_code == 200
        assert response2.status_code == 200

        berry1 = response1.json()
        berry2 = response2.json()

        assert berry2["firmness"]["name"] == "super-hard"
        assert berry2["size"] > berry1["size"]
        assert berry2["soil_dryness"] == berry1["soil_dryness"]

# Caso 3
class TestPikachu:
    def test_pikachu(self):
        response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu/")
        assert response.status_code == 200
        data = response.json()

        assert 10 < data["base_experience"] < 1000
        assert "electric" in [t["type"]["name"] for t in data["types"]]
