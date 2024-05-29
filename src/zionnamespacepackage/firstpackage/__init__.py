"""Package docstring. Think cautiously on putting the __version__ here. If __version__="0.1.0" is
put here. Print firstpackage.__version__ will get the output "0.1.0"."""

import os
import subprocess

src_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ["PATH"] = src_dir + os.pathsep + os.environ["PATH"]
subprocess.run("helloworld", env=os.environ)
