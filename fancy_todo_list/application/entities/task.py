from dataclasses import dataclass

@dataclass(frozen=True)
class Title():    
    __create_key = object()

    value: str
    create_key: object

    def __post_init__(self):
        class_name = self.__class__.__name__
        assert self.create_key == Username.__create_key, (
            f"{class_name} instance must be created by " +\
             f"using the '{class_name}.create' method.")

    @classmethod
    def create(cls, value: str)-> "Title":
        if not isinstance(value, str):
            raise ValueError("'value' must be a string value")

        value = value.strip()

        if not (1 < len(value) <= 50):
            raise ValueError("'value must be a string with at least 1 and a maximum of 50 characters")

        return Title(value=value, create_key=cls.__create_key)

@dataclass(frozen=True)
class Task():
    author: Username
    title: Title
    
    def __post_init__(self):
        assert isinstance(author, Username), "'author' must be an instance of Username."
        assert isinstance(title, Title), "'title' must be an instance of Title."
