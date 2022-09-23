import setuptools


# The information here can also be placed in setup.cfg - better separation of
# logic and declaration, and simpler if you include description/version in a file.
setuptools.setup(
    name="pybin",
    version="1.0",
    author="Nariaki Tateiwa",
    author_email="nariaki3551@gmail.com",
    packages=setuptools.find_packages(),
    dependencies=[
        "numpy",
        "tqdm",
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "pyadd=pybin.pyadd:cli_main",
            "pycolumn=pybin.pycolumn:cli_main",
            "pycount=pybin.pycount:cli_main",
            "pyhist=pybin.pyhist:cli_main",
            "pyjoin=pybin.pyjoin:cli_main",
            "pyline=pybin.pyline:cli_main",
            "pymax=pybin.pymax:cli_main",
            "pymean=pybin.pymean:cli_main",
            "pymin=pybin.pymin:cli_main",
            "pyplot=pybin.pyplot:cli_main",
            "pyremove=pybin.pyremove:cli_main",
            "pyreplace=pybin.pyreplace:cli_main",
            "pyscatter=pybin.pyscatter:cli_main",
            "pysort=pybin.pysort:cli_main",
            "pysplit=pybin.pysplit:cli_main",
            "pystat=pybin.pystat:cli_main",
            "pysum=pybin.pysum:cli_main",
            "pyviolin=pybin.pyviolin:cli_main",
            "pywhile=pybin.pywhile:cli_main",
            "T=pybin.T:cli_main",
        ],
    },
    python_requires=">=3.8",
)
