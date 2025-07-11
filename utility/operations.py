class Operations:
    
    @staticmethod
    def parse_metric_string(s: str) -> float:
        """Parse a numeric string, removing spaces and handling percentage."""
        s = s.strip().replace(' ', '')
        if s.endswith('%'):
            s = s[:-1]
        if s.endswith('ms'):
            s = s[:-2]
        if s.endswith('s'):
            s = s[:-1] + '0'
        if "." not in s:
            s += '.00'
        return float(s)