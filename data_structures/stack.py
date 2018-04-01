class Stack(object):
    def __init__(self, max_size):
        """Initializes a Stack with a specified maximum size.

        Args:
            max_size (int): The maximum size of the stack.
        """
        assert type(max_size) is int and max_size >= 0, '`max_size` must be 0 or large but was {}'.format(max_size)
        self._max_size = max_size
        self._top = -1
        self._stack = [None] * self._max_size

    def is_full(self):
        """Checks if the stack is full.

        Returns:
            bool: Whether or not the stack is full.
        """
        return self._top == self._max_size - 1

    def is_empty(self):
        """Checks if the stack is empty.

        Returns:
            bool: Whether or not the stack is empty.
        """
        return self._top == -1

    def peek(self):
        """Returns the top element of the stack without removing it.

        Returns:
            [type]: The top element
        """
        return self._stack[self._top]

    def push(self, data):
        """Pushes an element to the top of the stack.

        Args:
            data (type): The data to push.

        Raises:
            IndexError: If the stack is full.
        """
        if not self.is_full():
            self._top += 1
            self._stack[self._top] = data
        else:
            msg = 'Stack overflow at index {} with max size of {}'.format(self._top + 1, self._max_size)
            raise IndexError(msg)

    def pop(self):
        """Returns the top element of the stack, removing it from the stack.

        Raises:
            IndexError: If the stack is empty.

        Returns:
            [type]: The top element of the stack.
        """
        if not self.is_empty():
            data = self._stack[self._top]
            self._top -= 1
            return data
        else:
            msg = 'Stack is empty'
            raise IndexError(msg)
