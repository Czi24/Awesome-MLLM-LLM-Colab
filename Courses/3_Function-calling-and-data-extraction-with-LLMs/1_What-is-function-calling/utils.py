import inspect
def raven_post(payload):
    """
    Sends a payload to a TGI endpoint.
    """
    # Now, let's prompt Raven!
    API_URL = "http://nexusraven.nexusflow.ai"
    headers = {
            "Content-Type": "application/json"
    }
    import requests
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def call_functioncalling_llm(prompt, api_to_call):
    """
    This function sends a request to the TGI endpoint to get Raven's function call.
    This will not generate Raven's justification and reasoning for the call, to save on latency.
    """
    signature = inspect.signature(api_to_call)
    docstring = api_to_call.__doc__
    prompt = f'''Function:\n{api_to_call.__name__}{signature}\n"""{clean_docstring(docstring)}"""\n\n\nUser Query:{prompt}<human_end>'''
    import requests
    output = raven_post({
        "inputs": prompt,
        "parameters" : {"temperature" : 0.001, "stop" : ["<bot_end>"], "do_sample" : False, "max_new_tokens" : 2048, "return_full_text": False}})
    call = output[0]["generated_text"].replace("Call:", "").strip()
    return call

def query_raven(prompt):
	"""
	This function sends a request to the TGI endpoint to get Raven's function call.
	This will not generate Raven's justification and reasoning for the call, to save on latency.
	"""
	import requests
	output = raven_post({
		"inputs": prompt,
		"parameters" : {"temperature" : 0.001, "stop" : ["<bot_end>"], "return_full_text" : False, "do_sample" : False, "max_new_tokens" : 2048}})
	call = output[0]["generated_text"].replace("Call:", "").strip()
	return call

def clean_docstring(docstring):
    if docstring is not None:
        # Remove leading and trailing whitespace
        docstring = docstring.strip()
    return docstring

def build_raven_prompt(function_list, user_query):
    import inspect
    raven_prompt = ""
    for function in function_list:
        signature = inspect.signature(function)
        docstring = function.__doc__
        prompt = \
f'''
Function:
def {function.__name__}{signature}
    """
    {clean_docstring(docstring)}
    """
    
'''
        raven_prompt += prompt
        
    raven_prompt += f"User Query: {user_query}<human_end>"
    return raven_prompt
