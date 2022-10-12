class CustomError(Exception):
    """
    Custom Error
    :status_code: INT An existing status code (for ex : 404)
    :content: JSON Some content to be sent to the user
    """
    def __init__(self, status_code: int, content: dict):
        self.status_code = status_code
        self.content = content
