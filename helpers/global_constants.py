#network_tickers = 'JPM,BRK.b,BAC,WFC,C,GS,USB,MS,PNC'.split(',')
default_tick = 'JPM,BRK.b,BAC,WFC,C,GS,USB,MS,PNC,ADR,CHCO,CSBK,CMSS'
network_tickers = default_tick.replace(' ', '').split(',')
morning_star = 'http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t={}&reportType=bs&period=3&' \
               'dataType=A&order=asc&columnYear=5&number=3'
big_N = len(network_tickers)
