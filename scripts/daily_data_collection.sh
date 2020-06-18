#!/bin/bash
duka EURUSD -c M1 --f $HOME/trading-para-todos/data --header
echo -ne '\n' | duka XAUUSD -c M1 --f $HOME/trading-para-todos/data --header
echo -ne '\n' | duka AUDUSD -c M1 --f $HOME/trading-para-todos/data --header
echo -ne '\n' | duka NZDUSD -c M1 --f $HOME/trading-para-todos/data --header
echo -ne '\n' | duka USDJPY -c M1 --f $HOME/trading-para-todos/data --header
echo -ne '\n' | duka EURJPY -c M1 --f $HOME/trading-para-todos/data --header
echo -ne '\n' | duka GBPUSD -c M1 --f $HOME/trading-para-todos/data --header
