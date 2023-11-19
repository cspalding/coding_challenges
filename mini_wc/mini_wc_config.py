class MiniWordCountConfig:
  def __init__(self, bytes,lines,words,chars,files=[]) -> None:
    self._bytes = bytes
    self._lines = lines
    self._words = words
    self._chars = chars
    self.files = files

  def bytes(self):
    return self._bytes or self._noOptionsSet()

  def lines(self):
    return self._lines or self._noOptionsSet()

  def words(self):
    return self._words or self._noOptionsSet()

  def chars(self):
    return self._chars or self._noOptionsSet()

  def _noOptionsSet(self):
    return not self._bytes and not self._lines and not self._words and not self._chars

  @staticmethod
  def build(args: list[str]) -> 'MiniWordCountConfig':
    files = []
    bytes = False
    lines = False
    words = False
    chars = False
    for arg in args:
      if "." in arg:
        files.append(arg)
      elif len(files):
        raise Exception("optional named arg `%s` found after positional filename arg" %(arg))
      else:
        for letter in arg:
          if letter == "-":
            continue
          elif letter == "c":
            bytes = True
          elif letter == "l":
            lines = True
          elif letter == "w":
            words = True
          elif letter == "m":
            chars = True
          else:
            raise Exception("unknown named arg %s" %(letter))
    return MiniWordCountConfig(bytes,lines,words,chars,files)