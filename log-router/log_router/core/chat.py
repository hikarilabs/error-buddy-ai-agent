import requests
import json


def safe_single_message_chat(
    prompt: str,
    inference_url: str,
    role: str = "user",
    top_p: float = None,
    temperature: float = None,
    max_tokens: int = 500,
    model: str = "Llama 3.2 1B Instruct",
    stream: bool = False,
    **kwargs,
):
    """
    Sends a user prompt to an LLM. The prompt MUST have passed a safety check before invoking this function
    :param prompt: sanitized user prompt
    :param inference_url: the url of the inference point
    :param role: role
    :param top_p:
    :param temperature:
    :param max_tokens: restrict the number of tokens sent by the LLM in the response
    :param model: if not set the model name defaults to llama3.2:1b
    :param stream: specify if a streaming response is expected, defaults to False
    :param kwargs:
    :return:
    """
    if top_p is None:
        top_p = "none"

    if temperature is None:
        temperature = "none"

    payload = {
        "model": model,
        "messages": [{"role": role, "content": prompt}],
        "top_p": top_p,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": stream,
        **kwargs,
    }

    response = requests.post(inference_url, json=payload)

    if not response.ok:
        raise Exception(f"While calling the LLM the following error occurred: f{response.text}")

    try:
        json_response = json.loads(response.text)
        if "message" in json_response and "content" in json_response["message"]:
            output_dict = {
                "role": json_response["message"]["role"],
                "content": json_response["message"]["content"]
            }
            return output_dict

    except Exception as e:
        raise Exception(
            f"Failed to get a response with exception: {e}\n Received LLM response was: {response.text}"
        )

