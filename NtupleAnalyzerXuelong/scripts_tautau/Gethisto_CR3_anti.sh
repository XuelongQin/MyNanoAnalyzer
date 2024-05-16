python3 Gethisto_CR3_anti.py 2018 DY ZTT
python3 Gethisto_CR3_anti.py 2018 ST_t_top ST
python3 Gethisto_CR3_anti.py 2018 ST_t_antitop ST
python3 Gethisto_CR3_anti.py 2018 ST_tW_top ST
python3 Gethisto_CR3_anti.py 2018 ST_tW_antitop ST
hadd -f Histo/HistoCR3_anti_2018/ST.root Histo/HistoCR3_anti_2018/ST_t_top.root Histo/HistoCR3_anti_2018/ST_t_antitop.root Histo/HistoCR3_anti_2018/ST_tW_top.root Histo/HistoCR3_anti_2018/ST_tW_antitop.root 
python3 Gethisto_CR3_anti.py 2018 WZ2Q2L VV
python3 Gethisto_CR3_anti.py 2018 WZ3LNu VV
python3 Gethisto_CR3_anti.py 2018 VV2L2Nu VV
python3 Gethisto_CR3_anti.py 2018 ZZ2Q2L VV
python3 Gethisto_CR3_anti.py 2018 ZZ4L VV
hadd -f Histo/HistoCR3_anti_2018/VV.root Histo/HistoCR3_anti_2018/WZ2Q2L.root Histo/HistoCR3_anti_2018/WZ3LNu.root Histo/HistoCR3_anti_2018/VV2L2Nu.root Histo/HistoCR3_anti_2018/ZZ2Q2L.root Histo/HistoCR3_anti_2018/ZZ4L.root
python3 Gethisto_CR3_anti.py 2018 TTTo2L2Nu TT
python3 Gethisto_CR3_anti.py 2018 TTToHadronic TT
python3 Gethisto_CR3_anti.py 2018 TTToSemiLeptonic TT
hadd -f Histo/HistoCR3_anti_2018/TT.root Histo/HistoCR3_anti_2018/TTToHadronic.root Histo/HistoCR3_anti_2018/TTToSemiLeptonic.root Histo/HistoCR3_anti_2018/TTTo2L2Nu.root
python3 Gethisto_CR3_anti.py 2018 TauA data_obs
python3 Gethisto_CR3_anti.py 2018 TauB data_obs
python3 Gethisto_CR3_anti.py 2018 TauC data_obs
python3 Gethisto_CR3_anti.py 2018 TauD data_obs
hadd -f Histo/HistoCR3_anti_2018/Tau.root Histo/HistoCR3_anti_2018/TauA.root Histo/HistoCR3_anti_2018/TauB.root Histo/HistoCR3_anti_2018/TauC.root Histo/HistoCR3_anti_2018/TauD.root
python3 Create_fake_CR3.py --year 2018
