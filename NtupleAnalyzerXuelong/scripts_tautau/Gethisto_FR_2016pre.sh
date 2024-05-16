python3 Gethisto_FR.py 2016pre GGToTauTau_Ctb20
python3 Gethisto_FR.py 2016pre GGToElEl
python3 Gethisto_FR.py 2016pre GGToWW
python3 Gethisto_FR.py 2016pre DY
python3 Gethisto_FR.py 2016pre ST_t_top
python3 Gethisto_FR.py 2016pre ST_t_antitop
python3 Gethisto_FR.py 2016pre ST_tW_top
python3 Gethisto_FR.py 2016pre ST_tW_antitop
hadd -f Histo/HistoforFR_2016pre/ST.root Histo/HistoforFR_2016pre/ST_t_top.root Histo/HistoforFR_2016pre/ST_t_antitop Histo/HistoforFR_2016pre/ST_tW_top.root Histo/HistoforFR_2016pre/ST_tW_antitop.root 
python3 Gethisto_FR.py 2016pre WZ2Q2L
python3 Gethisto_FR.py 2016pre WZ3LNu
python3 Gethisto_FR.py 2016pre VV2L2Nu
python3 Gethisto_FR.py 2016pre ZZ2Q2L
python3 Gethisto_FR.py 2016pre ZZ4L
hadd -f Histo/HistoforFR_2016pre/VV.root Histo/HistoforFR_2016pre/WZ2Q2L.root Histo/HistoforFR_2016pre/WZ3LNu.root Histo/HistoforFR_2016pre/VV2L2Nu.root Histo/HistoforFR_2016pre/ZZ2Q2L.root Histo/HistoforFR_2016pre/ZZ4L.root
python3 Gethisto_FR.py 2016pre TTTo2L2Nu
python3 Gethisto_FR.py 2016pre TTToHadronic
python3 Gethisto_FR.py 2016pre TTToSemiLeptonic
hadd -f Histo/HistoforFR_2016pre/TT.root Histo/HistoforFR_2016pre/TTToHadronic.root Histo/HistoforFR_2016pre/TTToSemiLeptonic.root Histo/HistoforFR_2016pre/TTTo2L2Nu.root
hadd -f Histo/HistoforFR_2016pre/MC.root Histo/HistoforFR_2016pre/DY.root Histo/HistoforFR_2016pre/ST.root Histo/HistoforFR_2016pre/VV.root Histo/HistoforFR_2016pre/TT.root Histo/HistoforFR_2016pre/GGToElEl.root Histo/HistoforFR_2016pre/GGToWW.root 
python3 Gethisto_FR.py 2016pre TauB
python3 Gethisto_FR.py 2016pre TauC
python3 Gethisto_FR.py 2016pre TauD
python3 Gethisto_FR.py 2016pre TauE
python3 Gethisto_FR.py 2016pre TauF
hadd -f Histo/HistoforFR_2016pre/Tau.root Histo/HistoforFR_2016pre/TauB.root Histo/HistoforFR_2016pre/TauC.root Histo/HistoforFR_2016pre/TauD.root Histo/HistoforFR_2016pre/TauE.root Histo/HistoforFR_2016pre/TauF.root
python3 CreateFRhist.py --year 2016pre