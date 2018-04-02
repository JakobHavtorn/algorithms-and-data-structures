class Queue(object):
    def __init__(self, max_size):
        """Initializes a Queue with a specified maximum size.
        
        Parameters:
        ----------
        max_size : {int}
            The maximum size of the Queue
        """
        assert type(max_size) is int and max_size >= 0, '`max_size` must be 0 or large but was {}'.format(max_size)
        self._max_size = max_size
        self._front = 0         # Front pointer (front most element index)
        self._rear = -1         # Rear pointer (last element index)
        self._item_count = 0    # Elements in queue
        self._queue = [None] * self._max_size

    def enqueue(self, data):
        """Enqueues data in the Queue.
        
        Parameters:
        ----------
        data : {any type}
            The data to enqueue.
        Raises
        ------
        IndexError
            If the Queue is full.
        """
        if not self.is_full():
            self._increment_pointer('_rear')
            self._queue[self._rear] = data
            self._item_count += 1
        else:
            msg = 'Queue is full at {} elements'.format(self._max_size)
            raise IndexError(msg)

    def dequeue(self):
        """Dequeues the front item of the Queue.
        
        Raises
        ------
        IndexError
            If the Queue is empty.
        
        Returns
        -------
        <any type>
            The data dequeued.
        """
        if not self.is_empty():
            data = self._queue[self._front]
            self._increment_pointer('_front')
            self._item_count -= 1
            return data
        else:
            msg = 'Queue is empty'
            raise IndexError(msg)

    def is_full(self):
        """Checks if the queue is full.
        
        Returns
        -------
        bool
            Whether or not the queue is full.
        """
        return self._item_count == self._max_size

    def is_empty(self):
        """Checks if the queue is empty.
        
        Returns
        -------
        bool
            Whether or not the Queue is empty
        """
        return self._item_count == 0

    def peek(self):
        """Returns the front elelemt of the queue without removing it.
        
        Returns
        -------
        <any type>
            The front element.
        """
        return self._queue[self._front]

    def _increment_pointer(self, pointer):
        """Helper method to increment front and rear pointers.
        
        Parameters:
        ----------
        pointer : {str}
            String of the pointer attribute (_front or _rear)
        """
        if getattr(self, pointer) == self._max_size - 1:
            setattr(self, pointer, 0)
        else:
            setattr(self, pointer, getattr(self, pointer) + 1)
            