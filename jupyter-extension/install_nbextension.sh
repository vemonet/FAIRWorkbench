#jupyter-nbextension install FAIRWorkflowsExtension
#jupyter-nbextension enable FAIRWorkflowsExtension/main

jupyter-nbextension install --py FAIRWorkflowsExtension --sys-prefix
jupyter-nbextension enable --py FAIRWorkflowsExtension --sys-prefix
jupyter-serverextension enable --py FAIRWorkflowsExtension --sys-prefix
