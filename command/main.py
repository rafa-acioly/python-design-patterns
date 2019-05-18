from factory import Command
import matchers

def get_matcher(matcher_type: str) -> Command:
    matcher = getattr(matchers, matcher_type)
    return matcher.execute()

if __name__ == "__main__":
    print(get_matcher("xpto"))