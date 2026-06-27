with open("/workspaces/ACE-BOOTCAMP2026/DAY3/shih-tzu-dog-breed-profile-1117999-hero-5541b7f6f936478ca766d85ff5af202e.jpeg",'rb')as f:
    content=f.read()
    with open("/workspaces/ACE-BOOTCAMP2026/DAY3/shih-tzu-dog-breed-profile-1117999-hero-5541b7f6f936478ca766d85ff5af202e.jpeg","wb")as cf:
        cf.write(content)