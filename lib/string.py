def lstripml(s):
    """
    multi-line left strip
    """
    return '\n'.join(line.lstrip() for line in s.split('\n'))
