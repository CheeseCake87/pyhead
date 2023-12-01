class PageTitleNotSet(Exception):
    def __init__(self, message):
        super().__init__(message)


class KeywordsNotSet(Exception):
    def __init__(self, message):
        super().__init__(message)
