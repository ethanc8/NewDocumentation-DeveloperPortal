# GNUstep developer portal

## Installation of dependencies

First, please have Conda installed on your computer. If it's not installed, please install [Miniforge3](https://conda-forge.org/miniforge/), which includes Conda and a conda-forge based Python environment. You can install Miniforge3 using the following command:

```bash
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
rm Miniforge3-$(uname)-$(uname -m).sh
```

Close and reopen your shell, and run:

```bash
# Prevent Conda from polluting your environment when you're not working on Conda-managed projects.
conda config --set auto_activate_base false
```

Now, you can use Conda to install the dependencies.

```bash
mamba env create -f environment.yml
mamba activate NewDocumentation
```

If you modify `environment.yml`, please run

```bash
mamba env update -f environment.yml
```


## Acknowledgements

A large amount of this was modified from the new [GNOME developer documentation](https://developer.gnome.org/documentation/).

## License

Anything that was not part of the GNOME developer documentation is dual-licensed GPL-v2.0-or-later and CC-BY-SA-3.0+. Anything that was part of the GNOME developer documentation is licensed CC-BY-SA-3.0 only. See [developer.gnome.org#66](https://gitlab.gnome.org/Teams/Websites/developer.gnome.org/-/issues/66) for more information.