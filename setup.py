
from distutils.core import setup
setup \
  ( name='models'
  , version='0.1'
  , packages=['models']
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