python3 Gethisto_FR.py 2017 GGToTauTau_Ctb20
python3 Gethisto_FR.py 2017 GGToMuMu
python3 Gethisto_FR.py 2017 GGToWW
python3 Gethisto_FR.py 2017 DY
python3 Gethisto_FR.py 2017 ST_t_top
python3 Gethisto_FR.py 2017 ST_t_antitop
python3 Gethisto_FR.py 2017 ST_tW_top
python3 Gethisto_FR.py 2017 ST_tW_antitop
hadd -f Histo/HistoforFR_2017/ST.root Histo/HistoforFR_2017/ST_t_top.root Histo/HistoforFR_2017/ST_t_antitop.root Histo/HistoforFR_2017/ST_tW_top.root Histo/HistoforFR_2017/ST_tW_antitop.root 
python3 Gethisto_FR.py 2017 W
python3 Gethisto_FR.py 2017 W1
python3 Gethisto_FR.py 2017 W2
python3 Gethisto_FR.py 2017 W3
python3 Gethisto_FR.py 2017 W4
hadd -f Histo/HistoforFR_2017/Wall.root Histo/HistoforFR_2017/W.root Histo/HistoforFR_2017/W1.root Histo/HistoforFR_2017/W2.root Histo/HistoforFR_2017/W3.root Histo/HistoforFR_2017/W4.root 
python3 Gethisto_FR.py 2017 WZ2Q2L
python3 Gethisto_FR.py 2017 WZ3LNu
python3 Gethisto_FR.py 2017 VV2L2Nu
python3 Gethisto_FR.py 2017 ZZ2Q2L
python3 Gethisto_FR.py 2017 ZZ4L
hadd -f Histo/HistoforFR_2017/VV.root Histo/HistoforFR_2017/WZ2Q2L.root Histo/HistoforFR_2017/WZ3LNu.root Histo/HistoforFR_2017/VV2L2Nu.root Histo/HistoforFR_2017/ZZ2Q2L.root Histo/HistoforFR_2017/ZZ4L.root
python3 Gethisto_FR.py 2017 TTTo2L2Nu
python3 Gethisto_FR.py 2017 TTToHadronic
python3 Gethisto_FR.py 2017 TTToSemiLeptonic
hadd -f Histo/HistoforFR_2017/TT.root Histo/HistoforFR_2017/TTToHadronic.root Histo/HistoforFR_2017/TTToSemiLeptonic.root Histo/HistoforFR_2017/TTTo2L2Nu.root
hadd -f Histo/HistoforFR_2017/MC.root Histo/HistoforFR_2017/DY.root Histo/HistoforFR_2017/ST.root Histo/HistoforFR_2017/VV.root Histo/HistoforFR_2017/TT.root Histo/HistoforFR_2017/GGToMuMu.root Histo/HistoforFR_2017/GGToWW.root 
python3 Gethisto_FR.py 2017 SingleMuonB
python3 Gethisto_FR.py 2017 SingleMuonC
python3 Gethisto_FR.py 2017 SingleMuonD
python3 Gethisto_FR.py 2017 SingleMuonE
python3 Gethisto_FR.py 2017 SingleMuonF
hadd -f Histo/HistoforFR_2017/SingleMuon.root Histo/HistoforFR_2017/SingleMuonB.root Histo/HistoforFR_2017/SingleMuonC.root Histo/HistoforFR_2017/SingleMuonD.root Histo/HistoforFR_2017/SingleMuonE.root Histo/HistoforFR_2017/SingleMuonF.root
python3 CreateFRhist.py --year 2017
python3 CreateFraction.py --year 2017