class Queue(object):
  def __init__(self):
    self.queue = []

  def __len__(self):
    return len(self.queue)

  def __bool__(self):
    return len(self) > 0

  def __str__(self):
    if not self:
      return "Queue: <empty>"
    return "Queue:\n  " + "\n  ".join(map(str, self.queue))

  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    if self:
      val = self.queue[0]
      if len(self) > 1:
        self.queue = self.queue[1:]
      else:
        self.queue = []
      return val
