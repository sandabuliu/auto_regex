### EXAMPLE

```python
import re
import json
from auto_regex import AutoLogRegex
log = '''123.126.105.104 - - [28/Nov/2015:07:59:33 +0800] "POST /test HTTP/1.1" 200 544 0.047 "-" "Apache-HttpClient/4.4 (Java 1.5 minimum; Java/1.7.0_80)" "-" - "-"'''
alr = AutoLogRegex()
alr.parse(log)
print alr.best()
print
print json.dumps(re.match(alr.best(), log).groupdict(), indent=2, sort_keys=True)
```

输出结果
```
(?P<name0000>(((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))))(?P<name0001>\s+)(?P<name0002>[:\-/\.\[\]\(\)\?=&"])(?P<name0003>\s+)(?P<name0004>[:\-/\.\[\]\(\)\?=&"])(?P<name0005>\s+)(?P<name0006>[:\-/\.\[\]\(\)\?=&"])(?P<name0007>\d{2}/(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/\d{4}:\d{2}:\d{2}:\d{2}(\.\d+)?( \+\d{4})?)(?P<name0008>[:\-/\.\[\]\(\)\?=&"])(?P<name0009>\s+)(?P<name0010>[:\-/\.\[\]\(\)\?=&"])(?P<name0011>OPTIONS|HEAD|GET|POST|PUT|DELETE|TRACE|CONNECT)(?P<name0012>\s+)(?P<name0013>[:\-/\.\[\]\(\)\?=&"])(?P<name0014>\w+)(?P<name0015>\s+)(?P<name0016>\w+)(?P<name0017>[:\-/\.\[\]\(\)\?=&"])(?P<name0018>\d+\.\d+)(?P<name0019>[:\-/\.\[\]\(\)\?=&"])(?P<name0020>\s+)(?P<name0021>\d+)(?P<name0022>\s+)(?P<name0023>\d+)(?P<name0024>\s+)(?P<name0025>\d+\.\d+)(?P<name0026>\s+)(?P<name0027>"[^"]*?")(?P<name0028>\s+)(?P<name0029>"[^"]*?")(?P<name0030>\s+)(?P<name0031>"[^"]*?")(?P<name0032>\s+)(?P<name0033>[:\-/\.\[\]\(\)\?=&"])(?P<name0034>\s+)(?P<name0035>"[^"]*?")

{
  "name0000": "123.126.105.104",
  "name0001": " ",
  "name0002": "-",
  "name0003": " ",
  "name0004": "-",
  "name0005": " ",
  "name0006": "[",
  "name0007": "28/Nov/2015:07:59:33 +0800",
  "name0008": "]",
  "name0009": " ",
  "name0010": "\"",
  "name0011": "POST",
  "name0012": " ",
  "name0013": "/",
  "name0014": "test",
  "name0015": " ",
  "name0016": "HTTP",
  "name0017": "/",
  "name0018": "1.1",
  "name0019": "\"",
  "name0020": " ",
  "name0021": "200",
  "name0022": " ",
  "name0023": "544",
  "name0024": " ",
  "name0025": "0.047",
  "name0026": " ",
  "name0027": "\"-\"",
  "name0028": " ",
  "name0029": "\"Apache-HttpClient/4.4 (Java 1.5 minimum; Java/1.7.0_80)\"",
  "name0030": " ",
  "name0031": "\"-\"",
  "name0032": " ",
  "name0033": "-",
  "name0034": " ",
  "name0035": "\"-\""
}
```