python3 Gethisto_CR_shape.py 2017 GGToTauTau_Ctb20 GGTT
python3 Gethisto_CR_shape.py 2017 GGToWW GGWW
python3 Gethisto_CR_shape.py 2017 DY ZTT
python3 Gethisto_CR_shape.py 2017 ST_t_top ST
python3 Gethisto_CR_shape.py 2017 ST_t_antitop ST
python3 Gethisto_CR_shape.py 2017 ST_tW_top ST
python3 Gethisto_CR_shape.py 2017 ST_tW_antitop ST
hadd -f Histo/HistoCR_2017/ST.root Histo/HistoCR_2017/ST_t_top.root Histo/HistoCR_2017/ST_t_antitop.root Histo/HistoCR_2017/ST_tW_top.root Histo/HistoCR_2017/ST_tW_antitop.root 
python3 Gethisto_CR_shape.py 2017 WW2L2Nu VV
python3 Gethisto_CR_shape.py 2017 WZ2Q2L VV
python3 Gethisto_CR_shape.py 2017 WZ3LNu VV
python3 Gethisto_CR_shape.py 2017 ZZ2L2Nu VV
python3 Gethisto_CR_shape.py 2017 ZZ2Q2L VV
python3 Gethisto_CR_shape.py 2017 ZZ4L VV
hadd -f Histo/HistoCR_2017/VV.root Histo/HistoCR_2017/WW2L2Nu.root Histo/HistoCR_2017/WZ2Q2L.root Histo/HistoCR_2017/WZ3LNu.root Histo/HistoCR_2017/ZZ2L2Nu.root Histo/HistoCR_2017/ZZ2Q2L.root Histo/HistoCR_2017/ZZ4L.root
python3 Gethisto_CR_shape.py 2017 TTTo2L2Nu TT
python3 Gethisto_CR_shape.py 2017 TTToHadronic TT
python3 Gethisto_CR_shape.py 2017 TTToSemiLeptonic TT
hadd -f Histo/HistoCR_2017/TT.root Histo/HistoCR_2017/TTToHadronic.root Histo/HistoCR_2017/TTToSemiLeptonic.root Histo/HistoCR_2017/TTTo2L2Nu.root
python3 Gethisto_CR_shape.py 2017 TauB data_obs
python3 Gethisto_CR_shape.py 2017 TauC data_obs
python3 Gethisto_CR_shape.py 2017 TauD data_obs
python3 Gethisto_CR_shape.py 2017 TauE data_obs
python3 Gethisto_CR_shape.py 2017 TauF data_obs
hadd -f Histo/HistoCR_2017/Tau.root Histo/HistoCR_2017/TauB.root Histo/HistoCR_2017/TauC.root Histo/HistoCR_2017/TauD.root Histo/HistoCR_2017/TauE.root Histo/HistoCR_2017/TauF.root
hadd -f Histo/HistoCR_2017/Taug2_tautau_2017.root Histo/HistoCR_2017/ZTT.root Histo/HistoCR_2017/VV.root Histo/HistoCR_2017/TT.root Histo/HistoCR_2017/ST.root Histo/HistoCR_2017/Fake.root Histo/HistoCR_2017/GGToWW.root Histo/HistoCR_2017/GGToTauTau_Ctb20.root Histo/HistoCR_2017/Tau.root
