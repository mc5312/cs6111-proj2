# Imports
import os
import google.generativeai as genai
from gemini_prompt_generator import gemini_prompt_generate


# Apply Gemini API Key
GEMINI_API_KEY = 'AIzaSyAGiiKn8z2ZgWvIAA7Ly3DbbIjTMDa1ejk'
genai.configure(api_key=GEMINI_API_KEY)


def format_gemini_output(gemini_output):
    """
    Converts the raw gemini output into a list of dicts of the form {subj: ('<subject>', None ), obj: ('<object>', None) }.
    Each dict represents an extracted tuple from gemini. Note that the values in the dicts are tuples only because the calling
    code expects this format.
    """
    tups = []
    output_lines = gemini_output.split('\n')
    try:
        for line in output_lines:
            subj, relation, obj = (item.strip() for item in line[1:-1].split('|'))
            tups += [{'subj': (subj, None), 'obj': (obj, None)}]
        return tups
    except:
        print('EXCEPTION: CANNOT PARSE GEMINI OUTPUT: "{}"'.format(gemini_output))
        return []


# Generate response to prompt
def get_gemini_completion(prompt, model_name, max_tokens, temperature, top_p, top_k):

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

def test():

    # Feel free to modify the parameters below.
    # Documentation: https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini
    test_relation = 'Schools_Attended'
    test_text = """
                  "Timothy Donald Cook was born on November 1, 1960, in Mobile, Alabama.[10][11] He was baptized in a Baptist church[12] and grew up in nearby Robertsdale. His father was a shipyard worker,[13] and his mother worked at a pharmacy.[10][14] Cook graduated salutatorian from Robertsdale High School in Alabama in 1978.[15] He earned a Bachelor of Science degree with a major in industrial engineering from Auburn University in 1982 and a Master of Business Administration degree from Duke University in 1988.[16][17]"
                    """

    
    model_name = 'gemini-pro'
    max_tokens = 4096
    temperature = 0.2
    top_p = 1
    top_k = 32

    response_text = get_gemini_completion(gemini_prompt_generate(test_relation, test_text), model_name, max_tokens, temperature, top_p, top_k)
    print(response_text)