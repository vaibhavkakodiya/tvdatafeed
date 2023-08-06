#!/usr/bin/env python3

import TvDatafeed 

tv = TvDatafeed()
print(tv.get_hist("CRUDEOIL", "MCX", fut_contract=1))

