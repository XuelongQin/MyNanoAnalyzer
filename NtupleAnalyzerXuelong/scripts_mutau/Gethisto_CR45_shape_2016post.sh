python3 Gethisto_CR45_shape.py 2016post GGToTauTau_Ctb20 GGTT
python3 Gethisto_CR45_shape.py 2016post GGToWW GGWW
python3 Gethisto_CR45_shape.py 2016post GGToMuMu GGMM
python3 Gethisto_CR45_shape.py 2016post DY ZTT
python3 Gethisto_CR45_shape.py 2016post DY ZLL
python3 Gethisto_CR45_shape.py 2016post ST_t_top ST
python3 Gethisto_CR45_shape.py 2016post ST_t_antitop ST
python3 Gethisto_CR45_shape.py 2016post ST_tW_top ST
python3 Gethisto_CR45_shape.py 2016post ST_tW_antitop ST
hadd -f Histo/HistoCR45_2016post/ST.root Histo/HistoCR45_2016post/ST_t_top.root Histo/HistoCR45_2016post/ST_t_antitop.root Histo/HistoCR45_2016post/ST_tW_top.root Histo/HistoCR45_2016post/ST_tW_antitop.root 
python3 Gethisto_CR45_shape.py 2016post WZ2Q2L VV
python3 Gethisto_CR45_shape.py 2016post WZ3LNu VV
python3 Gethisto_CR45_shape.py 2016post VV2L2Nu VV
python3 Gethisto_CR45_shape.py 2016post ZZ2Q2L VV
python3 Gethisto_CR45_shape.py 2016post ZZ4L VV
hadd -f Histo/HistoCR45_2016post/VV.root Histo/HistoCR45_2016post/WZ2Q2L.root Histo/HistoCR45_2016post/WZ3LNu.root Histo/HistoCR45_2016post/VV2L2Nu.root Histo/HistoCR45_2016post/ZZ2Q2L.root Histo/HistoCR45_2016post/ZZ4L.root
python3 Gethisto_CR45_shape.py 2016post TTTo2L2Nu TT
python3 Gethisto_CR45_shape.py 2016post TTToHadronic TT
python3 Gethisto_CR45_shape.py 2016post TTToSemiLeptonic TT
hadd -f Histo/HistoCR45_2016post/TT.root Histo/HistoCR45_2016post/TTToHadronic.root Histo/HistoCR45_2016post/TTToSemiLeptonic.root Histo/HistoCR45_2016post/TTTo2L2Nu.root
python3 Gethisto_CR45_shape.py 2016post SingleMuonF data_obs
python3 Gethisto_CR45_shape.py 2016post SingleMuonG data_obs
python3 Gethisto_CR45_shape.py 2016post SingleMuonH data_obs
hadd -f Histo/HistoCR45_2016post/SingleMuon.root Histo/HistoCR45_2016post/SingleMuonF.root Histo/HistoCR45_2016post/SingleMuonG.root Histo/HistoCR45_2016post/SingleMuonH.root
hadd -f Histo/HistoCR45_2016post/Taug2_mutau_2016post.root Histo/HistoCR45_2016post/ZTT.root Histo/HistoCR45_2016post/ZLL.root Histo/HistoCR45_2016post/VV.root Histo/HistoCR45_2016post/TT.root Histo/HistoCR45_2016post/ST.root Histo/HistoCR45_2016post/Fake.root Histo/HistoCR45_2016post/GGToWW.root Histo/HistoCR45_2016post/GGToMuMu.root Histo/HistoCR45_2016post/GGToTauTau_Ctb20.root Histo/HistoCR45_2016post/SingleMuon.root
