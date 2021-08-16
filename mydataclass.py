from dataclasses import dataclass, field
import enum


class VerbTense(enum.Enum):
    SIMPLE_PRESENT = 'simple present'
    PRESENT_PERFECT = 'present perfect'
    SIMPLE_PAST = 'simple past'
    PAST_PROGRESSIVE = 'past progressive'
    PAST_PERFECT = 'past perfect'
    PAST_ANTERIOR = 'past anterior'
    FUTURE = 'future'
    FUTURE_PERFECT = 'future perfect'
    CONDITIONAL = 'conditional'
    CONDITIONAL_PERFECT = 'conditional perfect'


# @dataclass(order=True)
# class Person:
#     sort_index: int = field(init=False, repr=False)
#     name: str
#     job: str
#     age: int

#     def __post_init__(self):
#         self.sort_index = self.age


#     def __str__(self) -> str:
#         return f'{self.name}  {self.job}  ({self.age})'

# person1 = Person("Foo", "Developer", 43)
# person2 = Person("Bar", "SysAdmin", 44)
# person3 = Person("Bla", "DevOps", 43)

# print(id(person1))
# print(id(person2))
# print(id(person3))

# print(person1)

# print(person2 > person3)

print(VerbTense.FUTURE.value)