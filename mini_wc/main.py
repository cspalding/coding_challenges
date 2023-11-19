#! /usr/bin/env/python
from sys import argv
from mini_wc import MiniWordCount
from mini_wc_config import MiniWordCountConfig

if __name__=="__main__":
  config = MiniWordCountConfig.build(argv[1:])
  result = MiniWordCount(config).run()
  print(result)