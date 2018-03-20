from os.path import dirname

MAIN_DIRECTORY = dirname(dirname(__file__))

kawai = "Kamada Kawai"
layouts = ['Circular', kawai, 'Random', 'Rescale', "Shell", "Spring", "Spectral", "Fruchterman Reingold"]
network_types = ['Erdos', 'Barabasi']

morning_star = 'http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t={}&reportType=bs&period=3&dataType=A&order=asc&columnYear=5&number=3'

all_financials = [
    'PIH', 'TURN', 'FCCY', 'SRCE', 'ABIL', 'ANCX', 'ACNB', 'AGFS', 'AGFSW', 'ABTX', 'AMR', 'AMRWW', 'AMBC', 'AMBCW',
    'ATAX', 'AMNB', 'ANAT', 'AMRB', 'ABCB', 'AMSF', 'ASRV', 'ASRVP', 'ATLO', 'AFSI', 'ANCB', 'ANDA', 'ANDAR', 'ANDAU',
    'ANDAW', 'ACGL', 'ACGLO', 'ACGLP', 'AGII', 'AGIIL', 'AROW', 'ASFI', 'ATAC', 'ATACR', 'ATACU', 'AAME', 'ACBI',
    'ACFC', 'ATLC', 'AFH', 'AFHBL', 'AUBN', 'BWINA', 'BWINB', 'BANF', 'BANFP', 'BCTF', 'BOCH', 'BMRC', 'BMLP', 'BKSC',
    'BOTJ', 'OZRK', 'BFIN', 'BWFG', 'BANR', 'DFVL', 'DFVS', 'DLBL', 'DLBS', 'DTUL', 'DTUS', 'DTYL', 'DTYS', 'FLAT',
    'STPP', 'TAPR', 'BHAC', 'BHACR', 'BHACU', 'BHACW', 'BYBK', 'BCBP', 'BSF', 'BNCL', 'BGCP', 'BRPA', 'BRPAR', 'BRPAU',
    'BRPAW', 'BCAC', 'BCACR', 'BCACU', 'BCACW', 'BRAC', 'BRACR', 'BRACU', 'BRACW', 'HAWK', 'BCOR', 'BHBK', 'BOFI',
    'BOFIL', 'BOKF', 'BOKFL', 'BOMN', 'BPFH', 'BPFHP', 'BPFHW', 'BDGE', 'BHF', 'BYFC', 'BPY', 'BRKL', 'BMTC', 'BLMT',
    'CFFI', 'CATC', 'CAC', 'CCBG', 'CFFN', 'CSTR', 'CARO', 'CART', 'CARV', 'CATY', 'CATYW', 'CBFV', 'CBOE', 'CBTX',
    'CSFL', 'CFBK', 'CVCY', 'CNBKA', 'CHFN', 'CHFC', 'CHMG', 'CCCR', 'JRJC', 'HGSH', 'CLDC', 'CINF', 'CZNC', 'CZWI',
    'CZFC', 'CIZN', 'CHCO', 'CIVB', 'CIVBP', 'CSBK', 'CMSS', 'CMSSR', 'CMSSU', 'CMSSW', 'CME', 'CCNE', 'CWAY', 'COBZ',
    'CVLY', 'CIGI', 'CBAN', 'COLB', 'CBSH', 'CBSHP', 'ESXB', 'CFBI', 'CTBI', 'CWBC', 'CNFR', 'CNOB', 'CNAC', 'CNACR',
    'CNACU', 'CNACW', 'CPSS', 'CRVL', 'ICBK', 'COWN', 'COWNZ', 'PMTS', 'CACC', 'DGLD', 'DSLV', 'GLDI', 'SLVO', 'TVIX',
    'TVIZ', 'UGLD', 'USLV', 'USOI', 'VIIX', 'VIIZ', 'ZIV', 'CRESY', 'CVBF', 'DFBHU', 'DHIL', 'DCOM', 'DNBF', 'DGICA',
    'DGICB', 'LYL', 'DOTA', 'DOTAR', 'DOTAU', 'DOTAW', 'ETFC', 'EBMT', 'EGBN', 'EFBI', 'EWBC', 'EACQ', 'EACQU', 'EACQW',
    'EHTH', 'ELEC', 'ELECU', 'ELECW', 'ESBK', 'EMCI', 'EMCF', 'ECPG', 'ESGR', 'ENFC', 'EBTC', 'EFSC', 'EQFN', 'EQBK',
    'ERIE', 'ESQ', 'ESSA', 'EEFT', 'FANH', 'FMAO', 'FFKT', 'FMNB', 'FBSS', 'FSAC', 'FSACU', 'FSACW', 'FNHC', 'FFBW',
    'FDBC', 'LION', 'FITB', 'FITBI', 'FNGN', 'FISI', 'FNTE', 'FNTEU', 'FNTEW', 'FBNC', 'FNLC', 'BUSE', 'FBIZ', 'FCAP',
    'FCNCA', 'FCBC', 'FCCO', 'FBNK', 'FDEF', 'FFBC', 'FFBCW', 'FFIN', 'THFF', 'FFNW', 'FFWM', 'FGBI', 'FHB', 'INBK',
    'INBKL', 'FIBK', 'FRME', 'FMBH', 'FMBI', 'FNWB', 'FSFG', 'FUNC', 'FUSB', 'FSV', 'FFIC', 'FNBG', 'FNCB', 'FRPH',
    'FSBW', 'FSBC', 'FULT', 'GABC', 'GBCI', 'GLBZ', 'GBLI', 'GBLIL', 'GBLIZ', 'GPAQ', 'GPAQU', 'GPAQW', 'GSHT', 'GSHTU',
    'GSHTW', 'GOV', 'GOVNI', 'GSBC', 'GNBC', 'GCBC', 'GLRE', 'GRIF', 'GGAL', 'GTYH', 'GTYHU', 'GTYHW', 'GBNK', 'GNTY',
    'GFED', 'GWGH', 'HALL', 'HBK', 'HLNE', 'HBHC', 'HBHCL', 'HAFC', 'HONE', 'HWBK', 'HYAC', 'HYACU', 'HYACW', 'HIIQ',
    'HTLF', 'HNNA', 'HTBK', 'HFWA', 'HX', 'HMNF', 'HBCP', 'HOMB', 'HFBL', 'HMST', 'HMTA', 'HTBI', 'HOPE', 'HFBC',
    'HBNC', 'HBMD', 'HBAN', 'HBANN', 'HBANO', 'HVBC', 'IAM', 'IAMXR', 'IAMXW', 'IBKC', 'IBKCO', 'IBKCP', 'ICCH', 'IROQ',
    'ILG', 'INDB', 'IBCP', 'IBTX', 'INDU', 'INDUU', 'INDUW', 'IPCC', 'IBKR', 'IBOC', 'INTL', 'ISTR', 'ISBC', 'ITIC',
    'JXSB', 'JRVR', 'JTPY', 'KAAC', 'KAACU', 'KAACW', 'KBLM', 'KBLMR', 'KBLMU', 'KBLMW', 'KRNY', 'KFFB', 'KINS', 'KNSL',
    'LSBK', 'LBAI', 'LKFN', 'LCA', 'LCAHU', 'LCAHW', 'LARK', 'LCNB', 'LTXB', 'LACQ', 'LACQU', 'LACQW', 'TREE', 'LX',
    'LOB', 'LIVE', 'LMFA', 'LMFAW', 'LPLA', 'LBC', 'MBTF', 'MACQ', 'MACQW', 'MIII', 'MIIIU', 'MIIIW', 'MCBC', 'MFNC',
    'MGYR', 'MHLD', 'MSFG', 'MLVF', 'MKTX', 'MRLN', 'MPAC', 'MPACU', 'MPACW', 'MBFI', 'MBFIO', 'MFIN', 'MFINL', 'MELR',
    'MBWM', 'MBIN', 'EBSB', 'CASH', 'MPB', 'MBCN', 'MSBI', 'MOFG', 'MMAC', 'MMDM', 'MMDMR', 'MMDMU', 'MMDMW', 'MORN',
    'MSBF', 'MTEC', 'MTECU', 'MTECW', 'MUDS', 'MUDSU', 'MUDSW', 'MFSF', 'MVBF', 'NDAQ', 'NKSH', 'NCOM', 'NESR', 'NESRW',
    'NGHC', 'NGHCN', 'NGHCO', 'NGHCP', 'NGHCZ', 'NHLD', 'NHLDW', 'NSEC', 'NWLI', 'JSM', 'NAVI', 'NBTB', 'NEBU', 'NEBUU',
    'NEBUW', 'UEPS', 'NYMTP', 'NMRK', 'NODK', 'NICK', 'NCBS', 'NMIH', 'NBN', 'NTRS', 'NTRSP', 'NFBK', 'NRIM', 'NWBI',
    'NWFL', 'OVLY', 'OCFC', 'OFED', 'OVBC', 'OLBK', 'ONB', 'OPOF', 'OSBC', 'OSBCP', 'OPESU', 'OBAS', 'OPHC', 'ORIT',
    'ORRF', 'OSPR', 'OSPRU', 'OSPRW', 'OTTW', 'OXBR', 'OXBRW', 'PMBC', 'PPBI', 'PACW', 'PKBK', 'PBHC', 'PNBK', 'PYDS',
    'PBBI', 'PCSB', 'PDLB', 'PGC', 'PWOD', 'WRLS', 'WRLSR', 'WRLSU', 'WRLSW', 'PEBO', 'PEBK', 'PFIS', 'PBCT', 'PBCTP',
    'PUB', 'PICO', 'PNFP', 'EAGL', 'EAGLU', 'EAGLW', 'PLBC', 'PBSK', 'BPOP', 'BPOPM', 'BPOPN', 'PBIB', 'PRAA', 'PFBI',
    'PFG', 'PVBC', 'PROV', 'PBIP', 'QCRH', 'RNDB', 'RBB', 'RDFN', 'RBNC', 'RNST', 'RBCAA', 'FRBK', 'RVSB', 'STBA',
    'SCAC', 'SCACU', 'SCACW', 'SAFT', 'SAL', 'SASR', 'SBFG', 'SBFGP', 'SBCF', 'SNFCA', 'SEIC', 'SLCT', 'SIGI', 'STNL',
    'STNLU', 'STNLW', 'SFBS', 'SVBI', 'SHBI', 'SIFI', 'SIEB', 'BSRR', 'SBNY', 'SBNYW', 'SAMG', 'SFNC', 'SLM', 'SLMBP',
    'SMBK', 'SFBC', 'SSB', 'SFST', 'SMBC', 'SONA', 'SBSI', 'SSLJ', 'STFC', 'STBZ', 'STLR', 'STLRU', 'STLRW', 'SBT',
    'SSFN', 'SYBT', 'SMMF', 'SBBX', 'SIVB', 'TROW', 'AMTD', 'TBNK', 'TCBI', 'TCBIL', 'TCBIP', 'TCBIW', 'TFSL', 'TBBK',
    'CG', 'TCGP', 'TCFC', 'FBMS', 'FLIC', 'NAVG', 'TIL', 'TSBK', 'TIPT', 'TMSR', 'TMSRW', 'TCBK', 'TSC', 'TBK', 'TRST',
    'TRMK', 'TRCB', 'GROW', 'UMBF', 'UMPQ', 'UNAM', 'UBSH', 'UNB', 'UBCP', 'UBOH', 'UBSI', 'UCBA', 'UCBI', 'UCFC',
    'UBNK', 'UFCS', 'UIHC', 'UBFO', 'UNTY', 'UVSP', 'VALU', 'VEAC', 'VEACU', 'VEACW', 'VBTX', 'VCTR', 'VBFC', 'VIRT',
    'VRTS', 'VRTSP', 'WAFD', 'WAFDW', 'WASH', 'WSBF', 'WCFB', 'WEBK', 'WSBC', 'WTBA', 'WABC', 'WNEB', 'WLTW', 'WINS',
    'WTFC', 'WTFCM', 'WTFCW', 'WETF', 'WMIH', 'WRLD', 'WSFS', 'WVFC', 'YRIV', 'YIN', 'ZAIS', 'ZION', 'ZIONW', 'ZIONZ',
    'ABM', 'AEB', 'AED', 'AEG', 'AEH', 'AEK', 'AMG', 'AFL', 'Y', 'AB', 'NFJ', 'ALL', 'ALLY', 'AEL', 'AXP', 'AFG',
    'AFGE', 'AFGH', 'AIG', 'ARL', 'AMP', 'AFSS', 'AFST', 'AON', 'APO', 'ARES', 'AI', 'AIC', 'AIW', 'AHH', 'AJG', 'APAM',
    'AHL', 'ASB', 'AC', 'AIZ', 'AGO', 'ATH', 'AXS', 'BANC', 'BBVA', 'BBD', 'BBDO', 'BCH', 'BLX', 'BSMX', 'BSBR', 'BSAC',
    'SAN', 'CIB', 'BXS', 'BAC', 'BAC^W', 'BAC^Y', 'BOH', 'BMO', 'NTB', 'BK', 'BNS', 'BKU', 'BCS', 'BBT', 'BFR', 'BBX',
    'BHLB', 'BGCA', 'BLK', 'BCRH', 'BXG', 'BRO', 'BY', 'GYB', 'PFH', 'CADE', 'CM', 'COF', 'COF^C', 'CIC', 'CBG', 'CO',
    'LFC', 'XRF', 'CB', 'CIT', 'BLW', 'C', 'C^K', 'C^N', 'CFG', 'CIA', 'CNA', 'CNO', 'CNS', 'CMA', 'CBU', 'GYC', 'CPF',
    'BAP', 'CS', 'CFR', 'CURO', 'CUBI', 'CUBS', 'DKT', 'DB', 'DXB', 'DFS', 'DHCP', 'DNB', 'EV', 'ELVT', 'EFC', 'EIG',
    'ENVA', 'EFX', 'ESNT', 'EVR', 'RE', 'EVRI', 'FNB', 'FBK', 'FFG', 'FCB', 'AGM', 'FII', 'FG', 'FNF', 'FAC', 'FAF',
    'FBP', 'FCF', 'FHN', 'FPH', 'FBC', 'FOR', 'FSB', 'BEN', 'RESI', 'GCAP', 'GBL', 'GZT', 'GNW', 'GTY', 'GIG', 'GS',
    'GWB', 'GDOT', 'GHL', 'AVAL', 'SUPV', 'HGH', 'HIG', 'HCI', 'HDB', 'HRTG', 'HTH', 'HMN', 'HLI', 'HSBC', 'HSEA',
    'HSEB', 'HPP', 'IBN', 'IHC', 'ING', 'ISF', 'ISG', 'IIPR', 'ICE', 'IVZ', 'ITG', 'INVH', 'ITCB', 'ITUB', 'JPM',
    'JPM^A', 'JPM^H', 'JHG', 'JMP', 'JMPB', 'JMPD', 'JLL', 'KB', 'KMPA', 'KMPR', 'KW', 'KEY', 'KFS', 'KKR', 'LAZ',
    'LGC', 'LM', 'LMHA', 'LMHB', 'JBK', 'KTH', 'KTN', 'KTP', 'LEJU', 'LNC', 'LYG', 'L', 'MTB', 'BMA', 'MHLA', 'MHNC',
    'MN', 'MFC', 'MMI', 'MKL', 'VAC', 'MMC', 'MLP', 'MBI', 'MDLQ', 'MDLX', 'MDLY', 'MCY', 'PIY', 'MET', 'MCB', 'MFCB',
    'MTG', 'MSL', 'MTU', 'MFG', 'MC', 'MCO', 'MS', 'MOSC', 'HJV', 'NTP', 'NBHC', 'NSM', 'NNI', 'NYCB', 'NOAH', 'NMR',
    'OAK', 'OZM', 'OCN', 'OFG', 'OFG^A', 'ORI', 'OMAA', 'OMAM', 'ONDK', 'OMAD', 'OMF', 'OPY', 'IX', 'PFSI', 'PHH',
    'PJC', 'PJT', 'PNC', 'PPDF', 'PYS', 'PYT', 'PRI', 'PRA', 'PGR', 'PB', 'PFS', 'PFK', 'PJH', 'PRH', 'PRU', 'PUK',
    'PZN', 'QD', 'RDN', 'RJF', 'RMAX', 'RLGY', 'RWGE', 'RM', 'RF', 'RGA', 'RZA', 'RZB', 'RNR', 'RLI', 'ROL', 'RY',
    'RBS', 'SPGI', 'SFE', 'SC', 'JBN', 'JBR', 'SGZA', 'SRG', 'SHG', 'IPOA', 'STT', 'STL', 'STL^A', 'STC', 'SF', 'SF^A',
    'SFB', 'GJH', 'GJO', 'GJS', 'SMFG', 'SLF', 'STI', 'SYF', 'SNV', 'GJT', 'GJV', 'TCF', 'TRC', 'TRNO', 'BX', 'SCHW',
    'THG', 'THGA', 'TRV', 'TPRE', 'TMK', 'TD', 'TPGE', 'TPGH', 'TRU', 'GTS', 'USB', 'USB^A', 'UBS', 'UVE', 'UNM', 'UE',
    'VR', 'VLY', 'VLY^A', 'VOYA', 'WRB', 'WDR', 'WD', 'WBS', 'WFC', 'WAL', 'WALA', 'WBK', 'WHG', 'WTM', 'WF', 'XL',
    'YRD', 'ZBK']