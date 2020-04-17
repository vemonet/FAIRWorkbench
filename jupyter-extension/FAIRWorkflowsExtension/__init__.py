def _jupyter_server_extension_paths():
    return [{
        "module": "FAIRWorkflowsExtension"
    }]


# Jupyter Extension points
def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `my_fancy_module` directory
        src="static",
        # directory in the `nbextension/` namespace
        dest="FAIRWorkflowsExtension",
        # _also_ in the `nbextension/` namespace
        require="FAIRWorkflowsExtension/index")]


def load_jupyter_server_extension(nbapp):
    nbapp.log.info("FAIRWorkflowsExtension enabled!")
