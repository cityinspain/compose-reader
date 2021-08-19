def keys_to_padded_string(keys):
    l = list(keys)
    padded = ['  ' + x for x in l]
    return "\n".join(padded)

def get_field_from_each(services, field):
    output = {}
    
    for k, v in services.items():
        if (v.get(field)):
            output[k] = v[field]

    return output

def bold(string):
    openseq = "\033[1m"
    closeseq = "\033[0;0m"

    return openseq + string + closeseq