class StackEmpty(Exception):
  def __init__(self, msg = ""):
    super().__init__(msg)


class Stack(object):
  def __init__(self):
    self.data = []

  def push(self, item):
    self.data.append(item)

  def pop(self):
    if len(self.data) > 0:
      return self.data.pop()
    return None

  def peek(self):
    if len(self.data) > 0:
      return self.data[-1]
    return None

  def is_empty(self):
    return len(self.data) == 0

  def sink(self):
    self.data = []

  def __len__(self):
    return len(self.data)

  def __str__(self):
    if len(self) == 0:
      return "<empty>"

    s = ""
    for i, item in enumerate(self.data[::-1]):
      s += f"{i:3d} | {item}\n"
    return s

  def __repr__(self):
    return f"<Stack object at 0x{id(self):x} (len: {len(self)})>"
