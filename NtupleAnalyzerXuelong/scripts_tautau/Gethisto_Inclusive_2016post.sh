python3 Gethisto_Inclusive.py 2016post DY ZTT
python3 Gethisto_Inclusive.py 2016post ST_t_top ST
python3 Gethisto_Inclusive.py 2016post ST_t_antitop ST
python3 Gethisto_Inclusive.py 2016post ST_tW_top ST
python3 Gethisto_Inclusive.py 2016post ST_tW_antitop ST
hadd -f Histo/HistoInclu_2016post/ST.root Histo/HistoInclu_2016post/ST_t_top.root Histo/HistoInclu_2016post/ST_t_antitop.root Histo/HistoInclu_2016post/ST_tW_top.root Histo/HistoInclu_2016post/ST_tW_antitop.root 
python3 Gethisto_Inclusive.py 2016post WZ2Q2L VV
python3 Gethisto_Inclusive.py 2016post WZ3LNu VV
python3 Gethisto_Inclusive.py 2016post VV2L2Nu VV
python3 Gethisto_Inclusive.py 2016post ZZ2Q2L VV
python3 Gethisto_Inclusive.py 2016post ZZ4L VV
hadd -f Histo/HistoInclu_2016post/VV.root Histo/HistoInclu_2016post/WZ2Q2L.root Histo/HistoInclu_2016post/WZ3LNu.root Histo/HistoInclu_2016post/VV2L2Nu.root Histo/HistoInclu_2016post/ZZ2Q2L.root Histo/HistoInclu_2016post/ZZ4L.root
python3 Gethisto_Inclusive.py 2016post TTTo2L2Nu TT
python3 Gethisto_Inclusive.py 2016post TTToHadronic TT
python3 Gethisto_Inclusive.py 2016post TTToSemiLeptonic TT
hadd -f Histo/HistoInclu_2016post/TT.root Histo/HistoInclu_2016post/TTToHadronic.root Histo/HistoInclu_2016post/TTToSemiLeptonic.root Histo/HistoInclu_2016post/TTTo2L2Nu.root
python3 Gethisto_Inclusive.py 2016post TauF data_obs
python3 Gethisto_Inclusive.py 2016post TauG data_obs
python3 Gethisto_Inclusive.py 2016post TauH data_obs
hadd -f Histo/HistoInclu_2016post/Tau.root Histo/HistoInclu_2016post/TauF.root Histo/HistoInclu_2016post/TauG.root Histo/HistoInclu_2016post/TauH.root 
python3 Create_fake_inclusive.py --year 2016post
hadd -f Histo/HistoInclu_2016post/Inclusive_all.root Histo/HistoInclu_2016post/ZTT.root Histo/HistoInclu_2016post/VV.root Histo/HistoInclu_2016post/TT.root Histo/HistoInclu_2016post/ST.root Histo/HistoInclu_2016post/Fake.root Histo/HistoInclu_2016post/GGToTauTau.root Histo/HistoInclu_2016post/Tau.root