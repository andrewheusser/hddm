from distutils.core import setup
from distutils.extension import Extension
import numpy as np
import os

setup(
    name="HDDM",
    version="0.2a",
    author="Thomas V. Wiecki, Imri Sofer, Michael J. Frank",
    author_email="thomas_wiecki@brown.edu",
    url="http://github.com/hddm-devs/hddm",
    packages=["hddm", "hddm.tests", "hddm.sandbox"],
    package_data={"hddm":["examples/*.csv", "examples/*.conf"]},
    #package_dir={"hddm":"hddm/examples"},
    scripts=["scripts/hddm_fit.py", "scripts/hddm_demo.py"],
    description="HDDM is a python module that implements Hierarchical Bayesian estimation of Drift Diffusion Models.",
    install_requires=['NumPy >=1.3.0', 'kabuki >= 0.2a', 'pymc'],
    setup_requires=['NumPy >=1.3.0', 'kabuki >= 0.2a', 'pymc'],
    include_dirs = [np.get_include()],
    classifiers=[
                'Development Status :: 4 - Beta/Unstable',
                'Environment :: Console',
                'Operating System :: OS Independent',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved :: GNU General Public License (GPL)',
                'Programming Language :: Python',
                'Topic :: Scientific/Engineering',
                 ],
    ext_modules = [Extension("wfpt", ["src/wfpt.c"])]#, extra_compile_args=['-fopenmp'], extra_link_args=['-fopenmp'])]
)

