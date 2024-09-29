""" Who Likes It?

You probably know the "like" system from Facebook and other pages. People can "like" blog posts,
pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item.

It must return the display text as shown in the examples:
    []                                -->  "no one likes this"
    ["Peter"]                         -->  "Peter likes this"
    ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
    ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
    ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
"""


def likes(names: list[str]) -> str:
    """Initial, simple solution"""
    single_suffix = "likes this"
    plural_suffix = "like this"
    len_names = len(names)

    if len_names < 1:
        return f"no one {single_suffix}"
    if len_names == 1:
        return f"{names[0]} {single_suffix}"
    if len_names == 2:
        return f"{names[0]} and {names[1]} {plural_suffix}"
    if len_names == 3:
        return f"{names[0]}, {names[1]} and {names[2]} {plural_suffix}"

    remainder = len_names - 2
    return f"{names[0]}, {names[1]} and {remainder} others {plural_suffix}"


def likes2(names):
    """Clever solution.

    Returns the element in the dict based on the min() call, and then formats
    the returned string.
    """
    n = len(names)
    return {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {}, and {} like this",
        4: "{}, {}, and {others} others like this",
    }[min(4, n)].format(*names[:3], others=n - 2)


print(likes([]))
print(likes(["Tom"]))
print(likes(["Tom", "Bob"]))
print(likes(["Tom", "Bob", "Mary"]))
print(likes(["Tom", "Bob", "Mary", "foo"]))
print(likes(["Tom", "Bob", "Mary", "foo", "bar"]))

print("-----")

print(likes2([]))
print(likes2(["Tom"]))
print(likes2(["Tom", "Bob"]))
print(likes2(["Tom", "Bob", "Mary"]))
print(likes2(["Tom", "Bob", "Mary", "foo"]))
print(likes2(["Tom", "Bob", "Mary", "foo", "bar"]))
