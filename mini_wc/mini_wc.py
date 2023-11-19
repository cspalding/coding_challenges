from sys import stdin
from mini_wc_config import MiniWordCountConfig

class MiniWordCountResult:
  def __init__(self, config: MiniWordCountConfig, numBytes: int, numLines: int, numWords: int, numChars: int) -> None:
    self.config = config
    self.numBytes = numBytes
    self.numLines = numLines
    self.numWords = numWords
    self.numChars = numChars

  def __str__(self):
    res = ""
    if self.config.lines():
      res += "    " + str(self.numLines)
    if self.config.words():
      res += "   " + str(self.numWords)
    if self.config.bytes():
      res += "    " + str(self.numBytes)
    if self.config.chars():
      res += "   " + str(self.numChars)
    if len(self.config.files) > 0:
      res += " " + self.config.files[0]
    return res

class MiniWordCount:
  def __init__(self, config: MiniWordCountConfig) -> None:
    self.config = config

  def run(self) -> MiniWordCountResult:
    bytes = 0
    lines = 0
    words = 0
    chars = 0
    if len(self.config.files) > 0:
      file = open(self.config.files[0], mode='r')
    else:
      if not stdin.isatty():
        file = stdin
      else:
        return MiniWordCountResult(self.config, 0,0,0,0)

    for line in file:
      if self.config.bytes():
        bytes += len(line.encode('utf-8'))
      if self.config.lines():
        lines += 1
      if self.config.words() or self.config.chars():
        split = line.split()
        words += len(split)
        chars += sum((len(word) for word in split))

    file.close()
    return MiniWordCountResult(self.config, bytes, lines, words, chars)
