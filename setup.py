import setuptools

setuptools.setup(
        name="jenkinsProj",
        version="1.0",
        description="simulating jenkins ci",
        #package_dir={'':'python'},
        packages=setuptools.find_packages(),
        package_data={'':['libmylib.so']}
        )
