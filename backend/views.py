from django.shortcuts import render
from .scripts.gasmask_master.test_driver import lookup

scripts_location = "E:\Study Material\Final Year Project"

# Create your views here.
def home(request):
    return render(request, "index.html")


def farji(request):
    return render(request, "farji.html")

def scanA(request):
    if request.method == "POST":
        import subprocess

        site = str(request.POST["website"])
        output = subprocess.check_output(
            [
                #"C:\\Program Files (x86)\\Nmap\\nmap.exe",
                "nmap",
                "-A",
                "-v",
                #"python3",
               #"/root/Music/OSINT/osint4/osint_tools_security_auditing/checkIpDetails.py",
               #"--domain",
                site,      
            ]
        ).decode("utf-8").split("\n")

        #output = output[]

        # output = lookup(site)

        return render(
            request, "scanA.html", {"data": output}
        )
    else:
        return render(request, "scanA.html")

def IP_Lookup(request):
    if request.method == "POST":
        import subprocess

        site = str(request.POST["website"])
        output = subprocess.check_output(
            [
                #"python3",
               #"/root/Music/OSINT/osint4/osint_tools_security_auditing/checkIpDetails.py",
               #"--domain",
               "py",
               "C:\\Users\\Mridul\\Desktop\\OSINT\\osint4\\osint_tools_security_auditing\\checkIpDetails.py",
               "-d",
                site,      
            ]
        ).decode("utf-8").split("\n")

        #output = str(output[:-2])

        # output = lookup(site)

        return render(
            request, "ip.html", {"data": output}
        )
    else:
        return render(request, "ip.html")

def social(request):
    if request.method == "POST":
        import subprocess

        site = str(request.POST["website"])
        output = subprocess.check_output(
            [
               #"python3",
               #"/root/Music/OSINT/osint4/osint_tools_security_auditing/check_social_networks.py",
               # "-a",
               "py",
               "C:\\Users\\Mridul\\Desktop\\OSINT\\osint4\\osint_tools_security_auditing\\check_social_networks.py",
               "-a",
                site,
            ]
        ).decode("utf-8").split(" ")

        # output = str(output[:-2])

        # output = lookup(site)

        return render(
            request, "social.html", {"data": output}
        )
    else:
        return render(request, "social.html")


def builtwith(request):
    if request.method == "POST":
        import subprocess

        site = str(request.POST["website"])
        output = subprocess.check_output(
            [
                #"python3",
				#"/root/Music/OSINT/osint4/osint_tools_security_auditing/BuiltWith.py",
                #"--domain",
                "py",
               "C:\\Users\\Mridul\\Desktop\\OSINT\\osint4\\osint_tools_security_auditing\\BuiltWith.py",
               "--domain",
                site,
            ]
        ).decode("utf-8").split("\n")

        #output = str(output[:-2])

        # output = lookup(site)

        return render(
            request, "built.html", {"data": output}
        )
    else:
        return render(request, "built.html")

def virus(request):
    if request.method == "POST":
        import subprocess

        site = str(request.POST["website"])
        output = subprocess.check_output(
            [
                #"python3",
				#"/root/Music/OSINT/osint4/osint_tools_security_auditing/virusTotal.py",
                #"-d",
                "py",
               "C:\\Users\\Mridul\\Desktop\\OSINT\\osint4\\osint_tools_security_auditing\\virusTotal.py",
               "-d",
                site,
            ]
        ).decode("utf-8").split("\n")

        #output = str(output[:-2])

        # output = lookup(site)

        return render(
            request, "virus.html", {"data": output}
        )
    else:
        return render(request, "virus.html")


def urlemail(request):
    if request.method == "POST":
        import subprocess

        site = str(request.POST["website"])
        output = subprocess.check_output(
            [
                #"python3",
				#"/root/Music/OSINT/osint4/osint_tools_security_auditing/get_emails_from_url.py",
                #"-d",
                "py",
               "C:\\Users\\Mridul\\Desktop\\OSINT\\osint4\\osint_tools_security_auditing\\get_emails_from_url.py",
               "-d",
                site,
            ]
        ).decode("utf-8").split("\n")

        # output = str(output[:-2])

        # output = lookup(site)

        return render(
            request, "urlemail.html", {"data": output}
        )
    else:
        return render(request, "urlemail.html")

def emailosint(request):
    if request.method == "POST":
        import subprocess

        site = str(request.POST["website"])
        output = subprocess.check_output(
            [
                #"python3",
				#"/root/Music/OSINT/osint4/osint_tools_security_auditing/get_emails_from_url.py",
                #"-d",
                "py",
               "C:\\Users\\Mridul\\Desktop\\OSINT\\osint4\\Infoga-master\\infoga.py",
               "-d",
                site,
                "-b",
                "-v",
                "3",
            ]
        ).decode("utf-8").split("\n")

        # output = str(output[:-2])

        # output = lookup(site)

        return render(
            request, "emailosint.html", {"data": output}
        )
    else:
        return render(request, "emailosint.html")


def OS(request):
    if request.method == "POST":
        import subprocess

        site = str(request.POST["website"])
        output = subprocess.check_output(
            [
                "nmap",
                "-O",
                "-vv",
                site,
            ]
        ).decode("utf-8").split("\n")

        # output = str(output[:-2])

        # output = lookup(site)

        return render(
            request, "OS.html", {"data": output}
        )
    else:
        return render(request, "OS.html")

def phone(request):
    if request.method == "POST":
        import subprocess

        site = str(request.POST["website"])
        output = subprocess.check_output(
            [
                "py",
                "C:\\Users\\Mridul\\Desktop\\OSINT\\osint4\\main\\phone.py",
                "+91"+site,
            ]
        ).decode("utf-8").split("\n")

        # output = str(output[:-2])

        # output = lookup(site)

        return render(
            request, "phone.html", {"data": output}
        )
    else:
        return render(request, "phone.html")