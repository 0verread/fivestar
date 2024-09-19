import uuid

class UniqueIds():
  def __init__(self, prefix: str) -> None:
    self._prefix = prefix

  def __get_random_id(self) -> str:
    return str(uuid.uuid4())

  def get_id(self) -> str:
    random_id = self.__get_random_id()
    return self._prefix + random_id