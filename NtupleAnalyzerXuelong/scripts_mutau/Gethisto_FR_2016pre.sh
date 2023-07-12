python3 Gethisto_FR.py 2016pre DY
python3 Gethisto_FR.py 2016pre ST_t_top
python3 Gethisto_FR.py 2016pre ST_t_antitop
python3 Gethisto_FR.py 2016pre ST_tW_top
python3 Gethisto_FR.py 2016pre ST_tW_antitop
hadd -f Histo/HistoforFR_2016pre/ST.root Histo/HistoforFR_2016pre/ST_t_top.root Histo/HistoforFR_2016pre/ST_t_antitop.root Histo/HistoforFR_2016pre/ST_tW_top.root Histo/HistoforFR_2016pre/ST_tW_antitop.root 
python3 Gethisto_FR.py 2016pre W
python3 Gethisto_FR.py 2016pre W1
python3 Gethisto_FR.py 2016pre W2
python3 Gethisto_FR.py 2016pre W3
python3 Gethisto_FR.py 2016pre W4
hadd -f Histo/HistoforFR_2016pre/Wall.root Histo/HistoforFR_2016pre/W.root Histo/HistoforFR_2016pre/W1.root Histo/HistoforFR_2016pre/W2.root Histo/HistoforFR_2016pre/W3.root Histo/HistoforFR_2016pre/W4.root 
python3 Gethisto_FR.py 2016pre WW2L2Nu
python3 Gethisto_FR.py 2016pre WZ2Q2L
python3 Gethisto_FR.py 2016pre WZ3LNu
python3 Gethisto_FR.py 2016pre ZZ2L2Nu
python3 Gethisto_FR.py 2016pre ZZ2Q2L
python3 Gethisto_FR.py 2016pre ZZ4L
hadd -f Histo/HistoforFR_2016pre/VV.root Histo/HistoforFR_2016pre/WW2L2Nu.root Histo/HistoforFR_2016pre/WZ2Q2L.root Histo/HistoforFR_2016pre/WZ3LNu.root Histo/HistoforFR_2016pre/ZZ2L2Nu.root Histo/HistoforFR_2016pre/ZZ2Q2L.root Histo/HistoforFR_2016pre/ZZ4L.root
python3 Gethisto_FR.py 2016pre TTTo2L2Nu
python3 Gethisto_FR.py 2016pre TTToHadronic
python3 Gethisto_FR.py 2016pre TTToSemiLeptonic
hadd -f Histo/HistoforFR_2016pre/TT.root Histo/HistoforFR_2016pre/TTToHadronic.root Histo/HistoforFR_2016pre/TTToSemiLeptonic.root Histo/HistoforFR_2016pre/TTTo2L2Nu.root
hadd -f Histo/HistoforFR_2016pre/MC.root Histo/HistoforFR_2016pre/DY.root Histo/HistoforFR_2016pre/ST.root Histo/HistoforFR_2016pre/VV.root Histo/HistoforFR_2016pre/TT.root
python3 Gethisto_FR.py 2016pre SingleMuonB
python3 Gethisto_FR.py 2016pre SingleMuonC
python3 Gethisto_FR.py 2016pre SingleMuonD
python3 Gethisto_FR.py 2016pre SingleMuonE
python3 Gethisto_FR.py 2016pre SingleMuonF
hadd -f Histo/HistoforFR_2016pre/SingleMuon.root Histo/HistoforFR_2016pre/SingleMuonB.root Histo/HistoforFR_2016pre/SingleMuonC.root Histo/HistoforFR_2016pre/SingleMuonD.root Histo/HistoforFR_2016pre/SingleMuonE.root Histo/HistoforFR_2016pre/SingleMuonF.root
python3 CreateFRhist.py --year 2016pre
python3 CreateFraction.py --year 2016pre