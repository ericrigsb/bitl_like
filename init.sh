#!/bin/bash
rm -rf bitl_like
wait
git clone https://github.com/ericrigsb/bitl_like.git
wait
cd bitl_like/app
wait
pip install -r requirements.txt && python3 -u bot.py