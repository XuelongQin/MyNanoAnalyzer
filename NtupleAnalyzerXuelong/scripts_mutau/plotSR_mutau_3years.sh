#!/bin/bash
year=${1}
startMsg="Job started on "`date`
echo $startMsg

cd /afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong
source setup.sh

cd /afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/scripts_mutau

for channel in mt_0 mt_1
do
    echo "python3 plotSR_mutau_3years.py -y ${year} -c ${channel} -v mvis"
    python3 plotSR_mutau_3years.py -y ${year} -c ${channel} -v mvis
done