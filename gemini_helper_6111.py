# Imports
import os
import google.generativeai as genai

def format_gemini_output(gemini_output):
    """
    Converts the raw gemini output into a list of dicts of the form {subj: ('<subject>', None ), obj: ('<object>', None) }.
    Each dict represents an extracted tuple from gemini. Note that the values in the dicts are tuples only because the calling
    code expects this format.

    :param gemini_output: text output from gemini
    """
    tups = []
    output_lines = gemini_output.split('\n')
    try:
        for line in output_lines:
            subj, relation, obj = (item.strip() for item in line[1:-1].split('|'))
            tups += [{'subj': (subj, None), 'obj': (obj, None)}]
        return tups
    except:
        print('          EXCEPTION: CANNOT PARSE GEMINI OUTPUT: "{}"'.format(gemini_output))
        return []


# Generate response to prompt
def get_gemini_completion(prompt, GEMINI_API_KEY, model_name, max_tokens, temperature, top_p, top_k):
    """
    Configure gemini model with input params.
    Call gemini API with input prompt, generated by gemini_prompt_generate().

    :param prompt: prompt text to be sent to gemini api
    :param GEMINI_API_KEY: api key for gemini
    :param model_name: model name used
    :param max_tokens: maximum output tokens
    :param temperature: degree of randomness in output token selection
    :param top_p: threshold for sum of probabilities of top tokens
    :param top_k: k-most probable next token
    """

    genai.configure(api_key=GEMINI_API_KEY)

    # Initialize a generative model
    model = genai.GenerativeModel(model_name)

    # Configure the model with your desired parameters
    generation_config=genai.types.GenerationConfig(
        max_output_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k
    )

    # Generate a response
    response = model.generate_content(prompt, generation_config=generation_config)
    
    return format_gemini_output(response.text)
