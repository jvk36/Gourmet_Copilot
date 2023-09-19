import re
import json

def parse_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
        sections = text.split('<end>')
        retval = {}
        for s in sections:
            try:
                matches = re.findall(r'\[(.+?)\][\n\s]*\[(.+?)\][\n\s]*(.+)', 
                    s, flags=re.DOTALL)[0]
                name = matches[0].replace(' ', '-')
                retval[name] = {
                    'ingredients': matches[1],
                    'steps': matches[2]
                }
            except:
                # print(s)
                pass
        return json.dumps(retval)

if __name__ == '__main__':
    print(parse_file('data/combined.txt'))
    # parse_file('data/combined.txt')
