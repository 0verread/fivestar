import uuid

class UniqueIds():
  def __init__(self, prefix: str) -> None:
    self._prefix = prefix

  def __get_random_id(self) -> str:
    return str(uuid.uuid4()).replace('-','')

  def get_id(self) -> str:
    return self._prefix + self.__get_random_id()