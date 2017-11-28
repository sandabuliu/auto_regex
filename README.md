### EXAMPLE

```python
from auto_regex import AutoLogRegex
log = '''123.126.105.104 - - [28/Nov/2015:07:59:33 +0800] "POST /api/field/list?access_token=6a6dee62188650500831e323c22f3f1d&tb_id=tb_2ee57105aa794c2da1c83ff016c3ac77 HTTP/1.1" 200 544 0.047 "-" "Apache-HttpClient/4.4 (Java 1.5 minimum; Java/1.7.0_80)" "-" - "-"'''
alr = AutoLogRegex('knowledgebase/auto')
alr.parse(log)
print alr.best()
print json.dumps(re.match(alr.best(), log).groupdict(), indent=2, sort_keys=True)
```