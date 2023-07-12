python3 Gethisto_Inclusive.py 2017 DY ZTT
python3 Gethisto_Inclusive.py 2017 ST_t_top ST
python3 Gethisto_Inclusive.py 2017 ST_t_antitop ST
python3 Gethisto_Inclusive.py 2017 ST_tW_top ST
python3 Gethisto_Inclusive.py 2017 ST_tW_antitop ST
hadd -f Histo/HistoInclu_2017/ST.root Histo/HistoInclu_2017/ST_t_top.root Histo/HistoInclu_2017/ST_t_antitop.root Histo/HistoInclu_2017/ST_tW_top.root Histo/HistoInclu_2017/ST_tW_antitop.root 
python3 Gethisto_Inclusive.py 2017 WW2L2Nu VV
python3 Gethisto_Inclusive.py 2017 WZ2Q2L VV
python3 Gethisto_Inclusive.py 2017 WZ3LNu VV
python3 Gethisto_Inclusive.py 2017 ZZ2L2Nu VV
python3 Gethisto_Inclusive.py 2017 ZZ2Q2L VV
python3 Gethisto_Inclusive.py 2017 ZZ4L VV
hadd -f Histo/HistoInclu_2017/VV.root Histo/HistoInclu_2017/WW2L2Nu.root Histo/HistoInclu_2017/WZ2Q2L.root Histo/HistoInclu_2017/WZ3LNu.root Histo/HistoInclu_2017/ZZ2L2Nu.root Histo/HistoInclu_2017/ZZ2Q2L.root Histo/HistoInclu_2017/ZZ4L.root
python3 Gethisto_Inclusive.py 2017 TTTo2L2Nu TT
python3 Gethisto_Inclusive.py 2017 TTToHadronic TT
python3 Gethisto_Inclusive.py 2017 TTToSemiLeptonic TT
hadd -f Histo/HistoInclu_2017/TT.root Histo/HistoInclu_2017/TTToHadronic.root Histo/HistoInclu_2017/TTToSemiLeptonic.root Histo/HistoInclu_2017/TTTo2L2Nu.root
python3 Gethisto_Inclusive.py 2017 TauB data_obs
python3 Gethisto_Inclusive.py 2017 TauC data_obs
python3 Gethisto_Inclusive.py 2017 TauD data_obs
python3 Gethisto_Inclusive.py 2017 TauE data_obs
python3 Gethisto_Inclusive.py 2017 TauF data_obs
hadd -f Histo/HistoInclu_2017/Tau.root Histo/HistoInclu_2017/TauB.root Histo/HistoInclu_2017/TauC.root Histo/HistoInclu_2017/TauD.root Histo/HistoInclu_2017/TauE.root Histo/HistoInclu_2017/TauF.root
python3 Create_fake_inclusive.py --year 2017
hadd -f Histo/HistoInclu_2017/Inclusive_all.root Histo/HistoInclu_2017/ZTT.root Histo/HistoInclu_2017/VV.root Histo/HistoInclu_2017/TT.root Histo/HistoInclu_2017/ST.root Histo/HistoInclu_2017/Fake.root Histo/HistoInclu_2017/GGToTauTau.root Histo/HistoInclu_2017/Tau.root