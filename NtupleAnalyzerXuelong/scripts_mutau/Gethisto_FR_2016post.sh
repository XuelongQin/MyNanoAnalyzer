python3 Gethisto_FR.py 2016post DY
python3 Gethisto_FR.py 2016post ST_t_top
python3 Gethisto_FR.py 2016post ST_t_antitop
python3 Gethisto_FR.py 2016post ST_tW_top
python3 Gethisto_FR.py 2016post ST_tW_antitop
hadd -f Histo/HistoforFR_2016post/ST.root Histo/HistoforFR_2016post/ST_t_top.root Histo/HistoforFR_2016post/ST_t_antitop.root Histo/HistoforFR_2016post/ST_tW_top.root Histo/HistoforFR_2016post/ST_tW_antitop.root 
python3 Gethisto_FR.py 2016post W
python3 Gethisto_FR.py 2016post W1
python3 Gethisto_FR.py 2016post W2
python3 Gethisto_FR.py 2016post W3
python3 Gethisto_FR.py 2016post W4
hadd -f Histo/HistoforFR_2016post/Wall.root Histo/HistoforFR_2016post/W.root Histo/HistoforFR_2016post/W1.root Histo/HistoforFR_2016post/W2.root Histo/HistoforFR_2016post/W3.root Histo/HistoforFR_2016post/W4.root 
python3 Gethisto_FR.py 2016post WW2L2Nu
python3 Gethisto_FR.py 2016post WZ2Q2L
python3 Gethisto_FR.py 2016post WZ3LNu
python3 Gethisto_FR.py 2016post ZZ2L2Nu
python3 Gethisto_FR.py 2016post ZZ2Q2L
python3 Gethisto_FR.py 2016post ZZ4L
hadd -f Histo/HistoforFR_2016post/VV.root Histo/HistoforFR_2016post/WW2L2Nu.root Histo/HistoforFR_2016post/WZ2Q2L.root Histo/HistoforFR_2016post/WZ3LNu.root Histo/HistoforFR_2016post/ZZ2L2Nu.root Histo/HistoforFR_2016post/ZZ2Q2L.root Histo/HistoforFR_2016post/ZZ4L.root
python3 Gethisto_FR.py 2016post TTTo2L2Nu
python3 Gethisto_FR.py 2016post TTToHadronic
python3 Gethisto_FR.py 2016post TTToSemiLeptonic
hadd -f Histo/HistoforFR_2016post/TT.root Histo/HistoforFR_2016post/TTToHadronic.root Histo/HistoforFR_2016post/TTToSemiLeptonic.root Histo/HistoforFR_2016post/TTTo2L2Nu.root
hadd -f Histo/HistoforFR_2016post/MC.root Histo/HistoforFR_2016post/DY.root Histo/HistoforFR_2016post/ST.root Histo/HistoforFR_2016post/VV.root Histo/HistoforFR_2016post/TT.root
python3 Gethisto_FR.py 2016post SingleMuonF
python3 Gethisto_FR.py 2016post SingleMuonG
python3 Gethisto_FR.py 2016post SingleMuonH
hadd -f Histo/HistoforFR_2016post/SingleMuon.root Histo/HistoforFR_2016post/SingleMuonF.root Histo/HistoforFR_2016post/SingleMuonG.root Histo/HistoforFR_2016post/SingleMuonH.root
python3 CreateFRhist.py --year 2016post
python3 CreateFraction.py --year 2016post