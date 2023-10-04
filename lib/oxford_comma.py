def oxford_comma(items):
    x = "".join(items)
    return x

def oxford_comma(items):
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    elif len(items) > 2:
        last_item = items[-1]
        items_except_last = items[:-1]
        return f"{', '.join(items_except_last)}, and {last_item}"
    else:
        return ", ".join(items)