with open("/workspaces/ACE-BOOTCAMP2026/DAY3/program7.py", "rb") as f:
   content = f.read(2000)
with open("/workspaces/ACE-BOOTCAMP2026/DAY3/program7.py", "wb") as cf:
      while content>0:
       cf.write(content)
       content = f.read(2000)