class Person:
    def __init__(self, name: str, weight: float, hobbies: list):
        self.name = name
        if isinstance(weight, str) and weight.replace('.', '', 1).isdigit():
            self.weight = float(weight)
        elif isinstance(weight, (int, float)):
            self.weight = float(weight)
        else:
            self.weight = weight
        self.hobbies = hobbies

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I weigh {self.weight} kg. and my hobbies are {', '.join(self.hobbies)}"

    def __repr__(self) -> str:
        hobbies_str = ', '.join(f"'{hobby}'" for hobby in self.hobbies)
        return f"Person {{\n  name: '{self.name}',\n  weight: {self.weight},\n  hobbies: [ {hobbies_str} ]\n}}"
    