import json
# from pprint import pprint
from typing import TypedDict  # -> Tipa dicts


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


json_string = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}
'''

filme: Movie = json.loads(json_string)
# pprint(filme, width=40)
# print(filme['title'])
# print(filme['characters'][1])
# print(filme['year'])
print(json.dumps(filme, ensure_ascii=False, indent=2))
print(json_string)
