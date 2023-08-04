python3 Gethisto_SR_shape.py 2016pre GGToTauTau_Ctb20 GGTT
python3 Gethisto_SR_shape.py 2016pre DY ZTT
python3 Gethisto_SR_shape.py 2016pre DY ZLL
python3 Gethisto_SR_shape.py 2016pre ST_t_top ST
python3 Gethisto_SR_shape.py 2016pre ST_t_antitop ST
python3 Gethisto_SR_shape.py 2016pre ST_tW_top ST
python3 Gethisto_SR_shape.py 2016pre ST_tW_antitop ST
hadd -f Histo/HistoSR_2016pre/ST.root Histo/HistoSR_2016pre/ST_t_top.root Histo/HistoSR_2016pre/ST_t_antitop.root Histo/HistoSR_2016pre/ST_tW_top.root Histo/HistoSR_2016pre/ST_tW_antitop.root 
python3 Gethisto_SR_shape.py 2016pre WW2L2Nu VV
python3 Gethisto_SR_shape.py 2016pre WZ2Q2L VV
python3 Gethisto_SR_shape.py 2016pre WZ3LNu VV
python3 Gethisto_SR_shape.py 2016pre ZZ2L2Nu VV
python3 Gethisto_SR_shape.py 2016pre ZZ2Q2L VV
python3 Gethisto_SR_shape.py 2016pre ZZ4L VV
hadd -f Histo/HistoSR_2016pre/VV.root Histo/HistoSR_2016pre/WW2L2Nu.root Histo/HistoSR_2016pre/WZ2Q2L.root Histo/HistoSR_2016pre/WZ3LNu.root Histo/HistoSR_2016pre/ZZ2L2Nu.root Histo/HistoSR_2016pre/ZZ2Q2L.root Histo/HistoSR_2016pre/ZZ4L.root
python3 Gethisto_SR_shape.py 2016pre TTTo2L2Nu TT
python3 Gethisto_SR_shape.py 2016pre TTToHadronic TT
python3 Gethisto_SR_shape.py 2016pre TTToSemiLeptonic TT
hadd -f Histo/HistoSR_2016pre/TT.root Histo/HistoSR_2016pre/TTToHadronic.root Histo/HistoSR_2016pre/TTToSemiLeptonic.root Histo/HistoSR_2016pre/TTTo2L2Nu.root
python3 Gethisto_SR_shape.py 2016pre SingleMuonB data_obs
python3 Gethisto_SR_shape.py 2016pre SingleMuonC data_obs
python3 Gethisto_SR_shape.py 2016pre SingleMuonD data_obs
python3 Gethisto_SR_shape.py 2016pre SingleMuonE data_obs
python3 Gethisto_SR_shape.py 2016pre SingleMuonF data_obs
hadd -f Histo/HistoSR_2016pre/SingleMuon.root Histo/HistoSR_2016pre/SingleMuonB.root Histo/HistoSR_2016pre/SingleMuonC.root Histo/HistoSR_2016pre/SingleMuonD.root Histo/HistoSR_2016pre/SingleMuonE.root Histo/HistoSR_2016pre/SingleMuonF.root
hadd -f Histo/HistoSR_2016pre/Taug2_mutau_2016pre.root Histo/HistoSR_2016pre/ZTT.root Histo/HistoSR_2016pre/ZLL.root Histo/HistoSR_2016pre/VV.root Histo/HistoSR_2016pre/TT.root Histo/HistoSR_2016pre/ST.root Histo/HistoSR_2016pre/Fake.root Histo/HistoSR_2016pre/GGToTauTau_Ctb20.root Histo/HistoSR_2016pre/SingleMuon.root
python3 Gethisto_SR_BSM.py 2016pre
