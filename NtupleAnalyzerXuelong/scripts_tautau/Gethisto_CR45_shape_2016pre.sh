python3 Gethisto_CR45_shape.py 2016pre GGToTauTau_Ctb20 GGTT
python3 Gethisto_CR45_shape.py 2016pre GGToWW GGWW
python3 Gethisto_CR45_shape.py 2016pre GGToElEl GGEE
python3 Gethisto_CR45_shape.py 2016pre DY ZTT
python3 Gethisto_CR45_shape.py 2016pre ST_t_top ST
python3 Gethisto_CR45_shape.py 2016pre ST_t_antitop ST
python3 Gethisto_CR45_shape.py 2016pre ST_tW_top ST
python3 Gethisto_CR45_shape.py 2016pre ST_tW_antitop ST
hadd -f Histo/HistoCR45_2016pre/ST.root Histo/HistoCR45_2016pre/ST_t_top.root Histo/HistoCR45_2016pre/ST_t_antitop.root Histo/HistoCR45_2016pre/ST_tW_top.root Histo/HistoCR45_2016pre/ST_tW_antitop.root 
python3 Gethisto_CR45_shape.py 2016pre WZ2Q2L VV
python3 Gethisto_CR45_shape.py 2016pre WZ3LNu VV
python3 Gethisto_CR45_shape.py 2016pre VV2L2Nu VV
python3 Gethisto_CR45_shape.py 2016pre ZZ2Q2L VV
python3 Gethisto_CR45_shape.py 2016pre ZZ4L VV
hadd -f Histo/HistoCR45_2016pre/VV.root Histo/HistoCR45_2016pre/WZ2Q2L.root Histo/HistoCR45_2016pre/WZ3LNu.root Histo/HistoCR45_2016pre/VV2L2Nu.root Histo/HistoCR45_2016pre/ZZ2Q2L.root Histo/HistoCR45_2016pre/ZZ4L.root
python3 Gethisto_CR45_shape.py 2016pre TTTo2L2Nu TT
python3 Gethisto_CR45_shape.py 2016pre TTToHadronic TT
python3 Gethisto_CR45_shape.py 2016pre TTToSemiLeptonic TT
hadd -f Histo/HistoCR45_2016pre/TT.root Histo/HistoCR45_2016pre/TTToHadronic.root Histo/HistoCR45_2016pre/TTToSemiLeptonic.root Histo/HistoCR45_2016pre/TTTo2L2Nu.root
python3 Gethisto_CR45_shape.py 2016pre TauB data_obs
python3 Gethisto_CR45_shape.py 2016pre TauC data_obs
python3 Gethisto_CR45_shape.py 2016pre TauD data_obs
python3 Gethisto_CR45_shape.py 2016pre TauE data_obs
python3 Gethisto_CR45_shape.py 2016pre TauF data_obs
hadd -f Histo/HistoCR45_2016pre/Tau.root Histo/HistoCR45_2016pre/TauB.root Histo/HistoCR45_2016pre/TauC.root Histo/HistoCR45_2016pre/TauD.root Histo/HistoCR45_2016pre/TauE.root Histo/HistoCR45_2016pre/TauF.root
hadd -f Histo/HistoCR45_2016pre/Taug2_tautau_2016pre.root Histo/HistoCR45_2016pre/ZTT.root Histo/HistoCR45_2016pre/VV.root Histo/HistoCR45_2016pre/TT.root Histo/HistoCR45_2016pre/ST.root Histo/HistoCR45_2016pre/Fake.root Histo/HistoCR45_2016pre/GGToWW.root Histo/HistoCR45_2016pre/GGToElEl.root Histo/HistoCR45_2016pre/GGToTauTau_Ctb20.root Histo/HistoCR45_2016pre/Tau.root
