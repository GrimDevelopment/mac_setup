#!/usr/bin/env python

import sys
import subprocess

addigy = "sudo curl -o /tmp/macinstall https://agents.addigy.com/installer-darwin-amd64 && sudo chmod +x /tmp/macinstall && sudo /tmp/macinstall realm=prod orgid=7a000f1d-8057-4066-b67f-c9344ae0d799 policy_id=5320e423-676b-4e1f-b2db-11181c170585"
split = addigy.split("&&")
split1 = split[0].split()
split2 = split[1].split()
split3 = split[2].split()

print split

subprocess.call(split1)
subprocess.call(split2)
subprocess.call(split3)

sys.exit(0)