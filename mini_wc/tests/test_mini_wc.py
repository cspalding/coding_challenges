import subprocess
from tabnanny import check
from mini_wc import MiniWordCount
from mini_wc_config import MiniWordCountConfig

def test_integration_file():
  cmd = ["python", "main.py", "/Users/spalding/src/challenges/mini_wc/tests/input.txt"]
  result = subprocess.run(cmd, stdout=subprocess.PIPE)
  assert result.stdout == b'    3   7    28   22 /Users/spalding/src/challenges/mini_wc/tests/input.txt\n'

def test_integration_stdin():
  # in an ideal world we wouldn't use shell=True in subprocess.check_output. But this makes the test work for now
  # and it is a worthwhile test to have IMO. In theory there's a way to get rid of that arg (my impression is that the
  # issue is that it introduces a security vulnerability which may not matter in a test environment), but I couldn't
  # figure out how.
  result = subprocess.check_output(
    "cat /Users/spalding/src/challenges/mini_wc/tests/input.txt | python main.py",
    shell=True
  )
  assert result == b'    3   7    28   22\n'

def test_it_works():
  args = ["/Users/spalding/src/challenges/mini_wc/tests/input.txt"]
  config = MiniWordCountConfig.build(args)
  result = MiniWordCount(config).run()
  assert result.numBytes == 28
  assert result.numWords == 7
  assert result.numChars == 22
  assert result.numLines == 3
