#!/bin/bash
year=${1}
startMsg="Job started on "`date`
echo $startMsg

cd /afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong
source setup.sh

cd /afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/scripts_tautau

for channel in tt_3
do
    echo "python3 plotCR3_tautau_3years.py -y ${year} -c ${channel} -v Acopl"
    python3 plotCR3_tautau_3years.py -y ${year} -c ${channel} -v Acopl
done