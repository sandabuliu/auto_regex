#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json

__author__ = 'tong'
__version__ = '1.0.0'


class AutoLogRegex(object):
    def __init__(self, knowledgebase):
        if isinstance(knowledgebase, basestring):
            with open(knowledgebase) as fp:
                knowledgebase = json.load(fp)

        self._tag = 'name'
        self._types = knowledgebase['units']
        self._rules = knowledgebase['rules']
        self._results = []
        self._patterns = []
        self._buffer = []
        self._best = None

    def _ch_type(self, s):
        for _type in self._types:
            if re.match(_type, s):
                return _type
        return None

    def _match(self, string):
        ret = []
        for rule in self._rules:
            for pattern in rule['pattern']:
                if re.match(r'^('+pattern+r')$', string):
                    temp = rule.copy()
                    temp['pattern'] = pattern
                    ret.append(temp)
                    break
        return ret

    def _convert(self, logger, res, start=0):
        if not res[start] and start == len(logger):
            self._results.append(list(self._buffer))
        for end, rule in res[start]:
            self._buffer.append({'part': logger[start: end], 'rule': rule})
            self._convert(logger, res, end)
            self._buffer.pop()

    def _string(self, parts):
        ret = []
        weight = 0
        for i, part in enumerate(parts):
            if len(part['rule']) == 1:
                rule = part['rule'][0]
            else:
                rule = max(*part['rule'], key=lambda item: item['weight'])
            weight += rule['weight']
            ret.append('(?P<%s%04d>%s)' % (self._tag, i, rule['pattern']))

        str_res = ''.join(ret)
        self._patterns.append(str_res)
        return weight, str_res

    def tag(self, tagname):
        self._tag = tagname

    def parse(self, logger):
        res = {0: []}
        length = len(logger)
        for i in range(0, length):
            if i < length-1 and self._ch_type(logger[i+1]) == self._ch_type(logger[i]):
                continue

            for mark in res.copy():
                ret = self._match(logger[mark:i+1])
                if ret:
                    res[mark].append((i+1, ret))
                    res[i+1] = []
        self._convert(logger, res)

    def patterns(self):
        if not self._patterns and self._results:
            weight, self._best = self._string(self._results[0])
            for parts in self._results:
                w, ret_str = self._string(parts)
                if weight < w:
                    self._best = ret_str
                    weight = w
        return self._patterns

    def best(self):
        if self._best is None:
            self.patterns()
        return self._best
