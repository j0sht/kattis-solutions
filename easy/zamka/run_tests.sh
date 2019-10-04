#!/bin/bash

# Run tests, print each to actual output
cat test1.in | python3 zamka.py > actual1.out
cat test2.in | python3 zamka.py > actual2.out
cat test3.in | python3 zamka.py > actual3.out

# Check if diff is empty for each test, output test pass/fail
if [ "$(diff actual1.out test1.out)" == "" ]
then
    echo "Test 1: PASS"
    rm actual1.out
else
    echo "Test 1: FAIL"
fi
    
if [ "$(diff actual2.out test2.out)" == "" ]
then
    echo "Test 2: PASS"
    rm actual2.out
else
    echo "Test 2: FAIL"
fi

if [ "$(diff actual3.out test3.out)" == "" ]
then
    echo "Test 3: PASS"
    rm actual3.out
else
    echo "Test 3: FAIL"
fi
