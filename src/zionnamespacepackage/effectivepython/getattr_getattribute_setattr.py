"""Demonstrate how item 47 works."""


class LazyRecord:
    """
    data = LazyRecord()
    print("before: ", data.__dict__)
    print("foo: ", data.foo)
    print("after: ", data.__dict__)
    print("foo: ", data.foo)

    >>> before:  {'exists': 5}
    >>> Call __getattr__
    >>> foo:  value for foo
    >>> after:  {'exists': 5, 'foo': 'value for foo'}
    >>> foo:  value for foo

    """

    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        """__getattr__ is called each time if hasattr or getattr is called and
        element doesn't exist."""
        print("Call __getattr__")
        value = f"value for {name}"
        setattr(self, name, value)
        return value


class ValidatingRecord:
    """
    data = ValidatingRecord()
    print("exists: ", data.exists)
    print("first foo: ", data.foo)
    print("second foo: ", data.foo)

    >>> * Called __getattribute__'exists'
    >>> * Found {name!r}, returning {value!r}
    >>> exists:  5
    >>> * Called __getattribute__'foo'
    >>> * setting 'foo' to 'value for foo'
    >>> first foo:  value for foo
    >>> * Called __getattribute__'foo'
    >>> * Found {name!r}, returning {value!r}
    >>> second foo:  value for foo

    """

    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name: str):
        """__getattribute__ is called each time if hasattr or getattr is called."""
        print(f"* Called __getattribute__{name!r}")
        try:
            value = super().__getattribute__(name)
            print("* Found {name!r}, returning {value!r}")
            return value
        except AttributeError:
            value = f"value for {name}"
            print(f"* setting {name!r} to {value!r}")
            setattr(self, name, value)
            return value


class SavingRecord:
    """
    data = SavingRecord()
    print("before: ", data.__dict__)
    data.foo = 5
    print("after: ", data.__dict__)
    data.foo = 7
    print("finally: ", data.__dict__)

    >>> before:  {}
    >>> * Called __setattr__('foo', 5)
    >>> after:  {'foo': 5}
    >>> * Called __setattr__('foo', 7)
    >>> finally:  {'foo': 7}

    """

    def __setattr__(self, name: str, value) -> None:
        """__setattr__ method is always called every time an attribute is
        assigned on an instance (either directly or through the setattr built-in
        function."""
        print(f"* Called __setattr__({name!r}, {value!r})")
        super().__setattr__(name, value)


class BrokenDictionaryRecord:
    """BAD implementation. It will lead to infinite recursion. Explain why. The
    solution is DictionaryRecord"""

    def __init__(self, data) -> None:
        self._data = data

    def __getattribute__(self, name: str):
        print(f"* Called __getattribute__({name!r})")
        return self._data[name]


class DictionaryRecord:
    """It fetches value from the instance attritube `dictionary`. Thus, no
    recursion.

    data = DictionaryRecord({"foo": 3})
    print("foo:, ", data.foo)

    >>> * Called __getattribute__('foo')
    >>> foo:,  3

    """

    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name: str):
        print(f"* Called __getattribute__({name!r})")
        # data_dict is a dictionary. Not a DictionaryRecord object.
        data_dict = super().__getattribute__("_data")
        return data_dict[name]


if __name__ == "__main__":
    pass
