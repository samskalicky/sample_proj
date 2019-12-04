# sample_proj
sample project that combines C++/Python as a pip wheel


Flow that we want
-------------------
Build
Test
Package
Deploy

1. C++ code
2. Python code that calls C++ code
  - ctypes (no FFI)
  - https://solarianprogrammer.com/2019/07/18/python-using-c-cpp-libraries-ctypes/
3. Package all the code into a pip wheel
	- https://packaging.python.org/tutorials/packaging-projects/
4. Tests
6. Setting up Jenkins on AWS with Amazon Linux 2
  - https://medium.com/faun/ci-cd-pipeline-with-jenkins-and-aws-s3-c08a3656d381
