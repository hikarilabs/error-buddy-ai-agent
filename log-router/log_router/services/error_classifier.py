def generate_llm_args_dict(
        temperature: float = None,
        top_p: float = None,
        max_tokens: int = 2048) -> dict:
    """
    This function generates a set of default arguments passed to an LLM call. If otherwise specified in
    the function call, it will return the arguments passed to it.

    Args:
        :param temperature: randomness of the response (lower = more deterministic)
        :param top_p: diversity via nucleus sampling
        :param max_tokens: Maximum number of tokens to generate
    Returns:
        A dictionary containing the LLM arguments
    """

    # Create the dictionary with the necessary parameters
    llm_args = {
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens,
    }

    return llm_args


class ErrorClassifier:
    def __init__(self, prompt, llm, llm_args: dict = None):
        """

        :param prompt: user prompt containing the system pro
        :param llm: the
        :param llm_args:
        """
        self.prompt = prompt
        self.llm = llm

        # we allow llm_args to set at class creation, however, if not set, they will be initialized with the
        # default values here
        if llm_args is None:
            self.llm_args = {
                ""
            }
        else:
            self.llm_args = generate_llm_args_dict()

    def classify(self, error_message):
        pass


