def add(string):
    current_node = root
    for char in string:
        current_node = current_node.setdefault(char, {})

    current_node["is_last_char"] = True


def look_up(string):
    current_node = root

    for char in string:
        if not char in current_node:
            return False
        current_node = current_node[char]

    return "is_last_char" in current_node


def find_words_with_prefix(string):
    current_node = root
    for char in string:
        if not char in current_node:
            return False
        current_node = current_node[char]

    return [(string + item) for item in traverse(current_node)]


def traverse(root):
    my_list = []
    for char, value in root.items():
        if char == "is_last_char":
            my_list.append("")
        else:
            my_list.extend([(char + item) for item in traverse(value)])

    return my_list


def delete_with_prefix(root, key):
    for index, char in enumerate(key):
        if char in root:
            if len(key) == 1:
                root.pop(char)
                return True
            return delete_with_prefix(root[char], key[(index + 1) :])
        else:
            return False


root = {}

add("mat")
add("match")
add("bat")
add("been")
add("bearing")
add("bear")

print(look_up("match"))
print(look_up("mat"))
print(look_up("bat"))
print(look_up("been"))
print(look_up("bear"))
print(look_up("bearing"))
print(look_up("be"))
print(look_up("bearings"))

print(find_words_with_prefix("ma"))
print(find_words_with_prefix("bear"))
print(traverse(root))
print(delete_with_prefix(root, "bear"))
print(traverse(root))
