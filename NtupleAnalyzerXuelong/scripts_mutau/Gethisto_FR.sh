python3 Gethisto_FR.py 2018 DY
python3 Gethisto_FR.py 2018 ST_t_top
python3 Gethisto_FR.py 2018 ST_t_antitop
python3 Gethisto_FR.py 2018 ST_tW_top
python3 Gethisto_FR.py 2018 ST_tW_antitop
hadd -f Histo/HistoforFR_2018/ST.root Histo/HistoforFR_2018/ST_t_top.root Histo/HistoforFR_2018/ST_t_antitop.root Histo/HistoforFR_2018/ST_tW_top.root Histo/HistoforFR_2018/ST_tW_antitop.root 
python3 Gethisto_FR.py 2018 W
python3 Gethisto_FR.py 2018 W1
python3 Gethisto_FR.py 2018 W2
python3 Gethisto_FR.py 2018 W3
python3 Gethisto_FR.py 2018 W4
hadd -f Histo/HistoforFR_2018/Wall.root Histo/HistoforFR_2018/W.root Histo/HistoforFR_2018/W1.root Histo/HistoforFR_2018/W2.root Histo/HistoforFR_2018/W3.root Histo/HistoforFR_2018/W4.root 
python3 Gethisto_FR.py 2018 WW2L2Nu
python3 Gethisto_FR.py 2018 WZ2Q2L
python3 Gethisto_FR.py 2018 WZ3LNu
python3 Gethisto_FR.py 2018 ZZ2L2Nu
python3 Gethisto_FR.py 2018 ZZ2Q2L
python3 Gethisto_FR.py 2018 ZZ4L
hadd -f Histo/HistoforFR_2018/VV.root Histo/HistoforFR_2018/WW2L2Nu.root Histo/HistoforFR_2018/WZ2Q2L.root Histo/HistoforFR_2018/WZ3LNu.root Histo/HistoforFR_2018/ZZ2L2Nu.root Histo/HistoforFR_2018/ZZ2Q2L.root Histo/HistoforFR_2018/ZZ4L.root
python3 Gethisto_FR.py 2018 TTTo2L2Nu
python3 Gethisto_FR.py 2018 TTToHadronic
python3 Gethisto_FR.py 2018 TTToSemiLeptonic
hadd -f Histo/HistoforFR_2018/TT.root Histo/HistoforFR_2018/TTToHadronic.root Histo/HistoforFR_2018/TTToSemiLeptonic.root Histo/HistoforFR_2018/TTTo2L2Nu.root
hadd -f Histo/HistoforFR_2018/MC.root Histo/HistoforFR_2018/DY.root Histo/HistoforFR_2018/ST.root Histo/HistoforFR_2018/VV.root Histo/HistoforFR_2018/TT.root
python3 Gethisto_FR.py 2018 SingleMuonA
python3 Gethisto_FR.py 2018 SingleMuonB
python3 Gethisto_FR.py 2018 SingleMuonC
python3 Gethisto_FR.py 2018 SingleMuonD
hadd -f Histo/HistoforFR_2018/SingleMuon.root Histo/HistoforFR_2018/SingleMuonA.root Histo/HistoforFR_2018/SingleMuonB.root Histo/HistoforFR_2018/SingleMuonC.root Histo/HistoforFR_2018/SingleMuonD.root
python3 CreateFRhist.py --year 2018
python3 CreateFraction.py --year 2018