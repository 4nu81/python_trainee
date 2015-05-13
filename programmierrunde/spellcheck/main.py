#! /usr/bin/env python
# -*- coding: utf-8 -*-

import spellcheck
import cmd

if __name__ == '__main__':
	wbn = cmd.get_wb_name()
	tdn = cmd.get_txt_name()
	spellcheck.oeffnen(tdn = tdn, wbn = wbn)