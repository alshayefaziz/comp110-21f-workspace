c: int = 0
    for error in sent:
        for error_test in sent:
            if sent[error] == sent[error_test]:
                c += 1
        if c > 1:
            raise KeyError("Multiple keys are not allowed in dictionaries!")
        else:
            c = 0



inverted_color: dict[str, str] = {}
    for new in color:
        former: str = color[new]
        latter: str = new
        inverted_color[former] = latter
    counter: int = 0
    counter_2: int = 0
    popular: str = ""
    for colour in inverted_color:
        repeat: str = colour
        if repeat in inverted_color:
            counter_2 += 1
        if counter_2 > counter:
            popular = colour
            counter = counter_2
            counter_2 = 0
    return popular







inverted_color: dict[str, str] = {}
    for new in color:
        former: str = color[new]
        latter: str = new
        inverted_color[former] = latter
    counter: int = 0
    counter_2: int = 0
    popular: str = ""
    for colour in inverted_color:
        for repeat in inverted_color:
            if colour == repeat:
                counter += 1
        if counter > counter_2:
            popular = colour
            counter_2 = counter
            counter = 0
    return popular