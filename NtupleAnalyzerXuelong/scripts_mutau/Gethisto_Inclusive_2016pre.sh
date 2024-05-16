python3 Gethisto_Inclusive.py 2016pre DY ZTT
python3 Gethisto_Inclusive.py 2016pre DY ZLL
python3 Gethisto_Inclusive.py 2016pre ST_t_top ST
python3 Gethisto_Inclusive.py 2016pre ST_t_antitop ST
python3 Gethisto_Inclusive.py 2016pre ST_tW_top ST
python3 Gethisto_Inclusive.py 2016pre ST_tW_antitop ST
hadd -f Histo/HistoInclu_2016pre/ST.root Histo/HistoInclu_2016pre/ST_t_top.root Histo/HistoInclu_2016pre/ST_t_antitop.root Histo/HistoInclu_2016pre/ST_tW_top.root Histo/HistoInclu_2016pre/ST_tW_antitop.root 
python3 Gethisto_Inclusive.py 2016pre WZ2Q2L VV
python3 Gethisto_Inclusive.py 2016pre WZ3LNu VV
python3 Gethisto_Inclusive.py 2016pre VV2L2Nu VV
python3 Gethisto_Inclusive.py 2016pre ZZ2Q2L VV
python3 Gethisto_Inclusive.py 2016pre ZZ4L VV
hadd -f Histo/HistoInclu_2016pre/VV.root Histo/HistoInclu_2016pre/WZ2Q2L.root Histo/HistoInclu_2016pre/WZ3LNu.root Histo/HistoInclu_2016pre/VV2L2Nu.root Histo/HistoInclu_2016pre/ZZ2Q2L.root Histo/HistoInclu_2016pre/ZZ4L.root
python3 Gethisto_Inclusive.py 2016pre TTTo2L2Nu TT
python3 Gethisto_Inclusive.py 2016pre TTToHadronic TT
python3 Gethisto_Inclusive.py 2016pre TTToSemiLeptonic TT
hadd -f Histo/HistoInclu_2016pre/TT.root Histo/HistoInclu_2016pre/TTToHadronic.root Histo/HistoInclu_2016pre/TTToSemiLeptonic.root Histo/HistoInclu_2016pre/TTTo2L2Nu.root
python3 Gethisto_Inclusive.py 2016pre SingleMuonB data_obs
python3 Gethisto_Inclusive.py 2016pre SingleMuonC data_obs
python3 Gethisto_Inclusive.py 2016pre SingleMuonD data_obs
python3 Gethisto_Inclusive.py 2016pre SingleMuonE data_obs
python3 Gethisto_Inclusive.py 2016pre SingleMuonF data_obs
hadd -f Histo/HistoInclu_2016pre/SingleMuon.root Histo/HistoInclu_2016pre/SingleMuonB.root Histo/HistoInclu_2016pre/SingleMuonC.root Histo/HistoInclu_2016pre/SingleMuonD.root Histo/HistoInclu_2016pre/SingleMuonE.root Histo/HistoInclu_2016pre/SingleMuonF.root
python3 Create_fake_inclusive.py --year 2016pre
hadd -f Histo/HistoInclu_2016pre/Inclusive_all.root Histo/HistoInclu_2016pre/ZTT.root Histo/HistoInclu_2016pre/ZLL.root Histo/HistoInclu_2016pre/VV.root Histo/HistoInclu_2016pre/TT.root Histo/HistoInclu_2016pre/ST.root Histo/HistoInclu_2016pre/Fake.root Histo/HistoInclu_2016pre/GGToTauTau.root Histo/HistoInclu_2016pre/SingleMuon.root