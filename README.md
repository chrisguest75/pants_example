# PANTS EXAMPLE

Pantsbuild: The ergonomic build system

NOTES:

* THIS IS NOT CONFIGURED CORRECTLY YET.

TODO:

* Terraform
  * It's using terraform 1.9.
* Build a typescript package
* Build a typescript cli tool
* Build a python package
* Build a cpp package
* Build a docker image

## Install

```sh
brew install pantsbuild/tap/pants
```

## Configure

```sh
pants --version

pants help goals
pants help tailor
```

## Tests

```sh
pants test ::  

pants fix ::
```


## Resources

* https://www.pantsbuild.org/
* https://github.com/pantsbuild/example-python
* https://www.pantsbuild.org/stable/docs/getting-started/example-projects-and-repositories
* https://www.pantsbuild.org/stable/docs/using-pants/key-concepts/backends
* https://chrismati.cz/posts/uv-pex-monorepo/
* https://pypi.org/project/pex/