#!/bin/bash
SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
duka EURUSD -c M1 --f $SCRIPTPATH/../data --header
echo -ne '\n' | duka XAUUSD -c M1 --f $SCRIPTPATH/../data --header
echo -ne '\n' | duka AUDUSD -c M1 --f $SCRIPTPATH/../data --header
echo -ne '\n' | duka NZDUSD -c M1 --f $SCRIPTPATH/../data --header
echo -ne '\n' | duka USDJPY -c M1 --f $SCRIPTPATH/../data --header
echo -ne '\n' | duka EURJPY -c M1 --f $SCRIPTPATH/../data --header
echo -ne '\n' | duka GBPUSD -c M1 --f $SCRIPTPATH/../data --header
