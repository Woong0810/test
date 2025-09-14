import sys, os, importlib.util, pathlib
print("script dir =", pathlib.Path(__file__).parent)
print("cwd       =", os.getcwd())
print("in sys.path?", str(pathlib.Path(__file__).parent) in [str(pathlib.Path(p)) for p in sys.path if p])

spec = importlib.util.find_spec("data_unsorted_a_lot")
print("find_spec =", spec and spec.origin)
