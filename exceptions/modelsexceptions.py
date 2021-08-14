class MissingArgs(Exception):
    """will be raised when there aare not enough args to query the 
    database.

    Args:
        Exception (tuple): [tuple of required args]
    """


    def __init__(self, required_args:tuple) -> None:
        """initializ the required args to be added into the message """
        
        self.required_args = required_args
        super().__init__(self.required_args)

    def __str__(self):
        return f'MISSING REQUIRED_ARGS. Required args: {self.required_args}'