matchers = {
    "clube": "ClubeMatcher",
    "default": "DefaultMatcher"
}

def __getattr__(name):
    try:
        return getattr(
            __import__("commands"), matchers[name]
        )()
    except Exception as error:
        print("matcher:{name} not found retrieving default".format(
            name=name
        ))
        return getattr(
            __import__("commands"),
            matchers["default"]
        )()