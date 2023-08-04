python3 Gethisto_SR_anti.py 2016pre DY ZTT
python3 Gethisto_SR_anti.py 2016pre ST_t_top ST
python3 Gethisto_SR_anti.py 2016pre ST_t_antitop ST
python3 Gethisto_SR_anti.py 2016pre ST_tW_top ST
python3 Gethisto_SR_anti.py 2016pre ST_tW_antitop ST
hadd -f Histo/HistoSR_anti_2016pre/ST.root Histo/HistoSR_anti_2016pre/ST_t_top.root Histo/HistoSR_anti_2016pre/ST_t_antitop.root Histo/HistoSR_anti_2016pre/ST_tW_top.root Histo/HistoSR_anti_2016pre/ST_tW_antitop.root 
python3 Gethisto_SR_anti.py 2016pre WW2L2Nu VV
python3 Gethisto_SR_anti.py 2016pre WZ2Q2L VV
python3 Gethisto_SR_anti.py 2016pre WZ3LNu VV
python3 Gethisto_SR_anti.py 2016pre ZZ2L2Nu VV
python3 Gethisto_SR_anti.py 2016pre ZZ2Q2L VV
python3 Gethisto_SR_anti.py 2016pre ZZ4L VV
hadd -f Histo/HistoSR_anti_2016pre/VV.root Histo/HistoSR_anti_2016pre/WW2L2Nu.root Histo/HistoSR_anti_2016pre/WZ2Q2L.root Histo/HistoSR_anti_2016pre/WZ3LNu.root Histo/HistoSR_anti_2016pre/ZZ2L2Nu.root Histo/HistoSR_anti_2016pre/ZZ2Q2L.root Histo/HistoSR_anti_2016pre/ZZ4L.root
python3 Gethisto_SR_anti.py 2016pre TTTo2L2Nu TT
python3 Gethisto_SR_anti.py 2016pre TTToHadronic TT
python3 Gethisto_SR_anti.py 2016pre TTToSemiLeptonic TT
hadd -f Histo/HistoSR_anti_2016pre/TT.root Histo/HistoSR_anti_2016pre/TTToHadronic.root Histo/HistoSR_anti_2016pre/TTToSemiLeptonic.root Histo/HistoSR_anti_2016pre/TTTo2L2Nu.root
python3 Gethisto_SR_anti.py 2016pre TauB data_obs
python3 Gethisto_SR_anti.py 2016pre TauC data_obs
python3 Gethisto_SR_anti.py 2016pre TauD data_obs
python3 Gethisto_SR_anti.py 2016pre TauE data_obs
python3 Gethisto_SR_anti.py 2016pre TauF data_obs
hadd -f Histo/HistoSR_anti_2016pre/Tau.root Histo/HistoSR_anti_2016pre/TauB.root Histo/HistoSR_anti_2016pre/TauC.root Histo/HistoSR_anti_2016pre/TauD.root Histo/HistoSR_anti_2016pre/TauE.root Histo/HistoSR_anti_2016pre/TauF.root
python3 Create_fake_SR.py --year 2016pre
