#!/bin/bash


if [ $1 ]
then
    if [ $1 == "--connectfour" ];then
        ./run ConnectFour -s 127.0.0.1 -p 3000 -r C2Demo  & #> /dev/null &
        ./run ConnectFour -s 127.0.0.1 -p 3000 -r C2Demo  > /dev/null &
    elif [ $1 == "--amazons" ];then
        ./run Amazons -s 127.0.0.1 -p 3000 -r C2Demo  & #> /dev/null &
        ./run Amazons -s 127.0.0.1 -p 3000 -r C2Demo  > /dev/null &
    elif [ $1 == "--ultimatetictactoe" ];then
        ./run UltimateTicTacToe -s 127.0.0.1 -p 3000 -r C2Demo  & #> /dev/null &
        ./run UltimateTicTacToe -s 127.0.0.1 -p 3000 -r C2Demo  > /dev/null &
    fi
fi
