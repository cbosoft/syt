# `syt` - Simple YACS Templating

`yacs` is a great tool for writing config files in yaml. It can be handy to generate a bunch of config files. This can be achieved by use of a generation script, but this is a llittle clumsy.

This tool wraps yacs, and provides a simple way to template a bunch of configs.

# Installation
TODO

# Usage

```python
from syt import CfgNode

cfg = CfgNode()
...
# initialise your default config
# Ideall this is done in a config.py or defaults.py script in your project.
...
variants = cfg.apply_template('path/to/template.syt')
# variants now contains one config for each possible config specified by the variant.
```

The template file contains simple markup in the form of double square brackets to signify permuted variables, and square brackets with an exclamation for counted variables. The former will be more common, being the options which are tried in every possible permutation together. Counted variables are used to differentiate between and keep track of experiments.
```yaml
# Example .syt yaml template
experiment_ident: [[!ID]]
training:
  n_epochs: [[100, 200, 500, 1000]]
  learning_rate: [[0.1, 0.01, 0.001, 1e-4]]
model:
  n_layers: [[2, 4, 6, 10]]
```