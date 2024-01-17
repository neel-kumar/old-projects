import re

pattern = re.compile(r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])")
matches = pattern.finditer("abaabaabaabaae")

for match in matches:
    print(match.group(1))
