class BufferFullException(Exception):
    """Exception raised for a full buffer"""

    def __init__(self, message="Error: Buffer is full"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class BufferEmptyException(Exception):
    """Exception raised for an empty buffer"""

    def __init__(self, message="Error: Buffer is empty"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [[] for _ in range(capacity)]
        self.write_pointer = 0

    def read(self):
        if self._buffer_empty():
            raise BufferEmptyException()

        self.rotate_buffer()
        self.write_pointer -= 1
        return self.buffer[-1].pop()

    def write(self, data):
        if self._buffer_full():
            raise BufferFullException()
        else:
            self.buffer[self.write_pointer].append(data)
            self.write_pointer += 1

    def overwrite(self, data):
        if self._buffer_not_full():
            self.write(data)
        else:
            self.buffer[0][0] = data
            self.rotate_buffer()

    def clear(self):
        [data.clear() for data in self.buffer]
        self.write_pointer = 0

    def rotate_buffer(self):
        self.buffer = self.buffer[1:] + self.buffer[:1]

    def _buffer_empty(self):
        return not any(self.buffer)

    def _buffer_full(self):
        return all(self.buffer)

    def _buffer_not_full(self):
        return not all(self.buffer)
