#1) Install Requirements
echo 'Install Requirements'
pip install -r requirements.txt

#2) Install EasyVVUQ
echo 'Installing EasyVVUQ'
python -m pip install .

#3) Build cannonsim test
echo 'Building cannonsim'
cd tests/cannonsim/src
make 
cd ../../..
