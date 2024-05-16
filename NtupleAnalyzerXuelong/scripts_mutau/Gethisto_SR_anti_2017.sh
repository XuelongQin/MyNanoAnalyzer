python3 Gethisto_SR_anti.py 2017 DY ZTT
python3 Gethisto_SR_anti.py 2017 DY ZLL
python3 Gethisto_SR_anti.py 2017 ST_t_top ST
python3 Gethisto_SR_anti.py 2017 ST_t_antitop ST
python3 Gethisto_SR_anti.py 2017 ST_tW_top ST
python3 Gethisto_SR_anti.py 2017 ST_tW_antitop ST
hadd -f Histo/HistoSR_anti_2017/ST.root Histo/HistoSR_anti_2017/ST_t_top.root Histo/HistoSR_anti_2017/ST_t_antitop.root Histo/HistoSR_anti_2017/ST_tW_top.root Histo/HistoSR_anti_2017/ST_tW_antitop.root 
python3 Gethisto_SR_anti.py 2017 WZ2Q2L VV
python3 Gethisto_SR_anti.py 2017 WZ3LNu VV
python3 Gethisto_SR_anti.py 2017 VV2L2Nu VV
python3 Gethisto_SR_anti.py 2017 ZZ2Q2L VV
python3 Gethisto_SR_anti.py 2017 ZZ4L VV
hadd -f Histo/HistoSR_anti_2017/VV.root Histo/HistoSR_anti_2017/WZ2Q2L.root Histo/HistoSR_anti_2017/WZ3LNu.root Histo/HistoSR_anti_2017/VV2L2Nu.root Histo/HistoSR_anti_2017/ZZ2Q2L.root Histo/HistoSR_anti_2017/ZZ4L.root
python3 Gethisto_SR_anti.py 2017 TTTo2L2Nu TT
python3 Gethisto_SR_anti.py 2017 TTToHadronic TT
python3 Gethisto_SR_anti.py 2017 TTToSemiLeptonic TT
hadd -f Histo/HistoSR_anti_2017/TT.root Histo/HistoSR_anti_2017/TTToHadronic.root Histo/HistoSR_anti_2017/TTToSemiLeptonic.root Histo/HistoSR_anti_2017/TTTo2L2Nu.root
python3 Gethisto_SR_anti.py 2017 SingleMuonB data_obs
python3 Gethisto_SR_anti.py 2017 SingleMuonC data_obs
python3 Gethisto_SR_anti.py 2017 SingleMuonD data_obs
python3 Gethisto_SR_anti.py 2017 SingleMuonE data_obs
python3 Gethisto_SR_anti.py 2017 SingleMuonF data_obs
hadd -f Histo/HistoSR_anti_2017/SingleMuon.root Histo/HistoSR_anti_2017/SingleMuonB.root Histo/HistoSR_anti_2017/SingleMuonC.root Histo/HistoSR_anti_2017/SingleMuonD.root Histo/HistoSR_anti_2017/SingleMuonE.root Histo/HistoSR_anti_2017/SingleMuonF.root
python3 Create_fake_SR.py --year 2017
