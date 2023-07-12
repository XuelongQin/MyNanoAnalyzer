python3 Gethisto_FR.py 2016post DY
python3 Gethisto_FR.py 2016post ST_t_top
python3 Gethisto_FR.py 2016post ST_t_antitop
python3 Gethisto_FR.py 2016post ST_tW_top
python3 Gethisto_FR.py 2016post ST_tW_antitop
hadd -f Histo/HistoforFR_2016post/ST.root Histo/HistoforFR_2016post/ST_t_top.root Histo/HistoforFR_2016post/ST_t_antitop Histo/HistoforFR_2016post/ST_tW_top.root Histo/HistoforFR_2016post/ST_tW_antitop.root 
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
python3 Gethisto_FR.py 2016post TauF
python3 Gethisto_FR.py 2016post TauG
python3 Gethisto_FR.py 2016post TauH
hadd -f Histo/HistoforFR_2016post/Tau.root Histo/HistoforFR_2016post/TauF.root Histo/HistoforFR_2016post/TauG.root Histo/HistoforFR_2016post/TauH.root
python3 CreateFRhist.py --year 2016post