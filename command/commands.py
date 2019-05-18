from factory import Command

class ClubeMatcher(Command):

    def execute(self):
        return "clube matcher"


class DefaultMatcher(Command):

    def execute(self):
        return "default matcher"