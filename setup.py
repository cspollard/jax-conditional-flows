
from distutils.core import setup
setup \
  ( name='jax-conditional-flows'
  , version='0.1'
  , py_modules=['models']
  , install_requires= \
    [ "numpy"
    , "scipy"
    , "matplotlib"
    , "jax"
    , "flax"
    , "distrax"
    , "optax"
    , "einops"
    , "corner"
    , "tqdm"
    ]
  )