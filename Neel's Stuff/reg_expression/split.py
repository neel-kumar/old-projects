
regex_pattern = r",|\."   
# Do not delete 'r'.
st = "100,000,000.000"   
import re
print("\n".join(re.split(regex_pattern, st)))