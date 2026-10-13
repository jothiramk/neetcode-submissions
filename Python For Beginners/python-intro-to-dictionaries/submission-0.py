from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    result_dict = {}
    result_dict[name]=age
    return result_dict


def list_to_dict(words: List[str]) -> Dict[str, int]:
    result_dict = {}
    for word in words:
        result_dict[word]= words.index(word)

    return result_dict



# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))
