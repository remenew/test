#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:14:48 2021

@author: wangyuan
"""
import sqlite3

def initDB():
    conn = sqlite3.connect('stock.db')
    conn.isolation_level = None
    return conn

def createTable(conn):
    conn.execute('''CREATE TABLE indexgz
       (CODE TEXT     NOT NULL,
       DATE  TEXT    NOT NULL,
       NAME           TEXT    NOT NULL,
       INDICATORTYPE   TEXT,
       OPEN           REAL,
       CLOSE          REAL,
       UP             REAL,
       DOWN           REAL,
       TRADINGVOLUME  REAL,
       TRADINGAMOUNT  REAL,
       AMPLITUDE      REAL,
       VOLUMERATIO    REAL,
       PETTM          REAL,
       PES            REAL,
       PEG            REAL,
       PS             REAL,
       PCF            REAL,
       PB             REAL,
       FLUCTUATIONRANGE  REAL,
       TOTALMARKETVALUE  REAL,
       CIRCULATIONMARKETVALUE      REAL,
       MEANMARKETVALUE   REAL,
       COMPONYNUM       INTEGER,
       LOSSCOMPONYNUM   INTEGER,
       PRIMARY KEY (code,date));''')
def createTable2(conn):
    conn.execute('''CREATE TABLE hygzb
       (CODE TEXT     NOT NULL,
       DATE  TEXT    NOT NULL,
       NAME           TEXT,
       INDICATORTYPE   TEXT,
       OPEN           REAL,
       CLOSE          REAL,
       UP             REAL,
       DOWN           REAL,
       TRADINGVOLUME  REAL,
       TRADINGAMOUNT  REAL,
       AMPLITUDE      REAL,
       VOLUMERATIO    REAL,
       PETTM          REAL,
       PES            REAL,
       PEG            REAL,
       PS             REAL,
       PCF            REAL,
       PB             REAL,
       FLUCTUATIONRANGE  REAL,
       TOTALMARKETVALUE  REAL,
       CIRCULATIONMARKETVALUE      REAL,
       MEANMARKETVALUE   TEXT,
       MEANCIRCULATIONMARKETVALUE   TEXT,
       MEANEQUITY       TEXT,
       MEANCIRCULATIONEQUITY  TEXT,
       COMPONYNUM       INTEGER,
       LOSSCOMPONYNUM   INTEGER,
       PRIMARY KEY (code,date));''')
def createCB(conn):
    conn.execute('''CREATE TABLE cbb
       (CODE TEXT     NOT NULL,
       DATE  TEXT    NOT NULL,
       NAME           TEXT,
       PRICE           REAL,
       DELTA          REAL,
       STOCKCODE      TEXT,
       STOCKNAME      TEXT,
       STOCKPRICE     REAL,
       STOCKDELTA     REAL,
       CONVERTEPRICE      REAL,
       CONVERTEVALUE       REAL,
       CONVERTEPREMIUMRATE          REAL,
       DEBTPREMIUMRATE            REAL,
       RESALEPRICE            REAL,
       REDEPTIONPRICE             REAL,
       REDEEMPRICE            REAL,
       DEBTPRICE             REAL,
       STARTCONVERTEDATE  TEXT,
       IPODATE  TEXT,
       BUYDATE      TEXT,
       PRIMARY KEY (CODE,DATE));''')