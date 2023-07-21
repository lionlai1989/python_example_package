from setuptools import setup
from setuptools.command import develop, build_py, install
import subprocess

class CustomDevelop(develop.develop):
    def run(self):
        super(CustomDevelop, self).run()
        print("Execute CustomDevelop ......")

class CustomBuildPy(build_py.build_py):
    def run(self):
        super(CustomBuildPy, self).run()
        print("Execute CustomBuildPy ......")
        subprocess.check_call("cmake -S cpp/ -B cpp/cmakebuild && cmake --build cpp/cmakebuild", shell=True)

        # Copying `helloworld` to `src/.` doesn't make sense in normal mode, but it doesn't hurt.
        subprocess.check_call("cp cpp/cmakebuild/helloworld src/.", shell=True)
        
        # Copying `helloworld` to `build/lib/.` makes `helloworld` appear in venv/lib/python3.8/site-packages
        # in normal mode. This line doesn't work in develop mode. But again, it doesn't hurt.
        subprocess.check_call("cp cpp/cmakebuild/helloworld build/lib/.", shell=True)

class CustomInstall(install.install):
    def run(self):
        super(CustomInstall, self).run()
        print("Execute CustomInstall ......")
        
setup(
    cmdclass={
        'develop': CustomDevelop,
        'build_py': CustomBuildPy,
        'install': CustomInstall
    }
)
