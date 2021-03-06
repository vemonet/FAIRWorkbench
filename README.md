![Build Status](https://github.com/fair-workflows/FAIRWorkbench/workflows/Python%20application/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/fair-workflows/FAIRWorkbench/badge.svg?branch=master)](https://coveralls.io/github/fair-workflows/FAIRWorkbench?branch=master)

# FAIRWorkbench
Modules for implementation of the FAIR Workbench.

# Prerequisites
The np scripts needs to be called to generate rsa keys in the `~/.nanopub` directory.

```shell script
fairworkflows/np mkkeys -a RSA
```


## How to run FAIR workbench
The cli interface can be run as follows:

```python workflow-cli.py generate-workflow```

You will then be prompted for the required information, after which your workflow skeleton will be generated.

If you just want to see what the output looks like, you can run:

```python generate_sample_workflow.py```

This will generate a sample workflow with one step, and place the result in the folder `sample_output/`.



# ```fairworkflows``` python library
## Installation

From the root of the repo (directory containing ```setup.py```), run:

```
pip install .
```

## Usage
In your python notebook, import the library as follows:
```
import fairworkflows as fair
```

Try out the interactive widget:
```
fair.search()
```

