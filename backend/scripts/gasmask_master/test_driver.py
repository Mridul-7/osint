import subprocess


def lookup(site):
    scripts_location = "E:\Study Material\Final Year Project\gasmask-master"

    # output = subprocess.check_output(["choice_bowl.py","-","left-choices"])
    output = subprocess.check_output(
        ["python.exe", scripts_location + "\gasmask.py", "-d", site, "-i", "whois",]
    ).decode("utf-8")
    ##subprocess.run(["ls", "-l"])
    return output[:-2]

