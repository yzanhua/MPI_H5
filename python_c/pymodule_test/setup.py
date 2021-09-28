from distutils.core import setup, Extension

math_module = Extension('myCmath', sources=['cmath.c'])

setup(
    name="cmathExtension",
    version="1.0",
    description="This is my first c math extension",
    ext_modules=[math_module]
)