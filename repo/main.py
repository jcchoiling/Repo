#!/usr/bin/env python
# -*- coding: utf-8 -*-

import context
import lib.commons


class MyRepo():

    def run(self):
        print("run..")


if __name__ == '__main__':
	r = MyRepo()
	r.run()
	lib.commons.login()

