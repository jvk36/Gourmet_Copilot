import re

def parse_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
        sections = text.split('<end>')
        retval = []
        for s in sections:
            try:
                matches = re.findall(r'\[(.+?)\][\n\s]*\[(.+?)\][\n\s]*(.+)', 
                    s, flags=re.DOTALL)[0]
                retval.append({
                    'title': matches[0], 
                    'ingredients': matches[1],
                    'steps': matches[2]
                })
            except:
                print(s)
        return retval

if __name__ == '__main__':
    parse_file('./combined.txt')
