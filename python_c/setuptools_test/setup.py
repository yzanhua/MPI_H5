from setuptools import setup, Extension, find_packages

math_module = Extension(name='cmod.myCmath',
                        sources=['src/cmod/cmath.c'],
                        language="c",
                        extra_compile_args=['-DNDEBUG -O3']  # this makes no difference
                        )


setup(
    name="cmod",
    version="1.0",
    description="This is my second c math extension using setuptools",
    packages=find_packages("src"),
    package_dir={'': 'src'},
    ext_modules=[math_module]
)
