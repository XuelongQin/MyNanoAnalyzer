python3 Gethisto_Inclusive.py 2017 DY ZTT
python3 Gethisto_Inclusive.py 2017 DY ZLL
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
python3 Gethisto_Inclusive.py 2017 SingleMuonB data_obs
python3 Gethisto_Inclusive.py 2017 SingleMuonC data_obs
python3 Gethisto_Inclusive.py 2017 SingleMuonD data_obs
python3 Gethisto_Inclusive.py 2017 SingleMuonE data_obs
python3 Gethisto_Inclusive.py 2017 SingleMuonF data_obs
hadd -f Histo/HistoInclu_2017/SingleMuon.root Histo/HistoInclu_2017/SingleMuonB.root Histo/HistoInclu_2017/SingleMuonC.root Histo/HistoInclu_2017/SingleMuonD.root Histo/HistoInclu_2017/SingleMuonE.root Histo/HistoInclu_2017/SingleMuonF.root
python3 Create_fake_inclusive.py --year 2017
hadd -f Histo/HistoInclu_2017/Inclusive_all.root Histo/HistoInclu_2017/ZTT.root Histo/HistoInclu_2017/ZLL.root Histo/HistoInclu_2017/VV.root Histo/HistoInclu_2017/TT.root Histo/HistoInclu_2017/ST.root Histo/HistoInclu_2017/Fake.root Histo/HistoInclu_2017/GGToTauTau.root Histo/HistoInclu_2017/SingleMuon.root