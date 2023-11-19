from mini_wc_config import MiniWordCountConfig
import pytest

def test_can_instantiate():
  config = MiniWordCountConfig(False,False,False,False)
  assert config.bytes()
  assert config.lines()
  assert config.chars()
  assert config.files == []

def test_factory_raises_named_after_positional():
  args = ["abc.test", "-c"]
  with pytest.raises(Exception) as _:
    MiniWordCountConfig.build(args)

def test_factory_raises_unknown_named_arg():
  args = ["-x"]
  with pytest.raises(Exception) as _:
    MiniWordCountConfig.build(args)

def test_factory_works_with_valid_args():
  args = ["-cl", "abc.def", "ghi.jkl"]
  config = MiniWordCountConfig.build(args)
  assert config.files == ["abc.def", "ghi.jkl"]
  assert config.bytes()
  assert config.lines()
  assert not config.words()
  assert not config.chars()