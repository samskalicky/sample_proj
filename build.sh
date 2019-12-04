make
rm -rf joe
mkdir joe
cp -r python/jenkinsProj joe
cp lib/libmylib.so joe/jenkinsProj
cp setup.py joe
cd joe
python setup.py bdist_wheel