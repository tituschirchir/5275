import csv
import pandas as pd
import helpers.global_constants as gc
from network.fin.bank_agent import Bank
from structures.bank_structures import TimeSeries


def read_csv(f_name):
    return pd.read_csv(f_name, index_col=0)


import numpy as np


def download_balance_sheet(tickers, f_loc='data/bs_ms.csv', prev_quarter=3, save=True):
    import requests
    i_loc = -prev_quarter
    assets, liab, equities = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    for tkr in tickers:
        assets2, liab2, equities2 = pd.DataFrame(columns=[tkr]), pd.DataFrame(columns=[tkr]), pd.DataFrame(
            columns=[tkr])
        download = requests.get(gc.morning_star.format(tkr))
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)[2:]
        is_reached = True
        arr_v = []
        for j in range(0, len(my_list)):
            val = my_list[j]
            if val[0] == "Assets":
                arr_v.append(j + 1)
            elif val[0] == "Liabilities":
                arr_v.append(j + 1)
            elif val[0] == "Stockholders' equity":
                arr_v.append(j + 1)
        i = 0
        for row in my_list:
            if len(row) == 1 and is_reached:
                is_reached = False
            elif len(row) > 1 and "Total" not in row[0] and row[i_loc] != '':
                value = float(row[i_loc])
                if i < arr_v[1]:
                    value += assets2.loc[row[0]] if row[0] in assets2.index else 0
                    assets2.loc[row[0]] = [value]
                elif i >= arr_v[2]:
                    value += equities2.loc[row[0]] if row[0] in equities2.index else 0
                    equities2.loc[row[0]] = [value]
                else:
                    name = 'Deferred income taxes - L' if row[0] == 'Deferred income taxes' else row[0]
                    value += liab2.loc[name] if name in liab2.index else 0
                    liab2.loc[name] = [value]
                is_reached = True
            i += 1
        if not equities2.empty and not liab2.empty and not assets2.empty:
            equities = equities.join(equities2, how='outer')
            liab = liab.join(liab2, how='outer')
            assets = assets.join(assets2, how='outer')
    assets, liab, equities = assets.fillna(0.0), liab.fillna(0.0), equities.fillna(0.0)
    bs = pd.concat([assets, liab, equities])
    if not bs.empty:
        if "Net Loans" in bs.index:
            bs = bs.drop(['Net loans'])
        if save:
            bs.to_csv(f_loc)
        return bs
    return None


import os


def get_agents():
    ts, df = None, None
    if os.path.exists('data/bs_ms.csv'):
        ts, df = read_csv('data/t_series.csv'), read_csv('data/bs_ms.csv')
        rem = [x for x in gc.network_tickers if x not in df.columns]
    else:
        rem = gc.network_tickers
    if rem:
        bs, ts2 = download_all(rem, save=False)
        if bs is not None:
            ts = ts.join(ts2, how='outer')
            df = df.join(bs, how='outer')
            ts = ts.fillna(0.0)
            df = df.fillna(0.0)
        df.to_csv('data/bs_ms.csv')
        ts.to_csv('data/t_series.csv')
    i = 0
    agents = []
    for tkr, ser in df.iteritems():
        agents.append(Bank(tkr, i, None, ser, TimeSeries(ts[tkr])))
        i += 1
    return agents


def download_ticker_series_data(tickers, f_loc, start_date="2013-12-31", end_date="2018-03-16", save=True):
    import quandl
    quandl.ApiConfig.api_key = 'iyeLXysv9-BtunNLWLGH'
    t_series = pd.DataFrame()
    for tkr in tickers:
        t_2 = quandl.get('WIKI/{}'.format(tkr.replace('.', '_')), start_date=start_date, end_date=end_date)
        t_series[tkr] = t_2['Adj. Close']
    t_series = t_series.dropna(axis=0, how='any')
    if save:
        t_series.to_csv(f_loc)
    return t_series


def download_all(tickers=gc.network_tickers, n1="data/bs_ms.csv", n2="data/t_series.csv", save=True, prev_quarter=3):
    bs = download_balance_sheet(tickers=tickers, f_loc=n1, save=save, prev_quarter=prev_quarter)
    if bs is None:
        return None, None
    ts = download_ticker_series_data(tickers=bs.columns, f_loc=n2, save=save)
    return bs, ts
