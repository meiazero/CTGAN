"""CTGAN generator and discriminator as an installable package: `ctgan.CTGAN`.

Every other module here is a symlink to the upstream file in `model/`, so the package holds
the networks only, without the scripts' dependencies, which stay in the `scripts` dependency
group.
"""
