
class MyException(Exception):
    def __init__(this, message="Error: {}\n".format("An unknown error occurred"), cause="{}".format("Unknown cause")):
        this.message = message
        this.cause = cause
        this.error = "\n\t{}\n\t{}\n\n".format(this.message, this.cause)
        super().__init__(this.error)

    def __str__(this):
        return f'{this.message} -> {this.cause}'


class FileNotExistException(MyException):
    def __init__(this, message, cause):
        super().__init__(message=message, cause=cause)


class FileNotReadableException(MyException):
    def __init__(this, message, cause):
        super().__init__(message=message, cause=cause)


class NotAFileException(MyException):
    def __init__(this, message, cause):
        super().__init__(message=message, cause=cause)
